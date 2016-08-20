class FlyweightMeta(type):
    """
    Flyweight meta class as part of the Flyweight design pattern.
    """
    def __new__(mcs, name, bases, attrs):
        """
        Override class construction to add 'pool' attribute to classes dict.
        @param name: The name of the class.
        @param bases: Base classes of the class.
        @param attrs: Attributes of the class.
        @return: A new Class.
        """
        attrs['pool'] = dict()
        return super(FlyweightMeta, mcs).__new__(mcs, name, bases, attrs)

    @staticmethod
    def _serialize_params(cls, *args, **kwargs):
        """
        Serialize input parameters to a key.
        Simple implementation is just to serialize it as a string
        """
        args_list = [str(arg) for arg in args]
        args_list.extend([str(kwargs), cls.__name__])
        key = ''.join(args_list)
        return key

    def __call__(cls, *args, **kwargs):
        """
        Override call to use objects from a pool if identical parameters are used for object creation.

        @param args: Arguments for class instantiation.
        @param kwargs: Keyword arguments for class instantiation.
        @return: A new instance of the class.
        """
        key = FlyweightMeta._serialize_params(cls, *args, **kwargs)
        pool = getattr(cls, 'pool', {})

        instance = pool.get(key)
        if not instance:
            instance = super(FlyweightMeta, cls).__call__(*args, **kwargs)
            pool[key] = instance

        return instance
