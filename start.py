import logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s')
LOGGER = lambda message: logging.getLogger().debug(message + '\n')

DIR = '/regresioncnf/'
ENVS = {
    'MAX_REGRESSION_DEGREE': 100,
}

def generate_tensor_spec():
    # Performance
    p = hyweb_pb2.Tensor.Index()
    p.id = "score"
    p.metadata.tag.extend(["performance"])
    # Number clauses
    c = hyweb_pb2.Tensor.Index()
    c.id = "clauses"
    c.metadata.tag.extend(["number of clauses"])
    # Number of literals
    l = hyweb_pb2.Tensor.Index()
    l.id = "literals"
    l.metadata.tag.extend(["number of literals"])
    # Solver services
    s = hyweb_pb2.Tensor.Index()
    s.id = "solver"
    s.metadata.tag.extend(["SATsolver"])
    with open(DIR + '.service/solver.field', 'rb') as f:
        s.field.ParseFromString(f.read())

    tensor_specification = hyweb_pb2.Tensor()
    tensor_specification.index.extend([c, l, s, p])
    tensor_specification.rank = 3
    return tensor_specification

if __name__ == "__main__":

    import grpc, regresion_pb2, regresion_pb2_grpc, hyweb_pb2, regresion
    from concurrent import futures
    
    # Read __config__ file.
    config = hyweb_pb2.ConfigurationFile()
    config.ParseFromString(
        open('/__config__', 'rb').read()
    )    

    """
    for env_var in config.config.enviroment_variables:
        ENVS[env_var] = type(ENVS[env_var])(
            config.config.enviroment_variables[env_var].value
            )    
    """

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

        def MakeRegresion(self, request, context):
            return regresion.iterate_regression(
                TENSOR_SPECIFICATION = generate_tensor_spec(),
                data_set = request,
                MAX_DEGREE = ENVS['MAX_REGRESSION_DEGREE'],
                LOGGER = LOGGER
            )


    # create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 2)) # One for regresion and the other for stream logs.

    regresion_pb2_grpc.add_RegresionServicer_to_server(
        RegresionServicer(), server)

    # listen on port 9999
    LOGGER('Starting regresion. Listening on port 9999.')
    server.add_insecure_port('[::]:9999')
    server.start()
    server.wait_for_termination()
