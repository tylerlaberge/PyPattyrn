from unittest import TestCase
from tests.utils.dummy_class import DummyClass


class DummyClassTestCase(TestCase):
    """
    Unit testing class for the DummyClass class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        self.a = 10
        self.b = 5
        self.add_function = lambda instance: instance.a + instance.b
        self.subtract_function = lambda instance: instance.a - instance.b

    def test_init(self):
        """
        Test the __init__ method.

        @raise AssertionError: If the test fails.
        """
        dummy = DummyClass(attributes={'a': self.a, 'b': self.b},
                           functions={'add': self.add_function, 'subtract': self.subtract_function})

        self.assertEquals(self.a, dummy.a)
        self.assertEquals(self.b, dummy.b)

    def test_invalid_init(self):
        """
        Test the __init__ method with invalid parameters.

        @raise AssertionError if the test fails:
        """
        with self.assertRaises(ValueError):
            DummyClass(attributes={'a': self.add_function}, functions={'add': self.a})

    def test_add(self):
        """
        Test a dummy class initialized with an add function.

        @raise AssertionError: If the test fails.
        """
        dummy = DummyClass(attributes={'a': self.a, 'b': self.b},
                           functions={'add': self.add_function})

        self.assertEquals(15, dummy.add())

    def test_subtract(self):
        """
        Test a dummy class initialized with a subtract function.

        @raise AssertionError: If the test fails.
        """
        dummy = DummyClass(attributes={'a': self.a, 'b': self.b},
                           functions={'subtract': self.subtract_function})

        self.assertEquals(5, dummy.subtract())




