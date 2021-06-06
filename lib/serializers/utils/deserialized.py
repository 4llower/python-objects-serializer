from types import FunctionType, CodeType

from .types import object_types


def deserialized(func):
    def deserialized_wrapper(*args, **kwargs):
        return deserialize(func(*args, **kwargs))

    return deserialized_wrapper


def deserialize(obj):
    response = None
    if type(obj).__name__ == 'dict':
        if len(obj) == 1 and 'dict' in obj:
            response = {}
            for key, item in obj['dict'].items():
                response[deserialize(item['key'])] = deserialize(item['value'])
        elif len(obj) == 1 and 'func' in obj:
            return dict_to_function(deserialize(obj["func"]))
        else:
            for key, value in obj.items():
                if key is None:
                    response = None
                else:
                    response = object_types[key](deserialize(value))
                    # ????
                return response
    if type(obj).__name__ in object_types:
        response = []
        for item in obj:
            response.append(deserialize(item))

    if response is None:
        return str(obj)
    else:
        return response


def dict_to_function(obj):
    recursive_flag = False
    obj_globals = obj['__globals__']

    for outer_obj_name, outer_obj in obj_globals.items():
        if outer_obj_name == obj['__name__']:
            recursive_flag = True
        obj_globals[outer_obj_name] = deserialize(outer_obj)
    obj_globals['__builtins__'] = __builtins__

    code = obj['__code__']

    for i in range(len(code)):
        if i == 13 and code[i] is None:
            code[i] = b''
        if code[i] is None:
            code[i] = ()
        elif isinstance(code[i], list):
            code[i] = bytes(code[i])
    func = FunctionType(CodeType(*code), obj_globals, obj['__name__'], obj['__defaults__'], None)

    if recursive_flag:
        func.__getattribute__('__globals__')[obj['__name__']] = func
    return func
