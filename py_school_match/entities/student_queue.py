"""This module defines a queue of students."""

from math import ceil

from py_school_match.entities.slot import Slot


class StudentQueue:
    """This class defines a queue of students."""

    def __init__(self, school, preference_mode=False):
        """Initializes the queue.

        :param school: The school associated.
        :type school: :class:`.School`..
        :param preference_mode: If True, ignores all quotas and capacities.
        It is used to model preferences.
        :type preference_mode: bool.
        """
        self.slot_queue = []
        self.school = school
        self.rejected_student = None

        self.preference_mode = preference_mode

        self.define_slots()

    def get_all_students(self):
        """Returns all the students associated."""
        assigned_students = []
        for slot in self.slot_queue:
            assigned_students.extend([student for student in slot.queue])

        return assigned_students

    def define_slots(self):
        """Creates the slots associated."""
        capacity_used = 0
        if self.school.get_ruleset() and not self.preference_mode:
            for rule in self.school.get_ruleset().get_rules_prioritized():
                if rule.has_quota():
                    slot_size = ceil(rule.quota*self.school.capacity)
                    self.slot_queue.append(Slot(rule, slot_size))
                    capacity_used += slot_size

        self.slot_queue.append(Slot(None, self.school.capacity - capacity_used))

    def append(self, student):
        """Appends a student to the queue."""

        unassigned_student = student
        for slot in self.slot_queue:

            if slot.is_general_slot():
                self.assign_to_slot(slot, unassigned_student)
                unassigned_student = slot.pop_rejected() if not self.preference_mode else None

            elif slot.rule.has_flexible_quota() or slot.rule.criteria in unassigned_student.get_characteristics():
                self.assign_to_slot(slot, unassigned_student)
                unassigned_student = slot.pop_rejected() if not self.preference_mode else None

            self.rejected_student = unassigned_student

            if unassigned_student is None:
                break

    def assign_to_slot(self, slot, unassigned_student):  # ToDo: Possibly move this method to Slot
        """Assigns a student to a slot."""
        slot.append(unassigned_student)
        slot.sort_slot(self.get_priority)

    def get_priority(self, slot, student):
        """Returns the priority of the student inside a slot."""
        priorities = ()
        priority_rules = []

        if self.preference_mode:
            priority_rules = self.school.get_ruleset().get_rules_prioritized()
        else:
            for rule in self.school.get_ruleset().get_rules_prioritized():
                if not rule.has_quota() or (rule == slot.rule and slot.is_quoted_slot() and slot.rule.has_flexible_quota()):
                    priority_rules.append(rule)

        for rule in priority_rules:
            characteristic_group = student.get_characteristic(rule.criteria)  # ToDo: Find a better name for characteristic_group
            if characteristic_group:                                          # It is actually a group of characteristics.
                for characteristic in characteristic_group:
                    if characteristic.is_recognized_in(self.school):
                        rule_priority = self.evaluate_characteristic(characteristic)

                        priorities += (rule_priority,)
                        break
            else:
                priorities += (False,)

        return priorities

    def evaluate_characteristic(self, characteristic):
        """Evaluates a characteristic according to it's criteria associated."""
        if characteristic.criteria.criteria_type == list:
            rule_priority = self.school in characteristic.value
        elif characteristic.criteria.criteria_type == bool:
            rule_priority = characteristic.value
        elif characteristic.criteria.criteria_type == int:
            rule_priority = characteristic.value
        else:
            rule_priority = False

        return rule_priority

    def gen_indifference_groups(self):
        """Returns groups of students with the same priority."""
        groups = []
        for slot in self.slot_queue:
            groups.extend(slot.gen_indifference_groups(self.get_priority))
        return groups

    def get_rejected_student(self):
        """Returns a rejected student (if any)."""
        return self.rejected_student
