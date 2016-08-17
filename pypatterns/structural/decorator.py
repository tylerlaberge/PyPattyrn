from functools import partial
from abc import ABCMeta, abstractmethod


class Decorator(object, metaclass=ABCMeta):

    def __get__(self, instance, owner):
        return partial(self.__call__, instance)

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass


class DecoratorSimple(Decorator, metaclass=ABCMeta):

    def __init__(self, func):
        self.func = func


class DecoratorArgs(Decorator, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass


class Wrap(DecoratorSimple):

    def __call__(self, instance, func, *args, **kwargs):
        return lambda: self.func(instance, func, *args, **kwargs)