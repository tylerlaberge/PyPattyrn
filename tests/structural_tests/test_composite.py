from abc import ABCMeta, abstractmethod
from unittest import TestCase
from pypattyrn.structural.composite import Composite


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

        class Leaf(Component):

            def __init__(self):
                self.did_something = False

            def do_something(self):
                self.did_something = True

        self.component_class = Component
        self.leaf_one = Leaf()
        self.leaf_two = Leaf()
        self.leaf_three = Leaf()

    def test_add_component(self):
        """
        Test the add_component method.

        @raise AssertionError: If the test fails.
        """
        composite = Composite(self.component_class)
        composite.add_component(self.leaf_one)

        composite_two = Composite(self.component_class)
        composite_two.add_component(self.leaf_two)

        composite_three = Composite(self.component_class)
        composite_three.add_component(self.leaf_three)

        composite_two.add_component(composite_three)

        composite.add_component(composite_two)

        try:
            composite.add_component(composite_two)
            composite_two.add_component(composite_three)
        except:
            raise AssertionError()
        else:
            self.assertSetEqual({self.leaf_one, composite_two}, composite.components)
            self.assertSetEqual({self.leaf_two, composite_three}, composite_two.components)
            self.assertSetEqual({self.leaf_three}, composite_three.components)

    def test_remove_component(self):
        """
        Test the remove_component method.

        @raise AssertionError: If the test fails.
        """
        composite = Composite(self.component_class)

        composite_two = Composite(self.component_class)
        composite_two.add_component(self.leaf_one)
        composite_two.add_component(self.leaf_two)

        composite.add_component(self.leaf_one)
        composite.add_component(self.leaf_two)
        composite.add_component(composite_two)

        composite.remove_component(self.leaf_one)
        composite.remove_component(self.leaf_two)
        composite.remove_component(composite_two)
        try:
            composite.remove_component(composite_two)
        except:
            raise AssertionError
        else:
            self.assertSetEqual(set(), composite.components)

    def test_delegate(self):
        """
        Test the delegate method.

        @raise AssertionError: If the test fails
        """
        composite = Composite(self.component_class)
        composite_two = Composite(self.component_class)
        composite_three = Composite(self.component_class)

        composite.add_component(self.leaf_one)
        composite_two.add_component(self.leaf_two)
        composite_three.add_component(self.leaf_three)

        composite_two.add_component(composite_three)
        composite.add_component(composite_two)

        composite._delegate('do_something')

        self.assertTrue(self.leaf_one.did_something)
        self.assertTrue(self.leaf_two.did_something)
        self.assertTrue(self.leaf_three.did_something)

        self.leaf_one.did_something = False
        self.leaf_two.did_something = False
        self.leaf_three.did_something = False

    def test_getattr(self):
        """
        Test the getattr method.

        @raise AssertionError: If the test fails.
        """
        composite = Composite(self.component_class)
        composite_two = Composite(self.component_class)
        composite_three = Composite(self.component_class)

        composite.add_component(self.leaf_one)
        composite_two.add_component(self.leaf_two)
        composite_three.add_component(self.leaf_three)

        composite_two.add_component(composite_three)
        composite.add_component(composite_two)

        composite.do_something()

        self.assertTrue(self.leaf_one.did_something)
        self.assertTrue(self.leaf_two.did_something)
        self.assertTrue(self.leaf_three.did_something)

        self.leaf_one.did_something = False
        self.leaf_two.did_something = False
        self.leaf_three.did_something = False

    def test_invalid_getattr(self):
        """
        Test the getattr method with an invalid attribute.

        @raise AssertionError: If the test fails.
        """
        composite = Composite(self.component_class)
        composite_two = Composite(self.component_class)
        composite_three = Composite(self.component_class)

        composite.add_component(self.leaf_one)
        composite_two.add_component(self.leaf_two)
        composite_three.add_component(self.leaf_three)

        composite_two.add_component(composite_three)
        composite.add_component(composite_two)

        with self.assertRaises(AttributeError):
            composite.foo()
            composite.did_something()

    def test_interface(self):
        """
        Test the interface functionality.

        @raise AssertionError: If the test fails.
        """
        class BadComponent(object):
            def foo(self):
                raise NotImplementedError()

        class BadLeaf(BadComponent):
            def __init__(self):
                pass

            def foo(self):
                pass

        composite = Composite(self.component_class)
        composite_two = Composite(BadComponent)
        composite_two.add_component(BadLeaf())

        self.assertRaises(AttributeError, composite_two.add_component, self.leaf_one)
        self.assertRaises(AttributeError, composite.add_component, composite_two)
        self.assertRaises(AttributeError, composite.add_component, BadLeaf())
