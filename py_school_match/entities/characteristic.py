"""This module defines a characteristic.
The goal of a characteristic is to relate a criteria
and a value."""


class Characteristic:
    """This class define a characteristic.

    Characteristics are used to define which criteria
    does a student have (and what value does it contain).
    """

    def __init__(self, criteria, value, recognized_only_in=None):
        """Initializes a characteristic.

        :param criteria: A criteria.
        :type criteria: :class:`.Criteria`.
        :param value: The value associated with the criteria.
        :type value: Any.
        :param recognized_only_in: Where the characteristic is valid.
        :type recognized_only_in: list
        """
        self.criteria = criteria
        self.value = value

        self.__recognized_in = [recognized_only_in] if recognized_only_in is not None else []

    @property
    def recognizers(self):
        return self.__recognized_in

    def is_recognized_in(self, school):
        """Checks if the characteristic is recognized in the school.
        If the characteristic does not have any recognizer specified,
        the characteristic is recognized at every school."""
        return school in self.__recognized_in or not self.__recognized_in

    def add_recognizer(self, recognizer):
        """Adds a school where the characteristic is recognized."""
        self.__recognized_in.append(recognizer)
