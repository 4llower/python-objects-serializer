import pickle

from .common_serializer import CommonSerializer
from .utils import deserialized, serialized


class PICKLESerializer(CommonSerializer):
    @serialized
    def dump(self, obj, fp):
        pickle.dump(obj, fp)
        return

    @serialized
    def dumps(self, obj):
        return pickle.dumps(obj)

    @deserialized
    def load(self, fp):
        return pickle.load(fp)

    @deserialized
    def loads(self, s):
        return pickle.loads(s)
