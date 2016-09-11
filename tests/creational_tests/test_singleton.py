from unittest import TestCase
from pypattyrn.creational.singleton import Singleton


class SingletonTestCase(TestCase):
    """
    Unit testing class for the singleton design pattern.
    """

    def setUp(self):
        """
        Initialize testing data.
        """
        class DummySingletonOne(object, metaclass=Singleton):

            def __init__(self):
                pass

        class DummySingletonTwo(object, metaclass=Singleton):

            def __init__(self):
                pass

        self.dummy_class_one = DummySingletonOne

        self.dummy_class_two = DummySingletonTwo

    def test_single(self):
        """
        Test instances from a single singleton class.

        @raise AssertionError: If the test fails.
        """
        dummy_one = self.dummy_class_one()
        dummy_two = self.dummy_class_one()

        self.assertEquals(id(dummy_one), id(dummy_two))

    def test_multiple(self):
        """
        Test instances from multiple singleton classes.

        @raise AssertionError: If the test fails.
        """
        dummy_class_one_instance_one = self.dummy_class_one()
        dummy_class_one_instance_two = self.dummy_class_one()

        dummy_class_two_instance_one = self.dummy_class_two()
        dummy_class_two_instance_two = self.dummy_class_two()

        self.assertEquals(id(dummy_class_one_instance_one), id(dummy_class_one_instance_two))
        self.assertEquals(id(dummy_class_two_instance_one), id(dummy_class_two_instance_two))

        self.assertNotEquals(id(dummy_class_one_instance_one), id(dummy_class_two_instance_one))
        self.assertNotEquals(id(dummy_class_one_instance_two), id(dummy_class_two_instance_two))
