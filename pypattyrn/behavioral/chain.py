from abc import ABCMeta, abstractmethod


class ChainLink(object, metaclass=ABCMeta):
    """
    Abstract ChainLink object as part of the Chain of Responsibility pattern.

    - External Usage documentation: U{https://github.com/tylerlaberge/PyPattyrn#chain-of-responsibility-pattern}
    - External Chain of Responsibility Pattern documentation: U{https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern}
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
        return self.successor.handle(request)

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

    - External Usage documentation: U{https://github.com/tylerlaberge/PyPattyrn#chain-of-responsibility-pattern}
    - External Chain of Responsibility Pattern documentation: U{https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern}
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
        except AttributeError:
            return self.fail()

    @abstractmethod
    def fail(self):
        """
        The method to call when the chain could not handle a request.
        """
        pass
