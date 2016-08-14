from abc import ABCMeta, abstractmethod
from unittest import TestCase
from pypatterns.behavioral.interpreter import Context, Expression, NonTerminalExpression, TerminalExpression


class ContextTestCase(TestCase):
    """
    Unit testing class for the Context class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        self.context = Context('foo')

    def test_in_data(self):
        """
        Test the in data attribute.

        @raise AssertionError: If the test fails.
        """
        self.assertEquals('foo', self.context.in_data)

        try:
            self.context.in_data = 'bar'
        except AttributeError:
            raise AssertionError
        else:
            self.assertEquals('bar', self.context.in_data)

    def test_out_data(self):
        """
        Test the out data attribute.

        @raise AssertionError: If the test fails.
        """
        try:
            self.context.out_data = 'bar'
        except AttributeError:
            raise AssertionError
        else:
            self.assertEquals('bar', self.context.out_data)


class ExpressionTestCase(TestCase):
    """
    Unit testing class for the Expression class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class ConcreteExpression(Expression):

            def interpret(self, context):
                context.out_data = str(context.in_data).upper()

        self.concrete_expression = ConcreteExpression()
        self.context = Context('foo')

    def test_interpret(self):
        """
        Test the interpret method.

        @raise AssertionError: If the test fails.
        """
        self.concrete_expression.interpret(self.context)

        self.assertEquals('FOO', self.context.out_data)


class TerminalExpressionTestCase(TestCase):
    """
    Unit testing class for the TerminalExpression class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class ConcreteTerminal(TerminalExpression):

            def interpret(self, context):
                return self.literal

        self.concrete_terminal_class = ConcreteTerminal

    def test_init(self):
        """
        Test the __init__ method.

        @raise AssertionError: If the test fails.
        """
        terminal = self.concrete_terminal_class('foo')
        self.assertEquals('foo', terminal.literal)

    def test_interpret(self):
        """
        Test the interpret method.

        @raise AssertionError: If the test fails.
        """
        terminal = self.concrete_terminal_class('bar')
        self.assertEquals('bar', terminal.interpret(Context('')))


class NonTerminalExpressionTestCase(TestCase):
    """
    Unit testing class for the NonTerminalExpression class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class RomanTerminalExpression(TerminalExpression, metaclass=ABCMeta):
            
            def interpret(self, context):
                return self.literal
            
        class RomanNonTerminalExpression(NonTerminalExpression, metaclass=ABCMeta):

            def interpret(self, context):

                if context.out_data is None:
                    context.out_data = 0
                    
                if len(context.in_data) == 0:
                    return

                if context.in_data.startswith(self.nine()):
                    context.out_data += 9 * self.multiplier()
                    context.in_data = context.in_data[2:]

                elif context.in_data.startswith(self.four()):
                    context.out_data += 4 * self.multiplier()
                    context.in_data = context.in_data[2:]

                elif context.in_data.startswith(self.five()):
                    context.out_data += 5 * self.multiplier()
                    context.in_data = context.in_data[1:]

                while context.in_data.startswith(self.one()):
                    context.out_data += 1 * self.multiplier()
                    context.in_data = context.in_data[1:]

            def one(self):
                return self.expressions['one'].interpret(None)

            def four(self):
                return self.expressions['four'].interpret(None)

            def five(self):
                return self.expressions['five'].interpret(None)

            def nine(self):
                return self.expressions['nine'].interpret(None)
            
            @abstractmethod
            def multiplier(self):
                pass

        class ThousandExpression(RomanNonTerminalExpression):

            def __init__(self):
                one_terminal = RomanTerminalExpression('M')
                four_terminal = RomanTerminalExpression(' ')
                five_terminal = RomanTerminalExpression(' ')
                nine_terminal = RomanTerminalExpression(' ')
           
                super().__init__(one=one_terminal, four=four_terminal, five=five_terminal, nine=nine_terminal)
            
            def multiplier(self):
                return 1000

        class HundredExpression(RomanNonTerminalExpression):
            
            def __init__(self):                
                one_terminal = RomanTerminalExpression('C')
                four_terminal = RomanTerminalExpression('CD')
                five_terminal = RomanTerminalExpression('D')
                nine_terminal = RomanTerminalExpression('CM')
                
                super().__init__(one=one_terminal, four=four_terminal, five=five_terminal, nine=nine_terminal)
            
            def multiplier(self):
                return 100

        class TenExpression(RomanNonTerminalExpression):

            def __init__(self):
                one_terminal = RomanTerminalExpression('X')
                four_terminal = RomanTerminalExpression('XL')
                five_terminal = RomanTerminalExpression('L')
                nine_terminal = RomanTerminalExpression('XC')

                super().__init__(one=one_terminal, four=four_terminal, five=five_terminal, nine=nine_terminal)
            
            def multiplier(self):
                return 10

        class OneExpression(RomanNonTerminalExpression):

            def __init__(self):
                one_terminal = RomanTerminalExpression('I')
                four_terminal = RomanTerminalExpression('IV')
                five_terminal = RomanTerminalExpression('V')
                nine_terminal = RomanTerminalExpression('IX')
    
                super().__init__(one=one_terminal, four=four_terminal, five=five_terminal, nine=nine_terminal)
            
            def multiplier(self):
                return 1

        self.roman = "MCMXXVIII"
        self.context = Context(self.roman)
        self.expressions = [ThousandExpression(), HundredExpression(), TenExpression(), OneExpression()]

    def test_interpret(self):
        """
        Test the interpret method.

        @raise AssertionError: If the test fails.
        """
        for exp in self.expressions:
            exp.interpret(self.context)

        self.assertEquals(1928, int(self.context.out_data))




