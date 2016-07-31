from abc import ABCMeta, abstractmethod


class ChainException(Exception):
    """
    Exception for when a chain link could not handle a request.
    """
    pass


class ChainLink(object, metaclass=ABCMeta):
    """
    Abstract ChainLink object as part of the Chain of Responsibility pattern.
    """
    def __init__(self):
        """
        Initialize a new ChainLink instance.
        """
        self.successor = None

    def set_successor(self, successor):
        """
        Set a chain link to call if this chain link fails.

        @param successor: The chain link to call if this chain link fails.
        @type successor: ChainLink
        """
        self.successor = successor

    def successor_handle(self, request):
        """
        Have this chain links successor handle a request.

        @param request: The request to handle.
        """
        try:
            return self.successor.handle(request)
        except AttributeError:
            raise ChainException

    @abstractmethod
    def handle(self, request):
        """
        Handle a request.

        @param request: The request to handle.
        """
        pass


class Chain(object, metaclass=ABCMeta):
    """
    Abstract Chain class as part of the Chain of Responsibility pattern.
    """
    def __init__(self, chainlink):
        """
        Initialize a new Chain instance.

        @param chainlink: The starting chain link.
        """
        self.chainlink = chainlink

    def handle(self, request):
        """
        Handle a request.

        @param request: The request to handle.
        """
        try:
            return self.chainlink.handle(request)
        except ChainException:
            return self.fail()

    @abstractmethod
    def fail(self):
        """
        The method to call when the chain could not handle a request.
        """
        pass