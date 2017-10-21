from abc import ABCMeta, abstractmethod


class Observer(object, metaclass=ABCMeta):
    """
    Abstract Observer class as part of the Observer design pattern.

    - External Usage documentation: U{https://github.com/tylerlaberge/PyPattyrn#observer-pattern}
    - External Observer Pattern documentation: U{https://en.wikipedia.org/wiki/Observer_pattern}
    """
    @abstractmethod
    def update(self, **state):
        """
        Abstract method that is called when an Observable's state changes.
        """
        pass


class Observable(object):
    """
    Base Observable class as part of the Observer design pattern.

    - External Usage documentation: U{https://github.com/tylerlaberge/PyPattyrn#observer-pattern}
    - External Observer Pattern documentation: U{https://en.wikipedia.org/wiki/Observer_pattern}
    """
    def __init__(self):
        """
        Initialize a new Observable instance.
        """
        self._observers = set()

    def attach(self, observer):
        """
        Attach an observer to this Observable.

        @param observer: The Observer to attach.
        @type observer: Observer
        """
        self._observers.add(observer)

    def detach(self, observer):
        """
        Detach an observer from this Observable.

        @param observer: The Observer to detach.
        @type observer: Observer
        """
        try:
            self._observers.remove(observer)
        except KeyError:
            pass

    def notify(self):
        """
        Notify all attached Observers of the state of this Observable.
        """
        for observer in self._observers:
            state = {k: v for k, v in self.__dict__.items() if not k.startswith('__') and not k.startswith('_')}
            observer.update(**state)

