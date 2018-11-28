"""This module defines a criteria."""


class Criteria:
    """This class defines a criteria.
    The goal of a criteria is to associate an adjective
    and a value type.
    """

    def __init__(self, name, criteria_type):
        """Initializes a characteristic.

        :param name: The adjective's name.
        :type name: str.
        :param criteria_type: The type of the adjective
        :type criteria_type: type.
        """
        self.name = name
        self.criteria_type = criteria_type
