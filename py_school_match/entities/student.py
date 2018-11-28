"""This module defines a student."""

from collections import defaultdict
from itertools import count


class Student:
    """This class defines a student."""

    __id_counter = count(0)
    """This is used to generate an incremental id."""

    def __init__(self, id_=""):
        """Initializes a student.

        :param id_: Any unique identifier.
        :type id_: Any.
        """
        self._id = id_ if id_ else next(Student.__id_counter)
        self.preferences = []

        self.__characteristics = defaultdict(list)

        self.assigned_school = None

    @property
    def id(self):
        return self._id

    @property
    def characteristics(self):
        """Returns a list of characteristics."""
        return self.__characteristics

    def add_characteristic(self, characteristic):
        """Adds a characteristic to the student."""
        self.__characteristics[characteristic.criteria].append(characteristic)

    def get_characteristic(self, criteria):
        """Returns a characteristic associated with a criteria."""
        if criteria in self.__characteristics:
            return self.__characteristics[criteria]
        else:
            return []

    @staticmethod
    def reset_ids():
        """Resets the incremental id."""
        Student.__id_counter = count(0)
