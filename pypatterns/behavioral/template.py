from abc import ABCMeta, abstractmethod


class Template(object, metaclass=ABCMeta):
    """
    Abstract Template class as part of the Template design pattern.

    External Template Design Pattern Documentation: U{https://en.wikipedia.org/wiki/Template_method_pattern}
    """
    @abstractmethod
    def go(self):
        """
        Abstract method to call the concrete templates methods.
        """
        pass
