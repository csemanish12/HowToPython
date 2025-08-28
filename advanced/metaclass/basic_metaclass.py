class LoggingMeta(type):
    def __new__(mcls, name, bases, ns):
        print(f"[LoggingMeta] Create {name} with attrs: {list(ns.items())}]")
        return super().__new__(mcls,name, bases, ns)



class Example(metaclass=LoggingMeta):
    x = 42

    def greet(self): return "hi"

