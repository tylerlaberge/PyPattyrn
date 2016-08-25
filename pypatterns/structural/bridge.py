from abc import ABCMeta


class Bridge(object, metaclass=ABCMeta):
    """
    Base Bridge class as part of the Bridge design pattern.

    External Bridge Pattern documentation: U{https://en.wikipedia.org/wiki/Bridge_pattern}
    """
    def __init__(self, implementor):
        """
        Initialize a new Bridge instance.

        @param implementor: The implementor that concrete classes should call upon to do some action.
        """
        self.implementor = implementor

