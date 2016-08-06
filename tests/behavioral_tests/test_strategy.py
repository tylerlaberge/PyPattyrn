from unittest import TestCase
from pypatterns.behavioral.strategy import Strategy


class StategyTestCase(TestCase):
    """
    Unit testing class for the Strategy pattern.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class AddStrategy(Strategy):

            def __call__(self, a, b):
                return a + b

        class SubtractStrategy(Strategy):

            def __call__(self, a, b):
                return a - b

        class Solver(object):

            def __init__(self, strategy):
                self.strategy = strategy

            def solve(self, a, b):
                return self.strategy(a, b)

        self.add_class = AddStrategy
        self.subtract_class = SubtractStrategy
        self.solver_class = Solver

    def test_add_strategy(self):
        """
        Test the add strategy.

        @raise AssertionError: If the test fails.
        """
        solver = self.solver_class(self.add_class())

        self.assertEquals(15, solver.solve(5, 10))

    def test_subtract_strategy(self):
        """
        Test the subtract strategy.

        @raise AssertionError: If the test fails.
        """
        solver = self.solver_class(self.subtract_class())

        self.assertEquals(10, solver.solve(100, 90))

    def test_switch_strategies(self):
        """
        Test changing out strategies.

        @raise AssertionError: If the test fails.
        """
        solver = self.solver_class(self.add_class())
        self.assertEquals(5, solver.solve(2, 3))

        solver.strategy = self.subtract_class()
        self.assertEquals(-1, solver.solve(2, 3))

