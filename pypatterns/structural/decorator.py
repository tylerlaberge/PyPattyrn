from functools import partial
from abc import ABCMeta, abstractmethod


class Decorator(object, metaclass=ABCMeta):
    """
    Base Decorator class that all decorator classes inherit from.
    """
    def __get__(self, instance, owner):
        """
        Override __get__ in order to get the instance of a bound of method call.
        """
        return partial(self.__call__, instance)

    @abstractmethod
    def __call__(self, *args, **kwargs):
        """
        All decorators must implement a __call__ method.
        """
        pass


class DecoratorSimple(Decorator, metaclass=ABCMeta):
    """
    A Base Decorator class for decorators with no arguments.
    """
    def __init__(self, func):
        """
        Initialize a new DecoratorSimple instance.

        @param func: The function being decorated.
        """
        self.func = func


class DecoratorComplex(Decorator, metaclass=ABCMeta):
    """
    A Base Decorator class for decorators with arguments.
    """
    @abstractmethod
    def __init__(self, *args, **kwargs):
        """
        Initialize a new DecoratorComplex instance.

        @param args: Args for the decorator.
        @param kwargs: Keyword args for the decorator.
        """
        pass

    @abstractmethod
    def __call__(self, func, *args, **kwargs):
        """
        Concrete DecoratorComplex instances must override the __call__ method.

        @param func: The function being decorated.
        @param args: Arguments for the decorated function.
        @param kwargs: Keyword arguments for the decorated function.
        @return:
        """
        pass


class CallWrapper(DecoratorSimple):
    """
    A Decorator for wrapping DecoratorComplex __call__ methods.
    """
    def __call__(self, instance, func):
        """
        Wrap a concrete DecoratorComplex __call__ method.
        """
        def wrapped(*args, **kwargs):
            return self.func(instance, func, *args, **kwargs)

        return wrapped
