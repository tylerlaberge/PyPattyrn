

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
        self._method_names = [method for method in dir(interface) if callable(getattr(interface, method))]

    def add_component(self, component):
        """
        Add a component to this composite.

        @param component: The component to add to this Composite
        """
        component_methods = [method for method in dir(component) if callable(getattr(component, method))]
        for method_name in self._method_names:
            if method_name in component_methods:
                continue
            else:
                raise AttributeError
        else:
            self.components.add(component)

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
