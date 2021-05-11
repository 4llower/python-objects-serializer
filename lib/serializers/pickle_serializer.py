from .common_serializer import CommonSerializer
import pickle


class PICKLESerializer(CommonSerializer):
    def dump(self, obj, fp):
        pickle.dump(obj, fp)
        return

    def dumps(self, obj):
        return pickle.dumps(obj)

    def load(self, fp):
        return pickle.load(fp)

    def loads(self, s):
        return pickle.loads(s)
