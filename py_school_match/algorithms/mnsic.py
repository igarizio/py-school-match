"""This module implements the algorithm *'Deferred Acceptance with
multiple tie breaking'*, and then searches for non stable cycles.
.. DANGER::
   Be careful when running this algorithm. This algorithm
   tend to generate a large number of possible improvements,
   and this may consume all RAM available. See :class:`.PI`
   for a solution.
"""

from py_school_match.algorithms.abstract_matching_algorithm import AbstractMatchingAlgorithm
from py_school_match.algorithms.da_mtb import DAMTB
from py_school_match.algorithms.pi import PI


class MNSIC(AbstractMatchingAlgorithm):
    """This class implements the *'Deferred Acceptance with multiple
    tie breaking'* algorithm, and then searches for non stable
    improvement cycles.

    This takes a list of students, a list of schools and a ruleset
    (which is used to calculate 'a priori' priorities). First it applies
    :class:`.DAMTB`, and then :class:`.PI`.
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
        DAMTB().run(students, schools, ruleset)
        PI(stable_improvements=False, *self.args, **self.kwargs).run(students, schools, ruleset)
