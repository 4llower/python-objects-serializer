# from lib import SerializeFactory

# serializer = SerializeFactory.create_serializer("JSON")
# obj = serializer.dumps({"hello": 228})
# print(obj)

d = 228


def func(a, b):
    c = a + b
    return c + d


code = func.__code__
globals = func.__globals__
