"""This module defines a school."""

from itertools import count

from py_school_match.entities.student_queue import StudentQueue


class School:
    """This class defines school."""

    __id_counter = count(0)
    """This is used to generate an incremental id."""

    def __init__(self, capacity, id_=""):
        """Initializes a school.

        :param capacity: The maximum number of students.
        :type capacity: int.
        :param id_: Any unique identifier.
        :type id_: Any.
        """
        self.id = id_ if id_ else next(School.__id_counter)
        self.capacity = capacity

        self.ruleset = None
        self.assignation = StudentQueue(self)

    def reset_assignation(self):
        """Resets the assignations of the school."""
        self.assignation = StudentQueue(self)

    def set_ruleset_n_reset(self, ruleset):
        """Sets a new ruleset and resets the school's assignation."""
        self.ruleset = ruleset
        self.reset_assignation()

    def set_ruleset(self, ruleset):
        """Sets a new ruleset to the school."""
        self.ruleset = ruleset

    def get_ruleset(self):
        """Returns the school's ruleset."""
        return self.ruleset

    @staticmethod
    def reset_ids():
        """Resets the incremental id."""
        School.__id_counter = count(0)
