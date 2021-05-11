def deserialized(func):
    def deserialized_wrapper(*args, **kwargs):
        return deserialize(func(*args, **kwargs))

    return deserialized_wrapper


def deserialize(obj):
    return obj
