class Singleton(type):
    _instances = {}

    def __call__(cls, ENVS, DIR, LOGGER, SHA3_256):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(ENVS, DIR, LOGGER, SHA3_256)
        return cls._instances[cls]