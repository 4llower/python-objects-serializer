from .common_serializer import CommonSerializer
from .utils import deserialized, serialized


class YAMLSerializer(CommonSerializer):
    def dump(self, obj, fp):
        pass

    @serialized
    def dumps(self, obj):
        pass

    def load(self, fp):
        pass

    @deserialized
    def loads(self, s):
        pass
