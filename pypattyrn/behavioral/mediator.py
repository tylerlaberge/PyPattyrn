from collections import defaultdict


class Mediator(object):
    """
    Mediator class as part of the Mediator design pattern.

    - External Usage documentation: U{https://github.com/tylerlaberge/PyPattyrn#mediator-pattern}
    - External Mediator Pattern documentation: U{https://en.wikipedia.org/wiki/Mediator_pattern}
    """
    def __init__(self):
        """
        Initialize a new Mediator instance.
        """
        self.signals = defaultdict(list)

    def signal(self, signal_name, *args, **kwargs):
        """
        Send a signal out to all connected handlers.

        @param signal_name: The name of the signal.
        @type signal_name: Str
        @param args: Positional arguments to send with the signal.
        @param kwargs: Keyword arguments to send with the signal.
        """
        for handler in self.signals[signal_name]:
            handler(*args, **kwargs)

    def connect(self, signal_name, receiver):
        """
        Connect a receiver to a signal.

        @param signal_name: The name of the signal to connect the receiver to.
        @type signal_name: str
        @param receiver: A handler to call when the signal is sent out.
        """
        self.signals[signal_name].append(receiver)

    def disconnect(self, signal_name, receiver):
        """
        Disconnect a receiver from a signal.

        @param signal_name: The name of the signal to disconnect the receiver from.
        @type signal_name: str
        @param receiver: The receiver to disconnect from the signal.
        """
        try:
            self.signals[signal_name].remove(receiver)
        except ValueError:
            pass
