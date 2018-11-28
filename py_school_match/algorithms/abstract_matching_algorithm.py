"""This module defines an abstract class for other algorithms."""

from abc import ABCMeta, abstractmethod


class AbstractMatchingAlgorithm(metaclass=ABCMeta):
    """Abstract class for matching algorithms.
    Defined, using ABCMeta.
    """

    @abstractmethod
    def run(self, students, schools, ruleset):
        """
        Abstract method algorithms should implement.
        
        :param students: List of students.
        :type students: list
        :param schools: List of schools.
        :type schools: list
        :param ruleset: The ruleset to be used.
        :type ruleset: Ruleset
        """
        pass


