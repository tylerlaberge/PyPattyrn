from unittest import TestCase

from copy import deepcopy
from pypatterns.creational.pool import Reusable, Pool


class ReusableTestCase(TestCase):
    """
    Unit testing class for the reusable class.
    """

    def setUp(self):
        """
        Initialize testing data.
        """

        class Dog(Reusable):
            def __init__(self):
                self.sound = "woof"
                super(Dog, self).__init__()

        self.dog_class = Dog

    def test_reset(self):
        """
        Test the reset method.

        @raise AssertionError: If the test fails.
        """
        dog = self.dog_class()
        original_state = deepcopy(dog.__dict__)
        original_sound = dog.sound
        dog.sound = "bark"
        changed_sound = dog.sound
        dog.reset()
        reset_sound = dog.sound
        dog.sound = "meow"
        changed_sound_two = dog.sound
        dog.reset()
        reset_sound_two = dog.sound
        dog.name = "george"
        dog.reset()
        final_state = deepcopy(dog.__dict__)

        self.assertEquals("woof", original_sound)
        self.assertEquals("bark", changed_sound)
        self.assertEquals("woof", reset_sound)
        self.assertEquals("meow", changed_sound_two)
        self.assertEquals("woof", reset_sound_two)
        self.assertEquals(original_state, final_state)


class PoolTestCase(TestCase):
    """
    Unit testing class for the Pool class.
    """

    def setUp(self):
        """
        Initialize testing data.
        """

        class Dog(Reusable):
            def __init__(self, sound, name):
                self.sound = sound
                self.name = name
                super(Dog, self).__init__()

        class DogPool(Pool):
            def __init__(self):
                super(DogPool, self).__init__(Dog, 'woof', 'george')

        self.dog_pool_class = DogPool

    def test_acquire(self):
        """
        Test the acquire method.

        @raise AssertionError: If the test fails.
        """
        dog_pool = self.dog_pool_class()
        dog_one = dog_pool.acquire()
        dog_two = dog_pool.acquire()
        dog_three = dog_pool.acquire()

        self.assertEquals(dog_one.__dict__, dog_two.__dict__, dog_three.__dict__)
        self.assertNotEquals(id(dog_one), id(dog_two), id(dog_three))

    def test_release(self):
        """
        Test the release method.

        @raise AssertionError: If the test fails.
        """
        dog_pool = self.dog_pool_class()

        dog_one = dog_pool.acquire()
        dog_two = dog_pool.acquire()
        dog_two.sound = 'meow'

        dog_pool.release(dog_one)
        dog_three = dog_pool.acquire()
        self.assertEquals(id(dog_one), id(dog_three))

        dog_pool.release(dog_two)
        dog_four = dog_pool.acquire()
        self.assertEquals(id(dog_two), id(dog_four))

        self.assertEquals(dog_one.__dict__, dog_two.__dict__)
        self.assertEquals(dog_three.__dict__, dog_four.__dict__)
        self.assertEquals(dog_one.__dict__, dog_four.__dict__)

    def test_singleton(self):
        """
        Test that the pool class is a singleton

        @raise AssertionError: If the test fails.
        """
        dog_pool_one = self.dog_pool_class()
        dog_pool_two = self.dog_pool_class()

        class Cat(Reusable):
            def __init__(self, sound, name):
                self.sound = sound
                self.name = name
                super().__init__()

        class CatPool(Pool):
            def __init__(self):
                super().__init__(Cat, 'meow', 'tom')

        cat_pool_one = CatPool()
        cat_pool_two = CatPool()

        self.assertEquals(id(dog_pool_one), id(dog_pool_two))
        self.assertEquals(id(cat_pool_one), id(cat_pool_two))
        self.assertNotEquals(id(dog_pool_one), id(cat_pool_one))
