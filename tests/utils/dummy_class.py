from types import MethodType


def dummy_factory(base_class, attributes, functions):

    class DummyClass(base_class):
        """
        Class representing dummy data.
        """
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