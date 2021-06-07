from .common_serializer import CommonSerializer
from .utils import deserialized, serialized
from .parsers.json import dumps, loads, dump, load


class JSONSerializer(CommonSerializer):
    def dump(self, obj, fp):
        dump(obj, fp)
        return

    @serialized
    def dumps(self, obj):
        return dumps(obj)

    def load(self, fp):
        return load(fp)

    @deserialized
    def loads(self, s):
        return loads(s)
