from unittest import TestCase
from pypattyrn.structural.flyweight import FlyweightMeta


class FlyweightMetaTestCase(TestCase):
    """
    Unit testing class for the FlyweightMeta class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class Card(object, metaclass=FlyweightMeta):

            def __init__(self, suit, value):
                self.suit = suit
                self.value = value

        self.card_class = Card

    def test_flyweight(self):
        """
        Test that new objects with the same params are actually equal.

        @raise AssertionError: If the test fails.
        """
        three_of_spades = self.card_class('Spade', 3)
        four_of_spades = self.card_class('Spade', 4)
        three_of_spades_two = self.card_class('Spade', 3)

        self.assertEqual(id(three_of_spades), id(three_of_spades_two))
        self.assertNotEqual(id(three_of_spades), id(four_of_spades))
