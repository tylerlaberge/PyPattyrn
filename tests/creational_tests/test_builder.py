from unittest import TestCase

from abc import ABCMeta, abstractmethod
from pypattyrn.creational.builder import Director, Builder


class BuilderTestCase(TestCase):
    """
    Unit testing class for the Builder class.
    """

    def setUp(self):
        """
        Initialize testing data.
        """

        class Building(object):
            def __init__(self):
                self.floor = None
                self.size = None

            def __repr__(self):
                return 'Floor: {0.floor} | Size: {0.size}'.format(self)

        class HomeBuilder(Builder, metaclass=ABCMeta):
            def __init__(self):
                super().__init__(Building())
                self._register('floor', self._build_floor)
                self._register('size', self._build_size)

            @abstractmethod
            def _build_floor(self):
                pass

            @abstractmethod
            def _build_size(self):
                pass

        class HouseBuilder(HomeBuilder):
            def _build_floor(self):
                self.constructed_object.floor = 'One'

            def _build_size(self):
                self.constructed_object.size = 'Big'

        class FlatBuilder(HomeBuilder):
            def _build_floor(self):
                self.constructed_object.floor = 'More than one'

            def _build_size(self):
                self.constructed_object.size = 'Small'

        self.house_builder = HouseBuilder()
        self.flat_builder = FlatBuilder()

    def test_builder(self):
        """
        Test the build method.

        @raise AssertionError: If the test fails.
        """
        self.house_builder.build('floor')
        self.house_builder.build('size')
        self.assertEquals('One', self.house_builder.constructed_object.floor)
        self.assertEquals('Big', self.house_builder.constructed_object.size)
        self.assertEquals('Floor: One | Size: Big', str(self.house_builder.constructed_object))

        self.flat_builder.build('floor')
        self.flat_builder.build('size')
        self.assertEquals('More than one', self.flat_builder.constructed_object.floor)
        self.assertEquals('Small', self.flat_builder.constructed_object.size)
        self.assertEquals('Floor: More than one | Size: Small', str(self.flat_builder.constructed_object))


class DirectorTestCase(TestCase):
    """
    Unit testing class for the Director class
    """

    def setUp(self):
        """
        Initialize testing data.
        """

        class Building(object):
            def __init__(self):
                self.floor = None
                self.size = None

            def __repr__(self):
                return 'Floor: {0.floor} | Size: {0.size}'.format(self)

        class HomeBuilder(Builder, metaclass=ABCMeta):
            def __init__(self):
                super().__init__(Building())
                self._register('floor', self._build_floor)
                self._register('size', self._build_size)

            @abstractmethod
            def _build_floor(self):
                pass

            @abstractmethod
            def _build_size(self):
                pass

        class HouseBuilder(HomeBuilder):
            def _build_floor(self):
                self.constructed_object.floor = 'One'

            def _build_size(self):
                self.constructed_object.size = 'Big'

        class FlatBuilder(HomeBuilder):
            def _build_floor(self):
                self.constructed_object.floor = 'More than one'

            def _build_size(self):
                self.constructed_object.size = 'Small'

        class HomeDirector(Director):
            def construct(self):
                self.builder.build('floor')
                self.builder.build('size')

        self.house_builder = HouseBuilder()
        self.flat_builder = FlatBuilder()
        self.home_director = HomeDirector()

    def test_construct(self):
        """
        Test the construct method.

        @raise AssertionError: If the test fails.
        """
        self.home_director.builder = self.house_builder
        self.home_director.construct()
        house = self.home_director.get_constructed_object()
        self.assertEquals('One', house.floor)
        self.assertEquals('Big', house.size)
        self.assertEquals('Floor: One | Size: Big', str(house))

        self.home_director.builder = self.flat_builder
        self.home_director.construct()
        flat = self.home_director.get_constructed_object()
        self.assertEquals('More than one', flat.floor)
        self.assertEquals('Small', flat.size)
        self.assertEquals('Floor: More than one | Size: Small', str(flat))
