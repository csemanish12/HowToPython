class RequiredConfigMeta(type):
    def __new__(mcls, name, bases, ns):
        if 'CONFIG' not in ns:
            raise TypeError(f"{name} must define a CONFIG attribute")
        
        return super().__new__(mcls, name, bases, ns)


class Good(metaclass=RequiredConfigMeta):
    CONFIG = {"env": "prod"}


class Bad(metaclass=RequiredConfigMeta):
    pass