"""This module implements the algorithm *'Deferred Acceptance with
multiple tie breaking'*.
This implementation is based on Erdil and Ergin (2006)."""

import random

from py_school_match.entities.characteristic import Characteristic
from py_school_match.entities.criteria import Criteria
from py_school_match.algorithms.da import DA
from py_school_match.entities.rule import Rule

from py_school_match.algorithms.abstract_matching_algorithm import AbstractMatchingAlgorithm


class DAMTB(AbstractMatchingAlgorithm):
    """This class implements the *'Deferred Acceptance with multiple
    tie breaking'* algorithm.

    This takes a list of students, a list of schools and a ruleset
    (which is used to calculate 'a priori' priorities), and adds a 'lottery'
    tickets (for each student 'proposing' to each school) as an additional rule.
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

        self.break_ties(students, schools)
        DA().run(students, schools, ruleset)

        ruleset.remove_rule(lottery_rule)

    def break_ties(self, students, schools):
        """This breaks priority ties by assigning lottery tickets.
        
        Each student is given one lottery ticket for each school he 'proposes' to.
        This ticket is created as a :class:`.Characteristic`, which is
        only valid in the respective school.
        """

        for school in schools:
            setattr(school, 'applying_students', [])

        for student in students:
            for pref_school in student.preferences:
                pref_school.applying_students.append(student)

        for school in schools:
            n_applications = len(school.applying_students)
            tickets = random.sample(range(n_applications), n_applications)
            for index, student in enumerate(school.applying_students):
                characteristic = Characteristic(self.lottery, tickets[index], recognized_only_in=school)
                student.add_characteristic(characteristic)
