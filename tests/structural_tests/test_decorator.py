import time
from unittest import TestCase
from pypatterns.structural.decorator import DecoratorSimple, DecoratorArgs, Wrap


class DecoratorSimpleTestCase(TestCase):
    """
    Unit testing class for the DecoratorSimple class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class TimeThis(DecoratorSimple):

            def __call__(self, *args, **kwargs):
                start = time.time()
                result = self.func(*args, **kwargs)
                end = time.time() - start
                self.end = end
                return result

        self.time_this = TimeThis

    def test_decorate_function(self):
        """
        Test decorating a function.

        @raise AssertionError: If the test fails.
        """
        @self.time_this
        def slow_function():
            time.sleep(1)
            return 'foo'

        self.assertEquals('foo', slow_function())
        self.assertAlmostEqual(1.0, slow_function.end, delta=1.0)

    def test_decorate_function_with_args(self):
        """
        Test decoration a function with arguments.

        @raise AssertionError: If the test fails.
        """
        @self.time_this
        def slow_function(n):
            time.sleep(n)
            return 'foo'

        self.assertEquals('foo', slow_function(2))
        self.assertAlmostEqual(2.0, slow_function.end, delta=1.0)


class DecoratorArgsTestCase(TestCase):
    """
    Unit testing class for the DecoratorArgs class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class Alert(DecoratorArgs):

            def __init__(self, alert_time):
                self.alert_time = alert_time

            @Wrap
            def __call__(self, func, *args, **kwargs):
                start = time.time()
                return_val = func(*args, **kwargs)
                end = time.time() - start
                if end > self.alert_time:
                    return return_val, True
                return return_val, False

        self.alert = Alert

    def test_decorate(self):
        """
        Test decorating a function.

        @raise AssertionError: If the test fails.
        """
        @self.alert(1)
        def slow_function():
            time.sleep(2)
            return 'foo'

        self.assertEquals(('foo', True), slow_function())

    def test_decorate_args(self):
        """
        Test decorating a function with args.

        @raise AssertionError: If the test fails.
        """

        @self.alert(1)
        def slow_function(n):
            time.sleep(n)
            return 'foo'

        self.assertEquals(('foo', True), slow_function(2))
