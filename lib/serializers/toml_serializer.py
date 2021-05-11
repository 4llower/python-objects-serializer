from .common_serializer import CommonSerializer
import json


class TOMLSerializer(CommonSerializer):
    def dump(self, obj, fp):
        json.dump(obj, fp)
        return

    def dumps(self, obj):
        return json.dumps(obj)

    def load(self, fp):
        return json.load(fp)

    def loads(self, s):
        return json.loads(s)
