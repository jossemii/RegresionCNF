import logging
from session import Session
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s')
LOGGER = lambda message: logging.getLogger().debug(message + '\n')

DIR = '/randomcnf/'
ENVS = {
    'MAX_REGRESSION_DEGREE': 100,
    'TIME_FOR_EACH_REGRESSION_LOOP': 900,
}

import hashlib
# -- The service use sha3-256 for identify internal objects. --
SHA3_256_ID = bytes.fromhex("a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a")
SHA3_256 = lambda value: "" if value is None else hashlib.sha3_256(value).digest()


if __name__ == "__main__":

    from time import sleep
    import grpc, api_pb2, api_pb2_grpc
    from concurrent import futures
    
    # Read __config__ file.
    """
    config = api_pb2.hyweb__pb2.ConfigurationFile()
    config.ParseFromString(
        open('/__config__', 'rb').read()
    )    


    for env_var in config.config.enviroment_variables:
        ENVS[env_var] = type(ENVS[env_var])(
            config.config.enviroment_variables[env_var].value
            )    
    """
      
    _regresion = Session(ENVS=ENVS)

    class RegresionServicer(api_pb2_grpc.SolverServicer):

        def StreamLogs(self, request, context):
            with open('app.log') as file:
                while True:
                    f = api_pb2.File()
                    f.file = file.read()
                    yield f
                    sleep(1)

        def GetTensor(self, request, context):
            while True:
                yield _regresion.get_tensor()
                sleep(ENVS['TIME_FOR_EACH_REGRESSION_LOOP'])
        
        # Hasta que se implemente AddTensor.
        def GetDataSet(self, request, context):
            return _regresion.get_data_set()

        def AddDataSet(self, request, context):
            _regresion.add_data(new_data_set = request)
            return api_pb2.Empty()


    # create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))

    api_pb2_grpc.add_RegresionServicer_to_server(
        RegresionServicer(), server)

    # listen on port 9999
    LOGGER('Starting regresion. Listening on port 9999.')
    server.add_insecure_port('[::]:9999')
    server.start()
    server.wait_for_termination()
