from setuptools import setup

setup(
    name='python_object_serializer',
    packages=['lib', 'lib/serializers', 'lib/serializers/utils', 'resources', 'lib/serializers/parsers',
              'lib/serializers/parsers/json', 'lib/serializers/parsers/toml', 'lib/serializers/parsers/yaml',
              'lib/serializers/parsers/pickle'],
    version='0.1.0',
    description='Python object serializer',
    author='Me',
    license='MIT',
    install_requires=['toml==0.10.2', 'PyYAML==5.4.1', "coverage==5.5"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests/',
    scripts=['bin/pyos']
)
