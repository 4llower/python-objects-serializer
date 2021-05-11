def serialized(func):
    def serialized_wrapper(*args, **kwargs):
        if bool(kwargs):
            if kwargs.get('obj') is None:
                raise TypeError('[@serialized] obj doesn\'t exists in kwargs')
            kwargs['obj'] = serialize(kwargs.get('obj'))
        if bool(args):
            if not type(args[1]) is dict:
                raise TypeError('[@serialized] first argument(exclude self) is\'t available to serialize')
        return func(*[args[0], serialize(args[1]), *(args[2:])], **kwargs)

    return serialized_wrapper


def serialize(obj):
    obj["hello1"] = 222
    return obj
