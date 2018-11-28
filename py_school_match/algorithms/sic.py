"""This module implements the algorithm *'Stable Improvements Cycles'*.
This implementation is based on Erdil and Ergin (2006)."""

from py_school_match.algorithms.abstract_matching_algorithm import AbstractMatchingAlgorithm
from py_school_match.algorithms.da_stb import DASTB
from py_school_match.algorithms.pi import PI


class SIC(AbstractMatchingAlgorithm):
    """This class implements *Stable Improvements Cycles*.

    This takes a list of students, a list of schools and a ruleset
    (which is used to calculate priorities).
    First, it creates an assignation based on :class:`.DASTB`, and then
    it searches cycles with :class:`.PI`.
    """

    def __init__(self, *args, **kwargs):
        """Saves arguments for :class:`.PI`.

        :param kwargs: Arguments for :class:`.PI`
        """
        self.args = args
        self.kwargs = kwargs

    def run(self, students, schools, ruleset):
        """Runs the algorithm.

        :param students: List of students.
        :type students: list
        :param schools: List of school.
        :type schools: list
        :param ruleset: Set of rules used.
        :type ruleset: Ruleset
        """
        DASTB().run(students, schools, ruleset)
        PI(stable_improvements=True, *self.args, **self.kwargs).run(students, schools, ruleset)
