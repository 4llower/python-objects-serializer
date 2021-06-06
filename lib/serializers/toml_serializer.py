import json

from .common_serializer import CommonSerializer
from .utils import serialized, deserialized


class TOMLSerializer(CommonSerializer):
    @serialized
    def dump(self, obj, fp):
        json.dump(obj, fp)
        return

    @serialized
    def dumps(self, obj):
        return json.dumps(obj)

    @deserialized
    def load(self, fp):
        return json.load(fp)

    @deserialized
    def loads(self, s):
        return json.loads(s)
