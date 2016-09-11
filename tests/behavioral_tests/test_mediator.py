from unittest import TestCase
from pypattyrn.behavioral.mediator import Mediator


class MediatorTestCase(TestCase):
    """
    Unit testing class for the Mediator class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class Dog(object):
            self.sound = ''

            def set_sound(self, sound):
                self.sound = sound

        class Cat(object):
            self.sound = ''

            def set_sound(self, sound):
                self.sound = sound

        self.dog = Dog()
        self.cat = Cat()

    def test_connect(self):
        """
        Test connecting a receiver to a signal.

        @raise AssertionError: If the test fails.
        """
        mediator = Mediator()
        mediator.connect('set_dog_sound', self.dog.set_sound)
        self.assertEquals([self.dog.set_sound], mediator.signals['set_dog_sound'])

        mediator.connect('set_cat_sound', self.cat.set_sound)
        self.assertEquals([self.cat.set_sound], mediator.signals['set_cat_sound'])

    def test_disconnect(self):
        """
        Test disconnecting a receiver from a signal.

        @raise AssertionError: If the test fails.
        """
        mediator = Mediator()
        mediator.connect('set_dog_sound', self.dog.set_sound)
        self.assertEquals([self.dog.set_sound], mediator.signals['set_dog_sound'])

        mediator.disconnect('set_dog_sound', self.dog.set_sound)
        self.assertEquals([], mediator.signals['set_dog_sound'])

    def test_signal(self):
        """
        Test the signal method.

        @raise AssertionError: If the test fails.
        """
        mediator = Mediator()
        mediator.connect('set_dog_sound', self.dog.set_sound)
        mediator.connect('set_cat_sound', self.cat.set_sound)
        mediator.signal('set_dog_sound', 'woof')
        mediator.signal('set_cat_sound', 'meow')

        self.assertEquals('woof', self.dog.sound)
        self.assertEquals('meow', self.cat.sound)

    def test_invalid_disconnect(self):
        """
        Test disconnecting an unconnected receiver.

        @raise AssertionError: If the test fails.
        """
        mediator = Mediator()
        try:
            mediator.disconnect('foo', self.dog.set_sound)
            mediator.disconnect('bar', self.cat.set_sound)
        except:
            raise AssertionError()

    def test_invalid_signal(self):
        """
        Test sending a signal that no one is connected to.

        @raise AssertionError: If the test fails.
        """
        mediator = Mediator()

        try:
            mediator.signal('foo')
        except:
            raise AssertionError()




