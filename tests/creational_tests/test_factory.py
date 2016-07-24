from unittest import TestCase
from pypatterns.creational.factory import Factory


class FactoryTestCase(TestCase):
    """
    Unit testing class for the Factory class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class Cat(object):

            def speak(self):
                return 'Meow'

        class Dog(object):

            def speak(self):
                return 'Woof'

        class CatFactory(Factory):

            def create(self, **kwargs):
                return Cat()

        class DogFactory(Factory):

            def create(self, **kwargs):
                return Dog()

        self.cat_class = Cat
        self.dog_class = Dog
        self.cat_factory = CatFactory()
        self.dog_factory = DogFactory()

    def test_not_implemented(self):
        """
        Test that TypeError is raised when the create method is not overridden.

        @raise AssertionError: If the test fails.
        """
        with self.assertRaises(TypeError):
            class EmptyFactory(Factory):
                pass

            EmptyFactory()

    def test_create(self):
        """
        Test the create method.

        @raise AssertionError: If the test fails.
        """
        cat = self.cat_factory.create()
        dog = self.dog_factory.create()

        self.assertEquals(self.cat_class, cat.__class__)
        self.assertEquals(self.dog_class, dog.__class__)

        self.assertEquals('Meow', cat.speak())
        self.assertEquals('Woof', dog.speak())
