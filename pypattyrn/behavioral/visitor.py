from abc import ABCMeta, abstractmethod


class Visitor(metaclass=ABCMeta):
    """
    Abstract Visitor class as part of the Visitor Design Pattern.

    - External Usage documentation: U{https://github.com/tylerlaberge/PyPattyrn#visitor-pattern}
    - External Visitor Design Pattern documentation: U{https://en.wikipedia.org/wiki/Visitor_pattern}
    """
    def visit(self, node, *args, **kwargs):
        """
        Visit the visitor with some object.

        @param node: An object to call a visitor method with.
        @param args: Arguments to go with the visitor method call.
        @param kwargs: Keyword arguments to go with the visitor method call.
        @return: The return value of the method that was called for visiting object.
        """
        method = None
        for cls in node.__class__.__mro__:
            method_name = 'visit_' + cls.__name__.lower()
            method = getattr(self, method_name, None)
            if method:
                break

        if not method:
            method = self.generic_visit
        return method(node, *args, **kwargs)

    @abstractmethod
    def generic_visit(self, node, *args, **kwargs):
        """
        The method to call if no methods were found for a visiting object.

        @param node: An object to call a visitor method with.
        @param args: Arguments to go with the visitor method call.
        @param kwargs: Keyword arguments to go with the visitor method call.
        """


class Visitee(object):
    """
    A base class for objects that wish to be able to be visited by a Visitor class.

    - External Usage documentation: U{https://github.com/tylerlaberge/PyPattyrn#behavioral-patterns}
    - External Visitor Design Pattern documentation: U{https://en.wikipedia.org/wiki/Visitor_pattern}
    """
    def accept(self, visitor, *args, **kwargs):
        """
        Have a visitor visit this class instance.

        @param visitor: The visitor to visit.
        @type visitor: Visitor
        @param args: Any args to send with the visit.
        @param kwargs: Any kwargs to send with the visit.
        """
        return visitor.visit(self, *args, **kwargs)
