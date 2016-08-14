from abc import ABCMeta, abstractmethod
from unittest import TestCase
from pypatterns.structural.composite import Composite


class CompositeTestCase(TestCase):
    """
    Unit testing class for the Composite class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class Component(object, metaclass=ABCMeta):

            @abstractmethod
            def do_something(self):
                pass

        class LeafOne(Component):

            def __init__(self):
                self.did_something = False

            def do_something(self):
                self.did_something = True

        class LeafTwo(Component):

            def __init__(self):
                self.did_something = False

            def do_something(self):
                self.did_something = True

        self.component_class = Component
        self.leaf_one = LeafOne()
        self.leaf_two = LeafTwo()

    def test_init(self):

        composite = Composite(self.component_class)

        self.assertIn('do_something', composite._method_names)

    def test_add_invalid_component(self):

        composite = Composite(self.component_class)

        class BadComponent(object):

            def foo(self):
                pass

        with self.assertRaises(AttributeError):
            composite.add_component(BadComponent)

    def test_add_component(self):

        composite = Composite(self.component_class)
        composite.add_component(self.leaf_one)
        composite.add_component(self.leaf_two)
        try:
            composite.add_component(self.leaf_two)
        except:
            raise AssertionError
        else:
            self.assertSetEqual({self.leaf_one, self.leaf_two}, composite.components)

    def test_remove_component(self):

        composite = Composite(self.component_class)

        composite.add_component(self.leaf_one)
        composite.add_component(self.leaf_two)

        composite.remove_component(self.leaf_one)
        composite.remove_component(self.leaf_two)
        try:
            composite.remove_component(self.leaf_two)
        except:
            raise AssertionError
        else:
            self.assertSetEqual(set(), composite.components)

    def test_delegate(self):

        composite = Composite(self.component_class)

        composite.add_component(self.leaf_one)
        composite.add_component(self.leaf_two)

        composite.delegate('do_something')

        self.assertTrue(self.leaf_one.did_something)
        self.assertTrue(self.leaf_two.did_something)

        self.leaf_one.did_something = False
        self.leaf_two.did_something = False

    def test_getattr(self):

        composite = Composite(self.component_class)

        composite.add_component(self.leaf_one)
        composite.add_component(self.leaf_two)

        composite.do_something()

        self.assertTrue(self.leaf_one.did_something)
        self.assertTrue(self.leaf_two.did_something)

        self.leaf_one.did_something = False
        self.leaf_two.did_something = False

    def test_invalid_getattr(self):

        composite = Composite(self.component_class)

        composite.add_component(self.leaf_one)
        composite.add_component(self.leaf_two)

        with self.assertRaises(AttributeError):
            composite.foo()
            composite.did_something()