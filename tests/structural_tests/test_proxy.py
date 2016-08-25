from unittest import TestCase
from pypatterns.structural.proxy import Proxy


class ProxyTestCase(TestCase):
    """
    Unit testing class for the Proxy class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class Car(object):

            def drive_car(self):
                return 'drive car'

        class Driver(object):

            def __init__(self, age):
                self.age = age

        self.car = Car()
        self.driver = Driver(17)

    def test_valid_proxy(self):
        """
        Test a Proxy class following the same interface as the subject.

        @raise AssertionError: If the test fails.
        """
        class ProxyCar(Proxy):

            def __init__(self, subject, driver):
                super().__init__(subject)
                self.driver = driver

            def drive_car(self):
                if self.driver.age > 16:
                    return self._subject.drive_car()
                else:
                    return 'Driver is too young to drive'

        try:
            proxy = ProxyCar(self.car, self.driver)
        except AttributeError:
            raise AssertionError()
        else:
            self.assertEqual('drive car', proxy.drive_car())
            proxy.driver.age = 15
            self.assertEqual('Driver is too young to drive', proxy.drive_car())

    def test_invalid_proxy(self):
        """
        Test a Proxy class that is not following the same interface as the subject.

        @raise AssertionError: If the test fails.
        """
        class ProxyCar(Proxy):

            def __init__(self, subject, driver):
                super().__init__(subject)
                self.driver = driver

        self.assertRaises(AttributeError, lambda: ProxyCar(self.car, self.driver))
