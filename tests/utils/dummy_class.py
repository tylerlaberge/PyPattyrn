from types import MethodType


class DummyClass(object):
    """
    Class representing dummy data.
    """
    def __init__(self, attributes, functions):
        """
        Initialize a new DummyClass instance.

        @param attributes: A dictionary of instance variables for this dummy instance.
        @type attributes: dict
        @param functions: A dictionary of functions for this dummy instance.
        @type functions: dict
        """
        for key, value in attributes.items():
            if callable(value):
                raise ValueError
            else:
                setattr(self, key, value)

        for key, value in functions.items():
            if not callable(value):
                raise ValueError
            else:
                setattr(self, key, MethodType(value, self))
