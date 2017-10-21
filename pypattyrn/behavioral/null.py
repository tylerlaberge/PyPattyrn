class Null(object):
    """
    A Null object class as part of the Null object design pattern.

    - External Usage documentation: U{https://github.com/tylerlaberge/PyPattyrn#null-object-pattern}
    - External Null Object Pattern documentation: U{https://en.wikipedia.org/wiki/Null_Object_pattern}
    """
    def __init__(self, *args, **kwargs):
        """
        Do nothing.
        """
        pass

    def __call__(self, *args, **kwargs):
        """
        Do nothing.

        @return: This object instance.
        @rtype: Null
        """
        return self

    def __getattr__(self, name):
        """
        Do nothing.

        @return: This object instance.
        @rtype: Null
        """
        return self

    def __setattr__(self, name, value):
        """
        Do nothing.

        @return: This object instance.
        @rtype: Null
        """
        return self

    def __delattr__(self, name):
        """
        Do nothing.

        @return: This object instance.
        @rtype: Null
        """
        return self

    def __repr__(self):
        """
        Null object string representation is the empty string.

        @return: An empty string.
        @rtype: String
        """
        return ''

    def __str__(self):
        """
        Null object string representation is the empty string.

        @return: An empty string.
        @rtype: String
        """
        return ''

    def __bool__(self):
        """
        Null object evaluates to False.

        @return: False.
        @rtype: Boolean
        """
        return False
