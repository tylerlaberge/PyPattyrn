from abc import ABCMeta


class Proxy(object, metaclass=ABCMeta):
    """
    Base Proxy class as part of the Proxy design pattern.

    External Proxy Pattern documentation: U{https://en.wikipedia.org/wiki/Proxy_pattern}
    """
    def __init__(self, subject):
        """
        Initialize a new proxy instance.

        @param subject: The real subject this proxy calls upon.
        """
        self._subject = subject
        self._validate()

    def _validate(self):
        """
        Validate that the subject and this proxy follow the same interface.

        @raise AttributeError: If the subject and this proxy do not follow the same interface.
        """
        for attr in dir(self._subject):
            if attr.startswith('_') or attr.startswith('__'):
                continue

            elif not callable(getattr(self._subject, attr, None)) or not callable(getattr(self, attr, None)):
                raise AttributeError('Subject and Proxy must follow same interface')
