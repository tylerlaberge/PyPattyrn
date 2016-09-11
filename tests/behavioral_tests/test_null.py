from unittest import TestCase
from pypattyrn.behavioral.null import Null


class NullTestCase(TestCase):
    """
    Unit testing class for the Null class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        self.null = Null()

    def test_init(self):
        """
        Test the init method.

        @raise AssertionError: If the test fails.
        """
        try:
            Null()
            Null('value')
            Null('value', param='value')
        except:
            raise AssertionError()

    def test_call(self):
        """
        Test calling a Null object.

        @raise AssertionError: If the test fails.
        """
        self.assertEquals(self.null, self.null())
        self.assertEquals(self.null, self.null('value'))
        self.assertEquals(self.null, self.null('value', param='value'))

    def test_get_attribute(self):
        """
        Test getting attributes of a Null object.

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

    def test_set_attribute(self):
        """
        Test setting attributes of a Null object.

        @raise AssertionError: If the test fails.
        """
        try:
            self.null.attr1 = 'value'
            self.null.attr1.attr2 = 'value'
        except:
            raise AssertionError()

    def test_del_attribute(self):
        """
        Test deleting an attribute of a Null object.

        @raise AssertionError: If the test fails.
        """
        try:
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
