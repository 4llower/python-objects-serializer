from lib import SerializeFactory

serializer = SerializeFactory.create_serializer("JSON")


def hello():
    return 2 + 6


serialized = serializer.dumps(hello)
deserialized = serializer.loads(serialized)
print(deserialized())


