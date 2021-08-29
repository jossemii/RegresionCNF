from singleton import Singleton
import threading
from time import sleep
from regresion import iterate_regression
import api_pb2, solvers_dataset_pb2
from threading import Thread, get_ident
from start import DIR, LOGGER, SHA3_256


class Session(metaclass=Singleton):

    def __init__(self, ENVS) -> None:
        self.lock = threading.Lock()
        self.data_set = solvers_dataset_pb2.DataSet()
        self.onnx = None
        Thread(target=self.init, name='Regression', args=(ENVS,)).start()

    # Add new data
    def add_data(self, new_data_set: solvers_dataset_pb2.DataSet) -> None:
        self.lock.acquire()
        for hash, solver_data in new_data_set.data.items():
            if hash in self.data_set.data:
                for cnf, data in solver_data.data.items():
                    if cnf in self.data_set.data[hash].data:
                        self.data_set.data[hash].data[cnf].score = sum([
                            (self.data_set.data[hash].data[cnf].index * self.data_set.data[hash].data[cnf].score),
                            data.index * data.score,
                        ]) / (self.data_set.data[hash].data[cnf].index + data.index)
                        self.data_set.data[hash].data[cnf].index = self.data_set.data[hash].data[cnf].index + data.index
                        
                    else:
                        self.data_set.data[hash].data[cnf].CopyFrom(data)
            else:
                self.data_set.data[hash].CopyFrom(solver_data)
        self.lock.release()
        LOGGER('Dataset updated. ')

    # Return the tensor for the grpc stream method.
    def get_tensor(self) -> api_pb2.onnx__pb2.ONNX:
        # No hay condiciones de carrera aunque lo reescriba en ese momento.
        return self.onnx
    
    # Hasta que se implemente AddTensor en el clasificador.
    def get_data_set(self) -> solvers_dataset_pb2.DataSet:
        return self.data_set

    def init(self, ENVS):
        # set used envs on variables.
        time_for_each_regression_loop = ENVS['TIME_FOR_EACH_REGRESSION_LOOP']
        max_degree = ENVS['MAX_REGRESSION_DEGREE']
        data_set_hash = ""

        def generate_tensor_spec():
            # Performance
            p = api_pb2.hyweb__pb2.Tensor.Index()
            p.id = "score"
            p.hashtag.tag.extend(["performance"])
            # Number clauses
            c = api_pb2.hyweb__pb2.Tensor.Index()
            c.id = "clauses"
            c.hashtag.tag.extend(["number of clauses"])
            # Number of literals
            l = api_pb2.hyweb__pb2.Tensor.Index()
            l.id = "literals"
            l.hashtag.tag.extend(["number of literals"])
            # Solver services
            s = api_pb2.hyweb__pb2.Tensor.Index()
            s.id = "solver"
            s.hashtag.tag.extend(["SATsolver"])
            with open(DIR + '.service/solver.field', 'rb') as f:
                s.field.ParseFromString(f.read())

            tensor_specification = api_pb2.hyweb__pb2.Tensor()
            tensor_specification.index.extend([c, l, s, p])
            tensor_specification.rank = 3
            return tensor_specification

        LOGGER('INIT REGRESSION THREAD '+ str(get_ident()))
        while True:
            sleep(time_for_each_regression_loop)

            # Obtiene una hash del dataset para saber si se han añadido datos.
            actual_hash = SHA3_256(
                value = self.data_set.SerializeToString()
                ).hex()
            LOGGER('Check if dataset was modified ' + actual_hash + data_set_hash)
            if actual_hash != data_set_hash:
                data_set_hash = actual_hash
                
                # Se evita crear condiciones de carrera.
                self.lock.acquire()
                data_set = solvers_dataset_pb2.DataSet()
                data_set.CopyFrom(self.data_set)
                self.lock.release()

                if not self.onnx: self.onnx = api_pb2.onnx__pb2.ONNX()
                self.onnx.CopyFrom(
                    iterate_regression(
                        MAX_DEGREE=max_degree,
                        TENSOR_SPECIFICATION=generate_tensor_spec(),
                        data_set = data_set
                    )
                )