from unittest import TestCase
from pypattyrn.behavioral.iterator import Iterable, Iterator


class IterableTestCase(TestCase):
    """
    Unit testing class for the Iterable class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class Counter(Iterable):

            def __init__(self, max):
                self.count = 0
                self.max = max

            def __next__(self):
                self.count += 1
                if self.count > self.max:
                    raise StopIteration
                else:
                    return self.count - 1

        self.counter_class = Counter

    def test_next(self):
        """
        Test the iterables next method.

        @raise AssertionError: If the test fails.
        """
        counter = self.counter_class(10)
        for i in range(10):
            self.assertEquals(i, counter.__next__())

    def test_stop_iteration(self):
        """
        Test that StopIteration is raised.

        @raise AssertionError: If the test fails.
        """
        counter = self.counter_class(0)
        with self.assertRaises(StopIteration):
            counter.__next__()


class IteratorTestCase(TestCase):
    """
    Unit testing class for the Iterator class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class Counter(Iterable):

            def __init__(self, max):
                self.count = 0
                self.max = max

            def __next__(self):
                self.count += 1
                if self.count > self.max:
                    raise StopIteration
                else:
                    return self.count - 1

        class CounterIterator(Iterator):

            def __init__(self):
                super().__init__(Counter(10))

        self.counter_iterator_class = CounterIterator

    def test_next(self):
        """
        Test the built in next method on the Iterator.

        @raise AssertionError: If the test fails.
        """
        counter_iterator = self.counter_iterator_class()
        for i in range(10):
            self.assertEquals(i, next(counter_iterator))

    def test_stop_iteration(self):
        """
        Test that stop iteration is raised.

        @raise AssertionError: If the test fails.
        """
        counter_iterator = self.counter_iterator_class()

        with self.assertRaises(StopIteration):
            for i in range(12):
                next(counter_iterator)

    def test_loop(self):
        """
        Test looping over an Iterator class.

        @raise AssertionError: If the test fails.
        """
        counter_iterator = self.counter_iterator_class()
        i = 0
        for count in counter_iterator:
            self.assertEquals(i, count)
            i += 1
