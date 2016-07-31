from math import sqrt
from unittest import TestCase

from pypatterns.creational.prototype import Prototype


class PrototypeTestCase(TestCase):
    """
    Unit testing class for the Prototype class.
    """

    def setUp(self):
        """
        Initialize testing data.
        """

        class Point(Prototype):
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def move(self, x, y):
                self.x += x
                self.y += y

        self.__point_class = Point
        self.maxDiff = None

    def test_copy_instances(self):
        """
        Test that copy returns a new instance.

        @raise AssertionError: If the test fails.
        """
        point_one = self.__point_class(5, 5)
        point_two = point_one.copy()

        self.assertEquals(point_one.__class__, point_two.__class__)
        self.assertNotEquals(id(point_one), id(point_two))

    def test_identical_copy(self):
        """
        Test the copy method without updating any attributes.

        @raise AssertionError: If the test fails.
        """
        point_one = self.__point_class(5, 5)
        point_two = point_one.copy()

        self.assertEquals(point_one.__dict__, point_two.__dict__)

    def test_update_attributes_copy(self):
        """
        Test the copy method with updated attributes.

        @raise AssertionError: If the test fails.
        """
        point_one = self.__point_class(10, 10)
        point_two = point_one.copy(x=15, y=20)
        point_three = point_two.copy()

        self.assertEquals(point_one.__dict__, {'x': 10, 'y': 10})
        self.assertEquals(point_two.__dict__, {'x': 15, 'y': 20})
        self.assertEquals(point_three.__dict__, point_two.__dict__)

    def test_add_attributes_copy(self):
        """
        Test the copy method with completely new attributes.

        @raise AssertionError: If the test fails.
        """
        point_one = self.__point_class(15, 15)
        point_two = point_one.copy(z=20)
        point_three = point_two.copy()

        self.assertEquals(point_one.x, point_two.x)
        self.assertEquals(point_one.y, point_two.y)
        self.assertFalse(hasattr(point_one, 'z'))
        self.assertTrue(hasattr(point_two, 'z'))
        self.assertEquals(point_two.z, 20)
        self.assertEquals(point_three.__dict__, point_two.__dict__)

    def test_add_function_copy(self):
        """
        Test the copy method with a new instance method.

        @raise AssertionError: If the test fails.
        """
        point_one = self.__point_class(20, 25)

        def distance_to(this, other):
            return sqrt((this.x - other.x) ** 2 + (this.y - other.y) ** 2)

        point_two = point_one.copy(distance_to=distance_to)
        point_three = point_two.copy()

        self.assertFalse(hasattr(point_one, 'distance_to'))
        self.assertTrue(hasattr(point_two, 'distance_to'))
        self.assertEquals(point_two.distance_to(point_one), 0)
        self.assertTrue(hasattr(point_three, 'distance_to'))
        self.assertEquals(point_three.distance_to(point_two), 0)
