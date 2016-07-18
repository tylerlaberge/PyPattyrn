from unittest import TestCase
from tests.utils.dummy import dummy_class_factory
from abc import ABCMeta, ABC


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
        dummy_class = dummy_class_factory(attributes={'a': self.a, 'b': self.b},
                                          functions={'add': self.add_function, 'subtract': self.subtract_function})

        dummy = dummy_class()

        self.assertEquals(self.a, dummy.a)
        self.assertEquals(self.b, dummy.b)

    def test_add(self):
        """
        Test a dummy class initialized with an add function.

        @raise AssertionError: If the test fails.
        """
        dummy_class = dummy_class_factory(attributes={'a': self.a, 'b': self.b},
                                          functions={'add': self.add_function})

        dummy = dummy_class()
        self.assertEquals(15, dummy.add())

    def test_subtract(self):
        """
        Test a dummy class initialized with a subtract function.

        @raise AssertionError: If the test fails.
        """
        dummy_class = dummy_class_factory(attributes={'a': self.a, 'b': self.b},
                                          functions={'subtract': self.subtract_function})

        dummy = dummy_class()
        self.assertEquals(5, dummy.subtract())

    def test_instances(self):
        """
        Test multiple instances.

        @raise AssertionError: If the test fails.
        """
        dummy_class_one = dummy_class_factory(attributes={'a': self.a, 'b': self.b},
                                              functions={'add': self.add_function})

        dummy_class_one_instance_one = dummy_class_one()
        dummy_class_one_instance_two = dummy_class_one()

        self.assertEquals(dummy_class_one_instance_one.a, dummy_class_one_instance_two.a)
        self.assertEquals(dummy_class_one_instance_one.b, dummy_class_one_instance_two.b)
        self.assertEquals(dummy_class_one_instance_one.add(), dummy_class_one_instance_two.add())

    def test_classes(self):
        """
        Test multiple classes.

        @raise AssertionError: If the test fails.
        """
        dummy_class_one = dummy_class_factory(attributes={'a': self.a, 'b': self.b},
                                              functions={'add': self.add_function})
        dummy_class_two = dummy_class_factory(attributes={'a': 30, 'b': 10},
                                              functions={'subtract': self.subtract_function})

        self.assertNotEquals(dummy_class_one.a, dummy_class_two.a)
        self.assertNotEquals(dummy_class_one.b, dummy_class_two.b)

        assert (hasattr(dummy_class_one, 'add'))
        assert (not hasattr(dummy_class_one, 'subtract'))

        assert (hasattr(dummy_class_two, 'subtract'))
        assert (not hasattr(dummy_class_two, 'add'))

    def test_meta_class(self):
        """
        Test assigning a metaclass.

        @raise AssertionError: If the test fails.
        """
        dummy_class = dummy_class_factory(attributes={'a': self.a, 'b': self.b},
                                          functions={'add': self.add_function},
                                          meta_class=ABCMeta)

        self.assertEquals(ABCMeta, dummy_class.__class__)

    def test_base_class(self):
        """
        Test assigning a base class.

        @raise AssertionError: If the test fails
        """
        dummy_class = dummy_class_factory(attributes={'a': self.a, 'b': self.b},
                                          functions={'add': self.add_function},
                                          base_class=ABC)

        self.assertEquals(ABC, dummy_class.__base__)




