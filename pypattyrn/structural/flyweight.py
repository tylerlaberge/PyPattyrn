class FlyweightMeta(type):
    """
    Flyweight meta class as part of the Flyweight design pattern.

    - External Usage Documentation: U{https://github.com/tylerlaberge/PyPattyrn#flyweight-pattern}
    - External Flyweight Pattern documentation: U{https://en.wikipedia.org/wiki/Flyweight_pattern}
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
    def _serialize(cls, *args, **kwargs):
        """
        Serialize arguments to a string representation.
        """
        serialized_args = [str(arg) for arg in args]
        serialized_kwargs = [str(kwargs), cls.__name__]

        serialized_args.extend(serialized_kwargs)

        return ''.join(serialized_args)

    def __call__(cls, *args, **kwargs):
        """
        Override call to use objects from a pool if identical parameters are used for object creation.

        @param args: Arguments for class instantiation.
        @param kwargs: Keyword arguments for class instantiation.
        @return: A new instance of the class.
        """
        key = FlyweightMeta._serialize(cls, *args, **kwargs)
        pool = getattr(cls, 'pool', {})

        instance = pool.get(key)
        if not instance:
            instance = super(FlyweightMeta, cls).__call__(*args, **kwargs)
            pool[key] = instance

        return instance
