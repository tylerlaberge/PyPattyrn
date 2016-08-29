from abc import ABCMeta, abstractmethod


class Strategy(object, metaclass=ABCMeta):
    """
    An abstract Strategy class.
    All strategies should inherit this class.

    External Strategy Pattern documentation: U{https://en.wikipedia.org/wiki/Strategy_pattern}
    """

    @abstractmethod
    def __call__(self, *args, **kwargs):
        """
        Abstract method that must be overridden.
        The overridden method should execute the classes strategy.
        """
        pass
