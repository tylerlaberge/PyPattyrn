from abc import abstractmethod, ABCMeta


class Factory(object, metaclass=ABCMeta):
    """
    Abstract Factory Class.

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

