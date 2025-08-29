class PluginMeta(type):
    registry = {}

    def __new__(mcls, name, bases, ns):
        
        cls = super().__new__(mcls, name, bases, ns)
        if name != "PluginBase":
            PluginMeta.registry[name] = cls
        
        return cls
    

class PluginBase(metaclass=PluginMeta):
    pass

class CSVPlugin(PluginBase):
    pass

class JSONPlugin(PluginBase):
    pass

print("plugin registry:", PluginMeta.registry)