import toml

from .common_serializer import CommonSerializer
from .utils import serialized, deserialized


class TOMLSerializer(CommonSerializer):
    def dump(self, obj, fp):
        toml.dump(obj, fp)
        return

    @serialized
    def dumps(self, obj):
        return toml.dumps(obj)

    def load(self, fp):
        return toml.load(fp)

    @deserialized
    def loads(self, s):
        return toml.loads(s)
