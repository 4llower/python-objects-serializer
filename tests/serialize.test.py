from lib import SerializeFactory

serializer = SerializeFactory.create_serializer("JSON")
obj = serializer.dumps({"hello": 228})
print(obj)
