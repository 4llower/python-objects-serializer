from lib import SerializeFactory

serializer = SerializeFactory.create_serializer("JSON")


def hello():
    return 2 + 6


obj = serializer.dumps({"hello": {"anime": [1, 2, {"anime_object": 3.12312, "animeObject": "123112", "anime": hello}]}})
print(obj)


