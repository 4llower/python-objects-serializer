from setuptools import setup

setup(
    name='my_serializer',
    packages=['lib', 'resources'],
    version='0.1.0',
    description='Python object serializer',
    author='Me',
    license='MIT',
    install_requires=['toml==0.10.2', 'PyYAML==5.4.1', "coverage==5.5"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests/',
    scripts=['convert']
)