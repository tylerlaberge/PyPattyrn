from distutils.core import setup

setup(
    name='pypat',
    version='0.1',
    description='Python Design Patterns',
    author='Tyler LaBerge',
    packages=[
        'pypat',
        'pypat.creational',
        'pypat.behavioral',
        'pypat.structural'
    ],
)

