from types import FunctionType

from .types import rude_types, object_types


def serialized(func):
    def serialized_wrapper(*args, **kwargs):
        if bool(kwargs):
            if kwargs.get('obj') is None:
                raise TypeError('[@serialized] obj doesn\'t exists in kwargs')
            kwargs['obj'] = serialize(kwargs.get('obj'))
        if bool(args):
            if not type(args[1]) is dict and not type(args[1]) is func:
                raise TypeError('[@serialized] first argument(exclude self) is\'t available to serialize')
        return func(*[args[0], serialize(args[1]), *(args[2:])], **kwargs)

    return serialized_wrapper


def serialize(obj):
    result = {}

    if obj is None:
        return {"None": None}

    elif not rude_types.get(type(obj).__name__) is None:
        return {type(obj).__name__: obj}

    elif type(obj).__name__ == 'dict':
        serialized_dict = {}
        for key in obj:
            serialized_dict['item%i' % len(serialized_dict)] = {"key": serialize(key), "value": serialize(obj[key])}
        result = {type(obj).__name__: serialized_dict}

    elif not object_types.get(type(obj).__name__) is None:
        serialized_iterable = []
        for key in obj:
            serialized_iterable.append(serialize(key))
        result = {type(obj).__name__: serialized_iterable}

    elif type(obj) == FunctionType:
        result = {type(obj).__name__: obj}

    return result
