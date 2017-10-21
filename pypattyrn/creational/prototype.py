from copy import deepcopy
from types import MethodType


class Prototype(object):
    """
    Prototype design pattern abstract class.

    - External Usage documentation: U{https://github.com/tylerlaberge/PyPattyrn#prototype-pattern}
    - External Prototype Pattern documentation: U{https://en.wikipedia.org/wiki/Prototype_pattern}
    """
    def prototype(self, **attributes):
        """
        Copy the prototype this object and optionally update attributes.

        @param attributes: Keyword arguments of any attributes you wish to update.
        @return: A copy of this object with the updated attributes.
        """
        obj = deepcopy(self)
        for attribute in attributes:
            if callable(attributes[attribute]):
                setattr(obj, attribute, MethodType(attributes[attribute], obj))
            else:
                setattr(obj, attribute, attributes[attribute])

        return obj
