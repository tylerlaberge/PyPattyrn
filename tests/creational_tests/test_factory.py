from unittest import TestCase

from pypattyrn.creational.factory import Factory, AbstractFactory


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


class AbstractFactoryTestCase(TestCase):
    """
    Unit testing class for the AbstractFactory class.
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

        class AnimalFactory(AbstractFactory):
            def __init__(self):
                super().__init__()
                self._register('cat', CatFactory())
                self._register('dog', DogFactory())

            def create(self, animal_type):
                return self._factories[animal_type].create()

        self.cat_class = Cat
        self.dog_class = Dog
        self.animal_factory = AnimalFactory()

    def test_create(self):
        """
        Test the create method.

        @raise AssertionError: If the test fails.
        """
        cat = self.animal_factory.create('cat')
        dog = self.animal_factory.create('dog')

        self.assertEquals(self.cat_class, cat.__class__)
        self.assertEquals(self.dog_class, dog.__class__)

        self.assertEquals('Meow', cat.speak())
        self.assertEquals('Woof', dog.speak())
