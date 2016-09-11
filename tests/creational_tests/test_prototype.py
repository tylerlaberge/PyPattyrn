from math import sqrt
from unittest import TestCase

from pypattyrn.creational.prototype import Prototype


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

    def test_prototype_instances(self):
        """
        Test that prototype returns a new instance.

        @raise AssertionError: If the test fails.
        """
        point_one = self.__point_class(5, 5)
        point_two = point_one.prototype()

        self.assertEquals(point_one.__class__, point_two.__class__)
        self.assertNotEquals(id(point_one), id(point_two))

    def test_identical_prototype(self):
        """
        Test the prototype method without updating any attributes.

        @raise AssertionError: If the test fails.
        """
        point_one = self.__point_class(5, 5)
        point_two = point_one.prototype()

        self.assertEquals(point_one.__dict__, point_two.__dict__)

    def test_update_attributes_prototype(self):
        """
        Test the prototype method with updated attributes.

        @raise AssertionError: If the test fails.
        """
        point_one = self.__point_class(10, 10)
        point_two = point_one.prototype(x=15, y=20)
        point_three = point_two.prototype()

        self.assertEquals(point_one.__dict__, {'x': 10, 'y': 10})
        self.assertEquals(point_two.__dict__, {'x': 15, 'y': 20})
        self.assertEquals(point_three.__dict__, point_two.__dict__)

    def test_add_attributes_prototype(self):
        """
        Test the prototype method with completely new attributes.

        @raise AssertionError: If the test fails.
        """
        point_one = self.__point_class(15, 15)
        point_two = point_one.prototype(z=20)
        point_three = point_two.prototype()

        self.assertEquals(point_one.x, point_two.x)
        self.assertEquals(point_one.y, point_two.y)
        self.assertFalse(hasattr(point_one, 'z'))
        self.assertTrue(hasattr(point_two, 'z'))
        self.assertEquals(point_two.z, 20)
        self.assertEquals(point_three.__dict__, point_two.__dict__)

    def test_add_function_prototype(self):
        """
        Test the prototype method with a new instance method.

        @raise AssertionError: If the test fails.
        """
        point_one = self.__point_class(20, 25)

        def distance_to(this, other):
            return sqrt((this.x - other.x) ** 2 + (this.y - other.y) ** 2)

        point_two = point_one.prototype(distance_to=distance_to)
        point_three = point_two.prototype()

        self.assertFalse(hasattr(point_one, 'distance_to'))
        self.assertTrue(hasattr(point_two, 'distance_to'))
        self.assertEquals(point_two.distance_to(point_one), 0)
        self.assertTrue(hasattr(point_three, 'distance_to'))
        self.assertEquals(point_three.distance_to(point_two), 0)
