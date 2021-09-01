import logging
from session import Session
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s')
#LOGGER = lambda message: logging.getLogger().debug(message + '\n')
LOGGER = lambda message: print(message + '\n')

DIR = '' #'/regresioncnf/'
ENVS = {
    'MAX_WORKERS': 5,
    'MAX_REGRESSION_DEGREE': 100,
    'TIME_FOR_EACH_REGRESSION_LOOP': 900,
}

import hashlib
# -- The service use sha3-256 for identify internal objects. --
SHA3_256_ID = bytes.fromhex("a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a")
SHA3_256 = lambda value: "" if value is None else hashlib.sha3_256(value).digest()


if __name__ == "__main__":

    from time import sleep
    import grpc, regresion_pb2, regresion_pb2_grpc
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
      
    _regresion = Session(
        ENVS = ENVS, 
        DIR = DIR, 
        LOGGER = LOGGER, 
        SHA3_256 = SHA3_256
        )

    class RegresionServicer(regresion_pb2_grpc.RegresionServicer):

        def StreamLogs(self, request, context):
            if hasattr(self.StreamLogs, 'has_been_called'): 
                raise Exception('Only can call this method once.')
            else: 
                self.StreamLogs.__func__.has_been_called = True
            with open('app.log') as file:
                while True:
                    try:
                        f = regresion_pb2.File()
                        f.file = next(file)
                        yield f
                    except: pass

        def GetTensor(self, request, context):
            try:
                return _regresion.get_tensor()
            except:
                Exception('Wait more for it, tensor is not ready yet.')
        
        # Hasta que se implemente AddTensor.
        def GetDataSet(self, request, context):
            return _regresion.get_data_set()

        def AddDataSet(self, request, context):
            _regresion.add_data(new_data_set = request)
            return regresion_pb2.Empty()


    # create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=ENVS['MAX_WORKERS']))

    regresion_pb2_grpc.add_RegresionServicer_to_server(
        RegresionServicer(), server)

    # listen on port 9999
    LOGGER('Starting regresion. Listening on port 9999.')
    server.add_insecure_port('[::]:9999')
    server.start()
    server.wait_for_termination()
