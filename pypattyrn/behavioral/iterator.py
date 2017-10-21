from abc import ABCMeta, abstractmethod


class Iterator(object):
    """
    An Iterator class for the Iterator design pattern.

    - External Usage documentation: U{https://github.com/tylerlaberge/PyPattyrn#iterator-pattern}
    - External Iterator Pattern documentation: U{https://en.wikipedia.org/wiki/Iterator_pattern}
    """
    def __init__(self, iterable):
        """
        Initialize a new Iterator instance.

        @param iterable: An Iterable object to iterate over.
        @type iterable: Iterable
        """
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        return self.iterable.__next__()


class Iterable(object, metaclass=ABCMeta):
    """
    An abstract class representing an Iterable object as part of the Iterator design pattern.

    - External Usage documentation: U{https://github.com/tylerlaberge/PyPattyrn#iterator-pattern}
    - External Iterator Pattern documentation: U{https://en.wikipedia.org/wiki/Iterator_pattern}
    """
    @abstractmethod
    def __next__(self):
        """
        All Iterable's must implement a __next__ method which eventually raises StopIteration.
        """
        pass
