from .serializers import JSONSerializer
from .serializers import PICKLESerializer
from .serializers import TOMLSerializer
from .serializers import YAMLSerializer
from enum import Enum


class AvailableSerializers(Enum):
    json = "JSON"
    pickle = "PICKLE"
    toml = "TOML"
    yaml = "YAML"


class SerializeFactory:
    @staticmethod
    def validate_covers_all_available_serializers(serializer_type_to_serializer_object):
        for value in [e.value for e in AvailableSerializers]:
            if serializer_type_to_serializer_object.get(value) is None:
                raise TypeError("%s serializer doesn't exists in factory, but added to AvailableSerializers" % value)

    @classmethod
    def create_serializer(cls, serializer_type):
        """
        Fabric method which create serializer with depends from object type
        :param serializer_type: string such as JSON | YAML | PICKLE | TOML
        :return: serializer which has methods from common_serializer
        """
        serializer_type_to_serializer_object = {AvailableSerializers.json.value: JSONSerializer(),
                                                AvailableSerializers.pickle.value: PICKLESerializer(),
                                                AvailableSerializers.toml.value: TOMLSerializer(),
                                                AvailableSerializers.yaml.value: YAMLSerializer()}

        cls.validate_covers_all_available_serializers(serializer_type_to_serializer_object)

        if not serializer_type_to_serializer_object.get(serializer_type):
            raise ValueError("%s serializer doesn't support" % serializer_type)

        return serializer_type_to_serializer_object[serializer_type]

