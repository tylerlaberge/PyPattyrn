from unittest import TestCase
from pypatterns.behavioral.null import Null


class NullTestCase(TestCase):
    """
    Unit testing class for the Null class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        self.null = Null()

    def test_constructing(self):
        """
        Test constructing a Null object.

        @raise AssertionError: If the test fails.
        """
        try:
            n = Null()
            n = Null('value')
            n = Null('value', param='value')
        except:
            raise AssertionError()

    def test_calling(self):
        """
        Test calling a Null object.

        @raise AssertionError: If the test fails.
        """
        self.assertEquals(self.null, self.null())
        self.assertEquals(self.null, self.null('value'))
        self.assertEquals(self.null, self.null('value', param='value'))

    def test_attribute_handling(self):
        """
        Test attribute handling on a Null object.

        @raise AssertionError: If the test fails.
        """
        self.assertEquals(self.null, self.null.attr1)
        self.assertEquals(self.null, self.null.attr2)
        self.assertEquals(self.null, self.null.method1())
        self.assertEquals(self.null, self.null.method1().method2())
        self.assertEquals(self.null, self.null.method('value'))
        self.assertEquals(self.null, self.null.method(param='value'))
        self.assertEquals(self.null, self.null.method('value', param='value'))
        self.assertEquals(self.null, self.null.attr1.method1())
        self.assertEquals(self.null, self.null.method1().attr1)

        try:
            self.null.attr1 = 'value'
            self.null.attr1.attr2 = 'value'
            del self.null.attr1
            del self.null.attr1.attr2.attr3
        except:
            raise AssertionError()

    def test_string_representation(self):
        """
        Test the string representation of a Null object.

        @raise AssertionError:
        """
        self.assertEquals('', repr(self.null))
        self.assertEquals('', str(self.null))

    def test_truthiness(self):
        """
        Test the truthiness of a Null object.

        @raise AssertionError: If the test fails.
        """
        self.assertFalse(bool(self.null))
        self.assertFalse(bool(self.null.attr1))
        self.assertFalse(bool(self.null.attr1.method1()))
        self.assertFalse(bool(self.null.method2().attr2.method1().attr1))
