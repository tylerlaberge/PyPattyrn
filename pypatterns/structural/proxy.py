class Proxy(object):
    """
    Base Proxy class as part of the Proxy design pattern.
    """
    def __init__(self, subject):
        """
        Initialize a new proxy instance.

        @param subject: The real subject this proxy calls upon.
        """
        self._subject = subject







