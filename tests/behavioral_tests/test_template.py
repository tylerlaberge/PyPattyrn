from unittest import TestCase
from pypatterns.behavioral.template import Template


class TemplateTestCase(TestCase):
    """
    Unit testing class for the Template class
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class MakeMeal(Template):

            def __init__(self):
                self.prepared = False
                self.cooked = False
                self.eaten = False
                self.drank = False

            def go(self):
                self.prepare()
                self.cook()
                self.eat()
                self.drink()

            def prepare(self):
                pass

            def cook(self):
                pass

            def eat(self):
                pass

            def drink(self):
                pass

        class MakePizza(MakeMeal):

            def prepare(self):
                self.prepared = True

            def cook(self):
                self.cooked = True

            def eat(self):
                self.eaten = True

        class MakeTea(MakeMeal):

            def prepare(self):
                self.prepared = True

            def cook(self):
                self.cooked = True

            def drink(self):
                self.drank = True

        self.make_pizza = MakePizza()
        self.make_tea = MakeTea()

    def test_go(self):
        """
        Test the go method.

        @raise AssertionError: If the test fails.
        """
        self.make_pizza.go()
        self.make_tea.go()

        self.assertTrue(self.make_pizza.prepared)
        self.assertTrue(self.make_pizza.cooked)
        self.assertTrue(self.make_pizza.eaten)
        self.assertFalse(self.make_pizza.drank)

        self.assertTrue(self.make_tea.prepared)
        self.assertTrue(self.make_tea.cooked)
        self.assertFalse(self.make_tea.eaten)
        self.assertTrue(self.make_tea.drank)