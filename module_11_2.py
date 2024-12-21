import inspect

def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    obj_module = obj.__module__
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }
    return info

class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        return f'Value is: {self.value}'

    def increment(self):
        self.value += 1


my_obj = MyClass(10)
obj_info = introspection_info(my_obj)
print(obj_info)