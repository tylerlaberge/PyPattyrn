import time
from unittest import TestCase
from pypattyrn.structural.decorator import DecoratorSimple, DecoratorComplex, CallWrapper


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


class DecoratorComplexTestCase(TestCase):
    """
    Unit testing class for the DecoratorComplex class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class Alert(DecoratorComplex):

            def __init__(self, alert_time):
                self.alert_time = alert_time

            @CallWrapper
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
        class SlowClass(object):

            @self.alert(1)
            def slow_function_true(self):
                time.sleep(2)
                return 'foo'

            @self.alert(1)
            def slow_function_false(self):
                return 'bar'

        slow_class = SlowClass()
        self.assertEquals(('foo', True), slow_class.slow_function_true())
        self.assertEquals(('bar', False), slow_class.slow_function_false())

    def test_decorate_args(self):
        """
        Test decorating a function with args.

        @raise AssertionError: If the test fails.
        """

        class SlowClass(object):

            @self.alert(1)
            def slow_function_true(self, n):
                time.sleep(n)
                return 'foo'

            @self.alert(1)
            def slow_function_false(self, n):
                return n

        slow_class = SlowClass()
        self.assertEquals(('foo', True), slow_class.slow_function_true(2))
        self.assertEquals((10, False), slow_class.slow_function_false(10))

    def test_decorate_kwargs(self):
        """
        Test decorating a function with kwargs

        @raise AssertionError: If the test fails.
        """
        class SlowClass(object):

            @self.alert(1)
            def slow_function_true(self, n=0):
                time.sleep(n)
                return 'foo'

            @self.alert(1)
            def slow_function_false(self, n=0):
                return n

        slow_class = SlowClass()
        self.assertEquals(('foo', True), slow_class.slow_function_true(n=2))
        self.assertEquals((10, False), slow_class.slow_function_false(n=10))


class WrapTestCase(TestCase):
    """
    Unit testing class for the CallWrapper decorator class.
    """
    def test_wrap(self):
        """
        Test the wrap decorator

        @raise AssertionError: If the test fails.
        """
        class SlowClass(DecoratorComplex):

            def __init__(self, sleep_time):
                self.sleep_time = sleep_time
                self.end_time = None

            @CallWrapper
            def __call__(self, func, *args, **kwargs):
                start_time = time.time()
                return_val = func(*args, **kwargs)
                time.sleep(self.sleep_time)
                end_time = time.time() - start_time
                self.end_time = end_time
                return return_val, self.sleep_time, self.end_time

        @SlowClass(1)
        def hello_world(n):
            return ['hello world' for _ in range(n)]

        return_val, sleeptime, end_time = hello_world(5)

        self.assertEquals(1, sleeptime)
        self.assertAlmostEquals(1, end_time, delta=1)
        self.assertListEqual(['hello world' for _ in range(5)], return_val)
