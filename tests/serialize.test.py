from lib.factory import SerializeFactory

serializer = SerializeFactory.create_serializer("JSON")

print(serializer)