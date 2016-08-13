from abc import ABCMeta, abstractmethod


class Context(object):
    """
    Context class as part of the Interpreter design pattern.
    """
    def __init__(self, in_data):
        self.in_data = in_data
        self.out_data = None


class Expression(object, metaclass=ABCMeta):
    """
    Abstract Expression class as part of the Interpreter design pattern.
    """
    @abstractmethod
    def interpret(self, context):
        """
        Abstract interpret method.

        @param context: The context to interpret.
        @type context: Context
        """
        pass


class NonTerminalExpression(Expression, metaclass=ABCMeta):
    """
    Base class for the NonTerminalExpression class as part of the Interpreter design pattern.
    """
    def __init__(self, **expressions):
        """
        Initialize a new NonTerminalExpression instance.

        @param expressions: A dict of Expressions that are used in this NonTerminalExpressions production.
        @type expressions: dict
        """
        self.expressions = expressions


class TerminalExpression(Expression, metaclass=ABCMeta):
    """
    Base class for the TerminalExpression class as part of the Interpreter design pattern.
    """
    def __init__(self, literal):
        """
        Initialize a new TerminalExpression instance.

        @param literal: A literal representing this TerminalExpression.
        """
        self.literal = literal







