class Adapter(object):
    """
    Adapter class as part of the Adapter design pattern.

    - External Usage Documentation: U{https://github.com/tylerlaberge/PyPattyrn#adapter-pattern}
    - External Adapter Pattern Documentation: U{https://en.wikipedia.org/wiki/Adapter_pattern}
    """
    def __init__(self, adaptee, **adapted_methods):
        """
        Initialize a new adapter instance.

        @param adaptee: The object to adapt to a new interface.
        @type adaptee: Object
        @param adapted_methods: A dictionary of methods to adapt.
        @type adapted_methods: dict
        """
        self.__adaptee = adaptee
        self.__dict__.update({k: v for k, v in adapted_methods.items() if callable(v) and
                              getattr(self.__adaptee, v.__name__, None)})

    def __getattr__(self, attr):
        """
        All non-adapted calls are passed to the adaptee.

        @param attr: The attribute to get from the adaptee.
        """
        return getattr(self.__adaptee, attr)

    def original_dict(self):
        """
        Get the adaptee's  __dict__
        """
        return self.__adaptee.__dict__
