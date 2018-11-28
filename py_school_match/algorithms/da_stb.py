"""This module implements the algorithm *'Deferred Acceptance 
with single tie breaking'*.
This implementation is based on Erdil and Ergin (2006)."""

import random

from py_school_match.entities.characteristic import Characteristic
from py_school_match.entities.criteria import Criteria
from py_school_match.entities.rule import Rule

from py_school_match.algorithms.abstract_matching_algorithm import AbstractMatchingAlgorithm
from py_school_match.algorithms.da import DA


class DASTB(AbstractMatchingAlgorithm):
    """This class implements the *'Deferred Acceptance with single
    tie breaking'* algorithm.

    This takes a list of students, a list of schools and a ruleset
    (which is used to calculate 'a priori' priorities), and adds a 'lottery'
    ticket to each student, as an additional rule.
    After this, it executes 'Deferred Acceptance' (from :class:`.DA`).
    """

    def __init__(self):
        """Adds a new :class:`.Criteria`"""
        self.lottery = Criteria("lottery", int)

    def run(self, students, schools, ruleset):
        """Runs the *Deferred Acceptance with multiple tie breaking* algorithm.

        :param students: List of students.
        :type students: list
        :param schools: List of school.
        :type schools: list
        :param ruleset: Set of rules used.
        :type ruleset: Ruleset
        """
        lottery_rule = Rule(self.lottery)
        ruleset.add_rule(lottery_rule)

        self.break_ties(students)
        DA().run(students, schools, ruleset)

        ruleset.remove_rule(lottery_rule)

    def break_ties(self, students):
        """This breaks priority ties by assigning lottery tickets.

        Each student is given one lottery ticket (this ticket is created
        as a :class:`.Characteristic`).
        """
        n_students = len(students)
        tickets = random.sample(range(n_students), n_students)

        for index, student in enumerate(students):
            student.add_characteristic(Characteristic(self.lottery, tickets[index]))


