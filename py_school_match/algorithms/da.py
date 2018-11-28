"""This module implements the *'Deferred Acceptance'* algorithm.
This algorithm comes from Gale and Shapley (1962), and the
implementation is based on Erdil and Ergin (2006)."""

from py_school_match.algorithms.abstract_matching_algorithm import AbstractMatchingAlgorithm


class DA(AbstractMatchingAlgorithm):
    """This class implements the *Deferred Acceptance* algorithm.
    
    This takes a list of students, a list of schools and a ruleset
    (which is used to calculate priorities).
    This works by 'proposing' students to their most preferred
    (and available) school. Schools, on the other hand, accept
    or reject these students based on their priority.
    """

    def run(self, students, schools, ruleset):
        """Runs the *Deferred Acceptance* algorithm.

        :param students: List of students.
        :type students: list
        :param schools: List of school.
        :type schools: list
        :param ruleset: Set of rules used.
        :type ruleset: Ruleset
        """
        for student in students:
            setattr(student, 'option_n', 0)
            setattr(student, 'assigned', False)

        still_free_students = True
        while still_free_students:

            still_free_students = False
            for student in students:

                if not student.assigned:
                    pref_school = student.preferences[student.option_n]
                    DA.assign_student(student, pref_school)

                    rejected_student = pref_school.assignation.get_rejected_student()

                    if rejected_student:
                        rejected_student.option_n += 1

                        if rejected_student.option_n < len(rejected_student.preferences):
                            DA.unassign_student(rejected_student)
                            still_free_students = True
                        else:
                            DA.definitely_unassign_student(rejected_student)

    @staticmethod
    def assign_student(student, school):
        """Assigns a student to a school."""
        student.assigned_school = school
        student.assigned = True
        school.assignation.append(student)

    @staticmethod
    def unassign_student(student):
        """Unassigns a student to a school."""
        student.assigned = False
        student.assigned_school = None

    @staticmethod
    def definitely_unassign_student(student):
        """Sets a student as rejected by all schools."""
        student.assigned = True
        student.assigned_school = None
