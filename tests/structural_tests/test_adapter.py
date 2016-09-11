from unittest import TestCase
from pypattyrn.structural.adapter import Adapter


class AdapterTestCase(TestCase):
    """
    Unit testing class for the Adapter class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class Dog(object):
            def __init__(self):
                self.name = "Dog"

            def bark(self):
                return "woof!"

        class Cat(object):
            def __init__(self):
                self.name = "Cat"

            def meow(self):
                return "meow!"

        self.cat = Cat()
        self.dog = Dog()

    def test_init(self):
        """
        Test the init method.

        @raise AssertionError: If the test fails.
        """
        cat_adapter = Adapter(self.cat, make_noise=self.cat.meow, foo=self.cat.name)
        dog_adapter = Adapter(self.dog, make_noise=self.dog.bark, foo=self.dog.name)

        self.assertIn('make_noise', cat_adapter.__dict__)
        self.assertIn('make_noise', dog_adapter.__dict__)

        self.assertNotIn('foo', cat_adapter.__dict__)
        self.assertNotIn('foo', dog_adapter.__dict__)

        self.assertEquals(cat_adapter.make_noise, self.cat.meow)
        self.assertEquals(dog_adapter.make_noise, self.dog.bark)

    def test_getattr(self):
        """
        Test the __getattr__ method.

        @raise AssertionError: If the test fails.
        """
        cat_adapter = Adapter(self.cat, make_noise=self.cat.meow)
        dog_adapter = Adapter(self.dog, make_noise=self.dog.bark)

        self.assertEquals('Cat', cat_adapter.name)
        self.assertEquals('Dog', dog_adapter.name)

    def test_original_dict(self):
        """
        Test the original_dict method.

        @raise AssertionError: If the test fails.
        """
        cat_adapter = Adapter(self.cat, make_noise=self.cat.meow)
        dog_adapter = Adapter(self.dog, make_noise=self.dog.bark)

        self.assertEquals(self.cat.__dict__, cat_adapter.original_dict())
        self.assertEquals(self.dog.__dict__, dog_adapter.original_dict())

    def test_adapted_method(self):
        """
        Test and adapted method.

        @raise AssertionError: If the test fails.
        """
        cat_adapter = Adapter(self.cat, make_noise=self.cat.meow)
        dog_adapter = Adapter(self.dog, make_noise=self.dog.bark)

        self.assertEquals('meow!', cat_adapter.make_noise())
        self.assertEquals('woof!', dog_adapter.make_noise())
