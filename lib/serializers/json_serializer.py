import json

from .common_serializer import CommonSerializer
from .utils import deserialized, serialized


class JSONSerializer(CommonSerializer):
    @serialized
    def dump(self, obj, fp):
        return json.dump(obj, fp)

    @serialized
    def dumps(self, obj):
        return json.dumps(obj)

    @deserialized
    def load(self, fp):
        return json.load(fp)

    @deserialized
    def loads(self, s):
        return json.loads(s)
