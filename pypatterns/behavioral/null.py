class Null(object):
    """
    A class for implementing Null objects.

    This class ignores all parameters passed when constructing or
    calling instances and traps all attribute and method requests.
    Instances of it always (and reliably) do 'nothing'.

    The code might benefit from implementing some further special
    Python methods depending on the context in which its instances
    are used. Especially when comparing and coercing Null objects
    the respective methods' implementation will depend very much
    on the environment and, hence, these special methods are not
    provided here.

    Dinu C. Gherman,
    August 2001
    http://code.activestate.com/recipes/68205-null-object-design-pattern/
    """

    # object constructing

    def __init__(self, *args, **kwargs):
        """
        Ignore parameters.
        """
        pass

    # object calling

    def __call__(self, *args, **kwargs):
        """
        Ignore method calls.
        """
        return self

    # attribute handling

    def __getattr__(self, mname):
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

    # misc.

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
