"""
Prepare lets you choose the mapping used for the class body. eg to capture definition order or to transform
names as they are added
"""

from collections import OrderedDict


class AutoPrefixNamespace(dict):
    """
    Automatically adds prefix to non - magic attributes
    """

    def __setitem__(self, key, value):
        if not key.startswith('__'):
            key = f"api_{key}"
            print(f"Transformed:{key}")

        super().__setitem__(key, value)

class APIMeta(type):
    @classmethod
    def __prepare__(mcls, name, bases, **kwargs):
        return AutoPrefixNamespace()
    
class UserService(metaclass=APIMeta):
    version = "1.0"
    host = "localhost"

    def get_user(self):
        return "user data"


print(dir(UserService))