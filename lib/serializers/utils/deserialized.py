from types import FunctionType, CodeType

from .types import object_types, rude_types


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
        elif len(obj) == 1 and 'function' in obj:
            return dict_to_function(deserialize(obj["function"]))
        else:
            for key, value in obj.items():
                if key == "None":
                    return None
                types = {**rude_types, **object_types}
                return types[key](deserialize(value))

    elif type(obj).__name__ in object_types:
        response = []
        for item in obj:
            response.append(deserialize(item))

    if response is None:
        return str(obj)
    else:
        return response


def dict_to_function(obj):
    is_recursive = False
    function_globals = obj['__globals__']

    for name, out_obj in function_globals.items():
        if name == obj['__name__']:
            is_recursive = True
        function_globals[name] = deserialize(out_obj)
    function_globals['__builtins__'] = __builtins__

    code = obj['__code__']
    for i in range(len(code)):
        if i == 13 and code[i] is None:
            code[i] = b''
        if code[i] is None:
            code[i] = ()
        elif isinstance(code[i], list):
            code[i] = bytes(code[i])

    func = FunctionType(CodeType(*code), function_globals, obj['__name__'], obj['__defaults__'], None)

    if is_recursive:
        func.__getattribute__('__globals__')[obj['__name__']] = func

    return func
