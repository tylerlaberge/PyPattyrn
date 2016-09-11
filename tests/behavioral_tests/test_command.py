from unittest import TestCase

from pypattyrn.behavioral.command import Receiver, Command, Invoker


class ReceiverTestCase(TestCase):
    """
    Unit testing class for the Receiver class.
    """

    def setUp(self):
        """
        Initialize testing data.
        """

        class Thermostat(Receiver):
            def raise_temp(self, amount):
                return "Temperature raised by {0} degrees".format(amount)

            def lower_temp(self, amount):
                return "Temperature lowered by {0} degrees".format(amount)

        self.thermostat = Thermostat()

    def test_valid_action(self):
        """
        Test the action method with a valid action.

        @raise AssertionError: If the test fails.
        """
        self.assertEquals("Temperature raised by 5 degrees", self.thermostat.action('raise_temp', 5))
        self.assertEquals("Temperature lowered by 5 degrees", self.thermostat.action('lower_temp', 5))

    def test_invalid_action(self):
        """
        Test the action method with an invalid action.

        @raise AssertionError: If the test fails.
        """
        with self.assertRaises(AttributeError):
            self.thermostat.action('foo')


class CommandTestCase(TestCase):
    """
    Unit testing class for the Command class.
    """

    def setUp(self):
        """
        Initialize testing data.
        """

        class Thermostat(Receiver):
            def raise_temp(self, amount):
                return "Temperature raised by {0} degrees".format(amount)

            def lower_temp(self, amount):
                return "Temperature lowered by {0} degrees".format(amount)

        class RaiseTempCommand(Command):
            def __init__(self, receiver, amount=5):
                super().__init__(receiver)
                self.amount = amount

            def execute(self):
                return self._receiver.action('raise_temp', self.amount)

            def unexecute(self):
                return self._receiver.action('lower_temp', self.amount)

        class LowerTempCommand(Command):
            def __init__(self, receiver, amount=5):
                super().__init__(receiver)
                self.amount = amount

            def execute(self):
                return self._receiver.action('lower_temp', self.amount)

            def unexecute(self):
                return self._receiver.action('raise_temp', self.amount)

        self.thermostat = Thermostat()
        self.raise_temp_command_class = RaiseTempCommand
        self.lower_temp_command_class = LowerTempCommand

    def test_execute(self):
        """
        Test the execute method.

        @raise AssertionError: If the test fails.
        """
        raise_temp_command = self.raise_temp_command_class(self.thermostat, 10)
        lower_temp_command = self.lower_temp_command_class(self.thermostat, 5)

        self.assertEquals("Temperature raised by 10 degrees", raise_temp_command.execute())
        self.assertEquals("Temperature lowered by 5 degrees", lower_temp_command.execute())


class InvokerTestCase(TestCase):
    """
    Unit testing class for the Invoker class.
    """

    def setUp(self):
        """
        Initialize testing data.
        """

        class Thermostat(Receiver):
            def raise_temp(self, amount):
                return "Temperature raised by {0} degrees".format(amount)

            def lower_temp(self, amount):
                return "Temperature lowered by {0} degrees".format(amount)

        class RaiseTempCommand(Command):
            def __init__(self, receiver, amount=5):
                super().__init__(receiver)
                self.amount = amount

            def execute(self):
                return self._receiver.action('raise_temp', self.amount)

            def unexecute(self):
                return self._receiver.action('lower_temp', self.amount)

        class LowerTempCommand(Command):
            def __init__(self, receiver, amount=5):
                super().__init__(receiver)
                self.amount = amount

            def execute(self):
                return self._receiver.action('lower_temp', self.amount)

            def unexecute(self):
                return self._receiver.action('raise_temp', self.amount)

        class Worker(Invoker):
            def __init__(self):
                super().__init__([LowerTempCommand, RaiseTempCommand])

        self.worker = Worker()
        self.receiver = Thermostat()
        self.lower_temp_command = LowerTempCommand(self.receiver)
        self.raise_temp_command = RaiseTempCommand(self.receiver)

    def test_valid_execute(self):
        """
        Test the execute method with a valid command for the Worker Invoker.

        @raise AssertionError: If the test fails.
        """
        self.assertEquals("Temperature lowered by 5 degrees", self.worker.execute(self.lower_temp_command))
        self.assertEquals("Temperature raised by 5 degrees", self.worker.execute(self.raise_temp_command))

    def test_invalid_execute(self):
        """
        Test the execute method with an invalid command for the Worker Invoker.

        @raise AssertionError: If the test fails.
        """

        class Light(Receiver):
            def turn_on(self):
                return "Light turned on"

            def turn_off(self):
                return "Light turned off"

        class TurnOnLightCommand(Command):
            def execute(self):
                return self._receiver.action('turn_on')

            def unexecute(self):
                return self._receiver.action('turn_off')

        with self.assertRaises(AttributeError):
            self.worker.execute(TurnOnLightCommand(Light))

    def test_undo(self):
        """
        Test the undo method.

        @raise AssertionError: If the test fails.
        """
        self.worker.execute(self.raise_temp_command)

        self.assertIn(self.raise_temp_command, self.worker._history)
        self.assertEquals("Temperature lowered by 5 degrees", self.worker.undo())
        self.assertNotIn(self.raise_temp_command, self.worker._history)
