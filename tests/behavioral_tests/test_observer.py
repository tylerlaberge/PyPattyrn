from unittest import TestCase
from pypattyrn.behavioral.observer import Observer, Observable


class ObserverTestCase(TestCase):
    """
    Unit testing class for the Observer class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class ConcreteObserver(Observer):

            updated_state = None

            def update(self, **state):
                self.updated_state = state

        self.observer = ConcreteObserver()

    def test_update(self):
        """
        Test the update method.

        @raise AssertionError: If the test fails.
        """
        state = {'foo': 'test1', 'bar': 'test2'}
        self.observer.update(**state)

        self.assertEquals(state, self.observer.updated_state)


class ObservableTestCase(TestCase):
    """
    Unit testing class for the Observable class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class ConcreteObservable(Observable):
            _kinda_private_var = 'I am kinda private'
            __private_var = True

            def change_state(self, **kwargs):
                for key, value in kwargs.items():
                    setattr(self, key, value)

                self.notify()

        class ConcreteObserver(Observer):

            updated_state = None

            def update(self, **state):
                self.updated_state = state

        self.observer_class = ConcreteObserver
        self.observable_class = ConcreteObservable

    def test_attach(self):
        """
        Test the attach method.

        @raise AssertionError: If the test fails.
        """
        observable = self.observable_class()
        observer_1 = self.observer_class()
        observer_2 = self.observer_class()
        observer_3 = self.observer_class()

        observable.attach(observer_1)
        observable.attach(observer_2)
        observable.attach(observer_3)

        try:
            observable.attach(observer_1)
        except:
            raise AssertionError
        else:
            self.assertEquals({observer_1, observer_2, observer_3}, observable._observers)

    def test_detach(self):
        """
        Test the detach method.

        @raise AssertionError: If the test fails.
        """
        observable = self.observable_class()
        observer_1 = self.observer_class()
        observer_2 = self.observer_class()
        observer_3 = self.observer_class()
        observer_unattached = self.observer_class()

        observable.attach(observer_1)
        observable.attach(observer_2)
        observable.attach(observer_3)

        observable.detach(observer_1)
        observable.detach(observer_2)
        observable.detach(observer_3)

        try:
            observable.detach(observer_unattached)
        except:
            raise AssertionError
        else:
            self.assertEquals(set(), observable._observers)

    def test_notify(self):
        """
        Test the notify method.

        @raise AssertionError: If the test fails.
        """
        observable = self.observable_class()
        observer_1 = self.observer_class()
        observer_2 = self.observer_class()
        observer_3 = self.observer_class()

        observable.attach(observer_1)
        observable.attach(observer_2)
        observable.attach(observer_3)

        observable.change_state(public_state={'foo': 'test1', 'bar': 'test2'}, foo='foo', bar=False)
        expected_state = {'public_state': {'foo': 'test1', 'bar': 'test2'}, 'foo': 'foo', 'bar': False}

        self.assertDictEqual(expected_state, observer_1.updated_state)
        self.assertDictEqual(expected_state, observer_2.updated_state)
        self.assertDictEqual(expected_state, observer_3.updated_state)

        observable.change_state(bar='bar')
        expected_state_2 = {'public_state': {'foo': 'test1', 'bar': 'test2'}, 'foo': 'foo', 'bar': 'bar'}

        self.assertDictEqual(expected_state_2, observer_1.updated_state)
        self.assertDictEqual(expected_state_2, observer_2.updated_state)
        self.assertDictEqual(expected_state_2, observer_3.updated_state)

