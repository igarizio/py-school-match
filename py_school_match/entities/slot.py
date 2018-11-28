"""This module defines a slot."""

from itertools import groupby


class Slot:
    """This class defines a slot.
    A slot is used to store and prioritize students
    inside a school.
    """

    def __init__(self, rule, capacity):
        """Initializes a slot.

        :param rule: The rule used in the slot.
        :type rule: :class:`.Rule`..
        :param capacity: The slot capacity.
        :type capacity: int.
        """
        self.rule = rule
        self.capacity = capacity
        self.queue = []

    def is_general_slot(self):
        """If the slot has no rule attached."""
        return self.rule is None

    def is_quoted_slot(self):
        """If the slot has a quota."""
        return not self.is_general_slot()

    def append(self, student):
        """Appends a student to the slot."""
        self.queue.append(student)

    def sort_slot(self, get_priority):  # ToDo: Optimize insert + sort (the list is already sorted before the insert).
        """Sorts the slot according to the rules."""
        self.queue.sort(key=lambda student: get_priority(self, student), reverse=True)

    def gen_indifference_groups(self, get_priority):
        """Generates groups where all students have the same priority."""
        self.sort_slot(get_priority)
        groups = groupby(self.queue, key=lambda student: get_priority(self, student))
        groups_values = [[item for item in data] for (key, data) in groups]
        return groups_values

    def pop_rejected(self):
        """Removes rejected students from the slot."""
        if len(self.queue) > self.capacity:
            rejected = self.queue[-1]
            del self.queue[-1]
            return rejected
        else:
            return None

