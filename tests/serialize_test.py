from lib import SerializeFactory


def test__serialization_funcs_1():
    serializer = SerializeFactory.create_serializer("JSON")

    def func(x):
        return x + 100

    serialized = serializer.dumps(func)
    deserialized = serializer.loads(serialized)
    supposed = [200, -200, 0]
    real = [deserialized(100), deserialized(-300), deserialized(-100)]

    for i in range(len(supposed)):
        assert supposed[i] == real[i]


def test__serialization_funcs_2():
    serializer = SerializeFactory.create_serializer("JSON")

    a = lambda x: -x if x > 100 else x

    serialized = serializer.dumps(a)
    deserialized = serializer.loads(serialized)

    inputs = [101, -5, 100]
    supposed = [-101, -5, 100]

    for i in range(len(inputs)):
        result = deserialized(inputs[i])
        assert result == supposed[i]
