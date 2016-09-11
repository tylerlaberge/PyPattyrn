from unittest import TestCase

from pypattyrn.behavioral.memento import Memento, Originator


class MementoTestCase(TestCase):
    """
    Unit testing class for the Memento Class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        self.state = {'foo': 'bar'}

    def test_init(self):
        """
        Test the __init__ method.

        @raise AssertionError: If the test fails.
        """
        memento = Memento(self.state)

        self.assertEqual(memento.state, self.state)


class OriginatorTestCase(TestCase):
    """
    Unit testing class for the Originator class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class Cat(Originator):

            def __init__(self, name):
                self.name = name

        self.cat_class = Cat

    def test_commit(self):
        """
        Test the commit method.

        @raise AssertionError: If the test fails.
        """
        cat = self.cat_class('Tom')
        cat_memento = cat.commit()

        self.assertDictEqual(cat.__dict__, cat_memento.state)

    def test_rollback(self):
        """
        Test the rollback method.

        @raise AssertionError: If the test fails.
        """
        cat = self.cat_class('Tom')
        cat_memento = cat.commit()

        cat.name = 'jerry'
        cat.rollback(cat_memento)

        self.assertEqual('Tom', cat.name)
