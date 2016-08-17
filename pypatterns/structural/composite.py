class Composite(object):
    """
    Composite class as part of the Composite pattern.
    """
    def __init__(self, interface):
        """
        Initialize a new Composite instance.
        """
        self.components = set()
        self.interface = interface

    def add_component(self, component):
        """
        Add a component to this composite.

        @param component: The component to add to this Composite
        """
        valid = False
        try:
            if component.interface == self.interface:
                valid = True
        except AttributeError:
            if self.interface in component.__class__.__mro__:
                valid = True
        finally:
            if valid:
                self.components.add(component)
            else:
                raise AttributeError('Component {0} does not follow this composites interface {1}'.format(
                    component.__class__, self.interface))

    def remove_component(self, component):
        """
        Remove a component from this composite.

        @param component: The component to remove from this Composite.
        """
        try:
            self.components.remove(component)
        except KeyError:
            pass

    def delegate(self, func_name):
        """
        Apply a function to all child components by function name.

        @param func_name: The name of the function to call with all child components.
        @type func_name: str
        """
        for component in self.components:
            attribute = getattr(component, func_name)
            if callable(attribute):
                attribute()
            else:
                raise AttributeError()

    def __getattr__(self, item):
        """
        Override getattr to delegate all function calls to children.

        @param item: The function to call with this composites children components.
        @type item: str
        @return: A function that when called will call all child functions with the given function name.
        """
        return lambda: self.delegate(item)
