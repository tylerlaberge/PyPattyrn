class Null(object):
    """
    A Null object class as part of the Null object design pattern.

    External Null Object Pattern documentation: U{https://en.wikipedia.org/wiki/Null_Object_pattern}
    """
    def __init__(self, *args, **kwargs):
        """
        Ignore parameters.
        """
        pass

    def __call__(self, *args, **kwargs):
        """
        Ignore method calls.
        """
        return self

    def __getattr__(self, name):
        """
        Ignore attribute requests.
        """
        return self

    def __setattr__(self, name, value):
        """
        Ignore attribute setting.
        """
        return self

    def __delattr__(self, name):
        """
        Ignore deleting attributes.
        """
        return self

    def __repr__(self):
        """
        Return a string representation.
        """
        return ''

    def __str__(self):
        """
        Convert to a string and return it.
        """
        return ''

    def __bool__(self):
        """
        Boolean of Null object is always False.
        """
        return False
