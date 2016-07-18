from unittest import TestCase

from tests.utils.dummy_class import dummy_factory
from patterns.creational import Singleton


class SingletonTestCase(TestCase):
    """
    Unit testing class for the singleton design pattern.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        self.dummy_class = dummy_factory(base_class=Singleton, attributes={}, functions={})

    def test_id(self):
        """
        Test the id's of two singleton instances.

        @raise AssertionError: If the test fails.
        """
        dummy = self.dummy_class()
        dummy_2 = self.dummy_class()

        self.assertEquals(id(dummy), id(dummy_2))