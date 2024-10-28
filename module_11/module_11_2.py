import inspect

def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    obj_module = getattr(obj, '__module__', 'builtins' if obj_type in ['int', 'str', 'float', 'list', 'dict', 'set', 'tuple'] else None)

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }

    return info

# Пример использования
number_info = introspection_info(42)
print(number_info)
