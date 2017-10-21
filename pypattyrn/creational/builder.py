from abc import ABCMeta, abstractmethod


class Director(object, metaclass=ABCMeta):
    """
    Abstract director class, responsible for using a builder to fully construct an object.

    - External Usage documentation: U{https://github.com/tylerlaberge/PyPattyrn#builder-pattern}
    - External Builder Pattern documentation: U{https://en.wikipedia.org/wiki/Builder_pattern}
    """

    def __init__(self):
        """
        Initialize a new Director.
        """
        self.builder = None

    @abstractmethod
    def construct(self):
        """
        Abstract method for fully constructing an object.

        Concrete implementations should override this and use a builder to construct the object.

        @raise NotImplementedError: If this method is not overridden.
        """
        pass

    def get_constructed_object(self):
        """
        Get the object this director is responsible for constructing.

        @return: The object that this director is responsible for constructing.
        """
        return self.builder.constructed_object


class Builder(object, metaclass=ABCMeta):
    """
    Abstract builder class, responsible for constructing various pieces of an object.

    - External Usage documentation: U{https://github.com/tylerlaberge/PyPattyrn#builder-pattern}
    - External Builder Pattern documentation: U{https://en.wikipedia.org/wiki/Builder_pattern}
    """

    def __init__(self, constructed_object):
        """
        Initialize a new Builder.

        Concrete Builders should call this method from within their own __init__ method.
        The concrete __init__ method should also register all build options to build methods,
        by using the _register method.

        @param constructed_object: An instance of an object this builder is responsible for.
        """
        self.constructed_object = constructed_object
        self.build_methods = dict()

    def build(self, build_option, **kwargs):
        """
        Build a piece of the constructed object.

        @param build_option: The part of the object to build. All build options should have been registered in __init__.
        @type build_option: str
        @param kwargs: Additional arguments for building.
        """
        self.build_methods[build_option](**kwargs)

    def _register(self, build_option, build_method):
        """
        Register a build option to a build method.

        All concrete builders should call this method in their constructor at least once.

        @param build_option: A string representing the part of the object to build.
        @type build_option: str
        @param build_method: The method to call when given build option is selected.
        """
        self.build_methods[build_option] = build_method
