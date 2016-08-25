from abc import ABCMeta, abstractmethod


class Context(object):
    """
    Context class as part of the Interpreter design pattern.

    External Interpreter Pattern documentation: U{https://en.wikipedia.org/wiki/Interpreter_pattern}
    """
    def __init__(self, in_data):
        """
        Initialize a new Context class.

        @param in_data: The starting input of this context.
        """
        self.in_data = in_data
        self.out_data = None


class Expression(object, metaclass=ABCMeta):
    """
    Abstract Expression class as part of the Interpreter design pattern.

    External Interpreter Pattern documentation: U{https://en.wikipedia.org/wiki/Interpreter_pattern}
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

    External Interpreter Pattern documentation: U{https://en.wikipedia.org/wiki/Interpreter_pattern}
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

    External Interpreter Pattern documentation: U{https://en.wikipedia.org/wiki/Interpreter_pattern}
    """
    def __init__(self, literal):
        """
        Initialize a new TerminalExpression instance.

        @param literal: A literal value representing this TerminalExpression.
        """
        self.literal = literal







