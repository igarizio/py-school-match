"""This module implements the algorithm *'Non-stable improvement
cycles'*. This means, it applies *'Deferred Acceptance with single
tie breaking'*, and then searches for non-stable cycles.
"""

from py_school_match.algorithms.abstract_matching_algorithm import AbstractMatchingAlgorithm
from py_school_match.algorithms.da_stb import DASTB
from py_school_match.algorithms.pi import PI


class NSIC(AbstractMatchingAlgorithm):
    """This class implements the 'Non-stable improvement
    cycles'* algorithm.

    This takes a list of students, a list of schools and a ruleset
    (which is used to calculate 'a priori' priorities). First it applies
    :class:`.DASTB`, and then :class:`.PI`.
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
        PI(stable_improvements=False, *self.args, **self.kwargs).run(students, schools, ruleset)
