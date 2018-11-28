"""This module defines a social planner."""
from py_school_match.entities.ruleset import RuleSet

class SocialPlanner:
    """This class defines a social planner. 
    A social planner is used to run a algorithm
    using a group of students, a group of schools
    and a set of rules.
    """

    def __init__(self, students, schools, ruleset=None):
        """Initializes a slot.

        :param students: A list of students.
        :type students: list.
        :param schools: A list of school
        :type schools: list.
        :param ruleset: The set of rules. By default, it uses the
        same ruleset in every school.
        :type ruleset: :class:`.Ruleset`.
        """
        self.students = students
        self.schools = schools
        self.ruleset = ruleset if ruleset else RuleSet()

        self.assign_same_ruleset()  # By default it assigns the same ruleset to every school.

    def assign_same_ruleset(self):
        """Assigns the same ruleset to every school."""
        for school in self.schools:
            school.set_ruleset_n_reset(self.ruleset)  # ToDo: The assignation should update itself!

    def run_matching(self, algorithm):
        """Run the algorithm."""
        algorithm.run(self.students, self.schools, self.ruleset)

    @staticmethod
    def change_ruleset(school, ruleset):
        """Changes the ruleset used in a school."""
        school.ruleset = ruleset
        school.reset_assignation()
