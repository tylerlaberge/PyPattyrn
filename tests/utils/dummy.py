from types import MethodType


def dummy_class_factory(attributes, functions, base_class=object, meta_class=type):

    class DummyClass(base_class, metaclass=meta_class):
        """
        Class representing dummy data.
        """
        def __init__(self):
            pass

    for key, value in attributes.items():
        if callable(value):
            raise ValueError
        else:
            setattr(DummyClass, key, value)

    for key, value in functions.items():
        if not callable(value):
            raise ValueError
        else:
            setattr(DummyClass, key, MethodType(value, DummyClass))

    return DummyClass
