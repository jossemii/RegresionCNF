from types import LambdaType
from singleton import Singleton
import threading
from time import sleep
from regresion import iterate_regression
import solvers_dataset_pb2, onnx_pb2, hyweb_pb2
from threading import Thread, get_ident

class Session(metaclass=Singleton):

    def __init__(self, ENVS: dict, DIR: str, LOGGER: LambdaType, SHA3_256: LambdaType) -> None:
        self.DIR = DIR
        self.LOGGER = LOGGER
        self.SHA3_256 = SHA3_256
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
        self.LOGGER('Dataset updated. ')

    # Return the tensor for the grpc stream method.
    def get_tensor(self) -> onnx_pb2.ONNX:
        # No hay condiciones de carrera aunque lo reescriba en ese momento.
        if self.onnx:
            return self.onnx
        else:
            raise Exception
    
    # Hasta que se implemente AddTensor en el clasificador.
    def get_data_set(self) -> solvers_dataset_pb2.DataSet:
        return self.data_set

    def init(self, ENVS: dict):
        # set used envs on variables.
        time_for_each_regression_loop = ENVS['TIME_FOR_EACH_REGRESSION_LOOP']
        max_degree = ENVS['MAX_REGRESSION_DEGREE']
        data_set_hash = ""

        def generate_tensor_spec():
            # Performance
            p = hyweb_pb2.Tensor.Index()
            p.id = "score"
            p.hashtag.tag.extend(["performance"])
            # Number clauses
            c = hyweb_pb2.Tensor.Index()
            c.id = "clauses"
            c.hashtag.tag.extend(["number of clauses"])
            # Number of literals
            l = hyweb_pb2.Tensor.Index()
            l.id = "literals"
            l.hashtag.tag.extend(["number of literals"])
            # Solver services
            s = hyweb_pb2.Tensor.Index()
            s.id = "solver"
            s.hashtag.tag.extend(["SATsolver"])
            with open(self.DIR + '.service/solver.field', 'rb') as f:
                s.field.ParseFromString(f.read())

            tensor_specification = hyweb_pb2.Tensor()
            tensor_specification.index.extend([c, l, s, p])
            tensor_specification.rank = 3
            return tensor_specification

        self.LOGGER('INIT REGRESSION THREAD '+ str(get_ident()))
        while True:
            sleep(time_for_each_regression_loop)

            # Obtiene una hash del dataset para saber si se han añadido datos.
            actual_hash = self.SHA3_256(
                value = self.data_set.SerializeToString()
                ).hex()
            self.LOGGER('Check if dataset was modified ' + actual_hash + data_set_hash)
            if actual_hash != data_set_hash:
                self.LOGGER('Perform other regresion.')
                data_set_hash = actual_hash
                
                # Se evita crear condiciones de carrera.
                self.lock.acquire()
                data_set = solvers_dataset_pb2.DataSet()
                data_set.CopyFrom(self.data_set)
                self.lock.release()

                if not self.onnx: self.onnx = onnx_pb2.ONNX()
                self.LOGGER('..........')
                self.onnx.CopyFrom(
                    iterate_regression(
                        LOGGER = self.LOGGER,
                        MAX_DEGREE=max_degree,
                        TENSOR_SPECIFICATION=generate_tensor_spec(),
                        data_set = data_set
                    )
                )