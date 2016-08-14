from distutils.core import setup

setup(
    name='pypatterns',
    version='0.1',
    description='Python Design Patterns',
    author='Tyler LaBerge',
    packages=[
        'pypatterns',
        'pypatterns.creational',
        'pypatterns.behavioral',
        'pypatterns.structural'
    ],
)

