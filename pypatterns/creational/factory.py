from abc import abstractmethod, ABCMeta


class Factory(object, metaclass=ABCMeta):
    """
    Factory Interface.

    All Factories should inherit this class and overwrite the create method.
    """
    @abstractmethod
    def create(self, **kwargs):
        """
        Abstract create method.

        Concrete implementations should return a new instance of the object the factory class is responsible for.
        @param kwargs: Arguments for object creation.
        @return: A new instance of the object the factory is responsible for.
        """
        pass


class AbstractFactory(object):
    """
    Abstract Factory Class.
    """
    def __init__(self):
        """
        Initialize the abstract factory.

        Concrete implementations should call this from within their own __init__ method
        and register all their factories to keys using the register method.
        """
        self._factories = dict()

    @abstractmethod
    def create(self, **kwargs):
        """
        Abstract create method.

        Concrete implementations should return a new instance of an object by calling the appropriate factory.

        @param kwargs: Arguments for object creation.
        """
        pass

    def _register(self, key, factory):
        """
        Register a factory to a key.

        @param key: Key for identifying which factory to use.
        @type key: str
        @param factory: The factory to register to the key.
        """
        self._factories[str(key)] = factory()
