from abc import ABCMeta
from copy import deepcopy
from pypattyrn.behavioral.memento import Originator


class Reusable(Originator, metaclass=ABCMeta):
    """
    An abstract reusable class.

    - External Usage documentation: U{https://github.com/tylerlaberge/PyPattyrn#object-pool-pattern}
    - External Object Pool Pattern documentation: U{https://en.wikipedia.org/wiki/Object_pool_pattern}
    """
    def __init__(self):
        """
        Initialize a new Reusable instance.
        """
        self.memento = self.commit()

    def reset(self):
        """
        Reset this objects state to the state that it was created with.
        """
        memento = self.memento
        self.rollback(deepcopy(memento))
        self.memento = memento


class Pool(object):
    """
    An Object Pool design pattern implementation.

    - External Usage documentation: U{https://github.com/tylerlaberge/PyPatterns/wiki/Creational-Pattern-Usage}
    - External Object Pool Pattern documentation: U{https://en.wikipedia.org/wiki/Object_pool_pattern}
    """
    def __init__(self, reusable_class, *args, **kwargs):
        """
        Initialize a new object pool instance.

        @param reusable_class: The reusable class this object pool is responsible for.
        @param args: args for reusable object creation.
        @param kwargs: kwargs for reusable object creation.
        """
        self.reusables = list()
        self.reusable_class = reusable_class
        self.args = args
        self.kwargs = kwargs
        self.pool_size = 2
        self._expand(self.pool_size)

    def acquire(self):
        """
        Acquire an object from the pool.

        @return: An object from the pool.
        """
        try:
            reusable = self.reusables.pop()
        except IndexError:
            self._expand(self.pool_size)
            reusable = self.reusables.pop()

        return reusable

    def release(self, reusable):
        """
        Release an object back into the pool.

        @param reusable: The object to return to the pool.
        """
        reusable.reset()
        self.reusables.append(reusable)

    def _expand(self, size):
        for i in range(0, size):
            self.reusables.append(self.reusable_class(*self.args, **self.kwargs))
