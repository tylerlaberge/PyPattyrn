class Composite(object):
    """
    Composite class as part of the Composite pattern.

    - External Usage Documentation: U{https://github.com/tylerlaberge/PyPattyrn#composite-pattern}
    - External Composite Pattern documentation: U{https://en.wikipedia.org/wiki/Composite_pattern}
    """
    def __init__(self, interface):
        """
        Initialize a new Composite instance.

        @param interface: The interface the all child components must adhere to when added to this composite.
        @type interface: class
        """
        self.components = set()
        self.interface = interface

    def add_component(self, component):
        """
        Add a component to this composite.

        @param component: The component to add to this Composite
        @raise AttributeError: If the component does not adhere to this Composites interface.
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

    def _delegate(self, func_name):
        """
        Apply a function to all child components by function name.

        @param func_name: The name of the function to call with all child components.
        @type func_name: str
        @raise AttributeError: If a child component does not have a callable function with the given name.
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
        return lambda: self._delegate(item)
