from unittest import TestCase
from pypatterns.structural.bridge import Bridge


class BridgeTestCase(TestCase):
    """
    Unit testing class for the Bridge class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class DrawingAPI(object):

            def __init__(self): pass

            def draw_circle(self): pass

            def draw_rectangle(self): pass

        class DrawingAPI1(DrawingAPI):

            def draw_circle(self):
                return 'draw circle 1'

            def draw_rectangle(self):
                return 'draw rectangle 1'

        class DrawingAPI2(DrawingAPI):

            def draw_circle(self):
                return 'draw circle 2'

            def draw_rectangle(self):
                return 'draw rectangle 2'

        class Shape(Bridge):

            def draw(self): pass

            def do_something_high_level(self): pass

        class CircleShape(Shape):

            def draw(self):
                return self.implementor.draw_circle()

            def do_something_high_level(self):
                return 'high level circle'

        class RectangleShape(Shape):

            def draw(self):
                return self.implementor.draw_rectangle()

            def do_something_high_level(self):
                return 'high level rectangle'

        self.drawing_api_one = DrawingAPI1()
        self.drawing_api_two = DrawingAPI2()

        self.circle_shape_one = CircleShape(self.drawing_api_one)
        self.circle_shape_two = CircleShape(self.drawing_api_two)

        self.rectangle_shape_one = RectangleShape(self.drawing_api_one)
        self.rectangle_shape_two = RectangleShape(self.drawing_api_two)

    def test_init(self):
        """
        Test the __init__ method.

        @raise AssertionError: If the test fails.
        """
        self.assertEquals(self.drawing_api_one, self.circle_shape_one.implementor)
        self.assertEquals(self.drawing_api_two, self.circle_shape_two.implementor)
        self.assertEquals(self.drawing_api_one, self.rectangle_shape_one.implementor)
        self.assertEquals(self.drawing_api_two, self.rectangle_shape_two.implementor)

    def test_implementation(self):
        """
        Test an implementation of the bridge pattern

        @raise AssertionError: If the test fails.
        """
        self.assertEquals('draw circle 1', self.circle_shape_one.draw())
        self.assertEquals('draw circle 2', self.circle_shape_two.draw())
        self.assertEquals('draw rectangle 1', self.rectangle_shape_one.draw())
        self.assertEquals('draw rectangle 2', self.rectangle_shape_two.draw())

        self.assertEquals('high level circle', self.circle_shape_one.do_something_high_level())
        self.assertEquals('high level circle', self.circle_shape_two.do_something_high_level())
        self.assertEquals('high level rectangle', self.rectangle_shape_one.do_something_high_level())
        self.assertEquals('high level rectangle', self.rectangle_shape_two.do_something_high_level())
