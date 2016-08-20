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

        class ProxyCar(Proxy):

            def __init__(self, subject, driver):
                super().__init__(subject)
                self.driver = driver

            def drive_car(self):
                if self.driver.age > 16:
                    return self._subject.drive_car()
                else:
                    return 'Driver is too young to drive'

        self.proxy = ProxyCar(Car(), Driver(17))

    def test_drive_car(self):
        """
        Test the proxy with the drive car method.

        @raise AssertionError: If the test fails.
        """
        self.assertEqual('drive car', self.proxy.drive_car())
        self.proxy.driver.age = 15
        self.assertEqual('Driver is too young to drive', self.proxy.drive_car())
