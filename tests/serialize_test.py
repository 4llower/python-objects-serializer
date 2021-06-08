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


def fib(x):
    if x < 2:
        return 1
    else:
        return fib(x - 2) + fib(x - 1)


def test__serialization_funcs_3():
    serializer = SerializeFactory.create_serializer("JSON")

    serialized = serializer.dumps(fib)
    deserialized = serializer.loads(serialized)

    supposed = [fib(i) for i in range(10)]
    real = [deserialized(i) for i in range(10)]

    for i in range(len(supposed)):
        assert supposed[i] == real[i]


def get_max(a, b):
    return max(a, b)


def test__serialization_funcs_4():
    serializer = SerializeFactory.create_serializer("PICKLE")

    serialized = serializer.dumps(get_max)
    deserialized = serializer.loads(serialized)

    inputs = [[1, 2], [10, 20], [90, 1], [-1, 20], [-20, -40]]
    supposed = [2, 20, 90, 20, -20]

    for i in range(len(inputs)):
        result = deserialized(inputs[i][0], inputs[i][1])
        assert result == supposed[i]


context = 42


def context_global():
    global context
    context += 1
    return context


def test__serialization_funcs_5():
    serializer = SerializeFactory.create_serializer("JSON")

    serialized = serializer.dumps(context_global)
    deserialized = serializer.loads(serialized)

    supposed = [43, 44, 45, 46]

    for i in range(len(supposed)):
        result = deserialized()
        assert result == supposed[i]
