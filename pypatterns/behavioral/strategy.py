from abc import ABCMeta, abstractmethod


class Strategy(object):
    """
    An abstract Strategy class.
    All strategies should inherit this class.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __call__(self, *args, **kwargs):
        """
        Abstract method that must be overridden.
        The overridden method should execute the classes strategy.
        """
        pass
