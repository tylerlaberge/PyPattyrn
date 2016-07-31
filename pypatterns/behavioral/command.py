from abc import ABCMeta, abstractmethod


class InvalidActionException(Exception):
    """
    Exception for when an invalid action is called on a Receiver.
    """
    pass


class InvalidInvokerCommandException(Exception):
    """
    Exception for when an invalid command is given to an Invoker to execute.
    """


class Receiver(object, metaclass=ABCMeta):
    """
    Abstract receiver class as part of the Command pattern.
    """
    def action(self, name, *args, **kwargs):
        """
        Delegates which method to be called for a desired action.

        @param name: The name of the action to execute.
        @type name: str
        @param args: Any arguments for the action.
        @param kwargs: Any keyword arguments for the action.
        """
        try:
            return getattr(self, name)(*args, **kwargs)
        except AttributeError:
            raise InvalidActionException


class Command(object, metaclass=ABCMeta):
    """
    Abstract Command class as part of the Command pattern.
    """
    def __init__(self, receiver):
        """
        Initialize a new command instance.

        @param receiver: The receiver for this command to use.
        @type receiver: Receiver
        """
        self._receiver = receiver

    @abstractmethod
    def execute(self):
        """
        Abstract method for executing an action.
        """
        pass

    @abstractmethod
    def unexecute(self):
        """
        Abstract method for unexecuting an action.
        """
        pass


class Invoker(object, metaclass=ABCMeta):
    """
    Abstract Invoker class as part of the Command pattern.
    """
    def __init__(self, valid_commands):
        """
        Initialize a new Invoker instance.

        @param valid_commands: A list of command classes this invoker can handle.
        """
        self._history = []
        self._valid_commands = valid_commands

    def execute(self, command):
        """
        Execute a command.

        @param command: A command for the invoker to execute.
        @type command: Command
        """
        if command.__class__ not in self._valid_commands:
            raise InvalidInvokerCommandException
        else:
            self._history.append(command)
            return command.execute()

    def undo(self):
        """
        Undo the last command.
        """
        return self._history.pop().unexecute()
