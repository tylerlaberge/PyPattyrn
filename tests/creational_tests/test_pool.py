from unittest import TestCase

from copy import deepcopy
from pypattyrn.creational.pool import Reusable, Pool


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
                super().__init__()

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
        dog.reset()
        final_state = deepcopy(dog.__dict__)

        original_state.pop('memento')
        final_state.pop('memento')

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
            def __init__(self, sound):
                self.sound = sound
                super(Dog, self).__init__()

        class DogPool(Pool):
            def __init__(self):
                super(DogPool, self).__init__(Dog, 'woof')

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

        self.assertEquals(dog_one.sound, dog_two.sound, dog_three.sound)
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

        self.assertEquals(dog_one.sound, dog_two.sound)
        self.assertEquals(dog_three.sound, dog_four.sound)
        self.assertEquals(dog_one.sound, dog_four.sound)
