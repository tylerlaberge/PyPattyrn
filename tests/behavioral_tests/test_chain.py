from unittest import TestCase

from pypattyrn.behavioral.chain import ChainLink, Chain


class ChainLinkTestCase(TestCase):
    """
    Unit testing class for the ChainLink class.
    """

    def setUp(self):
        """
        Initialize testing data.
        """

        class ConcreteChainLinkThree(ChainLink):

            def handle(self, request):
                if request == 'handle_three':
                    return "Handled in chain link three"
                else:
                    return self.successor_handle(request)

        class ConcreteChainLinkTwo(ChainLink):

            def __init__(self):
                super().__init__()
                self.set_successor(ConcreteChainLinkThree())

            def handle(self, request):
                if request == 'handle_two':
                    return "Handled in chain link two"
                else:
                    return self.successor_handle(request)

        class ConcreteChainLinkOne(ChainLink):

            def __init__(self):
                super().__init__()
                self.set_successor(ConcreteChainLinkTwo())

            def handle(self, request):
                if request == 'handle_one':
                    return "Handled in chain link one"
                else:
                    return self.successor_handle(request)

        self.chain_link_one_class = ConcreteChainLinkOne

    def test_success_handle(self):
        """
        Test the handle method with successful requests.

        @raise AssertionError: If the test fails.
        """
        handler = self.chain_link_one_class()

        self.assertEquals("Handled in chain link one", handler.handle("handle_one"))
        self.assertEquals("Handled in chain link two", handler.handle("handle_two"))
        self.assertEquals("Handled in chain link three", handler.handle("handle_three"))

    def test_fail_handle(self):
        """
        Test the handle method with unsuccessful requests.

        @raise AssertionError: If the test fails.
        """
        handler = self.chain_link_one_class()
        with self.assertRaises(AttributeError):
            handler.handle("foo")


class ChainTestCase(TestCase):
    """
    Unit testing class for the Chain class.
    """

    def setUp(self):
        """
        Initialize testing data.
        """

        class ConcreteChainLinkThree(ChainLink):

            def handle(self, request):
                if request == 'handle_three':
                    return "Handled in chain link three"
                else:
                    return self.successor_handle(request)

        class ConcreteChainLinkTwo(ChainLink):

            def __init__(self):
                super().__init__()
                self.set_successor(ConcreteChainLinkThree())

            def handle(self, request):
                if request == 'handle_two':
                    return "Handled in chain link two"
                else:
                    return self.successor_handle(request)

        class ConcreteChainLinkOne(ChainLink):

            def __init__(self):
                super().__init__()
                self.set_successor(ConcreteChainLinkTwo())

            def handle(self, request):
                if request == 'handle_one':
                    return "Handled in chain link one"
                else:
                    return self.successor_handle(request)

        class ConcreteChain(Chain):

            def __init__(self):
                super().__init__(ConcreteChainLinkOne())

            def fail(self):
                return 'Fail'

        self.chain_class = ConcreteChain

    def test_success_handle(self):
        """
        Test the handle method with a successful request

        @raise AssertionError: If the test fails.
        """
        chain = self.chain_class()

        self.assertEquals("Handled in chain link one", chain.handle("handle_one"))
        self.assertEquals("Handled in chain link two", chain.handle("handle_two"))
        self.assertEquals("Handled in chain link three", chain.handle("handle_three"))

    def test_fail_handle(self):
        """
        Test the handle method with unsuccessful requests.

        @raise AssertionError: If the test fails.
        """
        chain = self.chain_class()

        self.assertEquals("Fail", chain.handle("foo"))
