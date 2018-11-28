"""This module defines a rule."""


class Rule:
    """This class defines rule. 
    A rule is used to determine the priority
    of a student.
    """

    def __init__(self, criteria, quota=1, strict_quota=False):
        """Initializes a rule.

        :param criteria: The criteria this rule checks.
        :type criteria: :class:`.Criteria`.
        :param quota: The minimum percentage a school can have of
        students with the selected criteria.
        :type quota: float.
        :param strict_quota: Whether the quota is strict or flexible.
        A flexible quota means that if there are no more students
        with the selected criteria left, the school can accept
        other students.
        :type strict_quota: bool.
        """
        self.criteria = criteria
        self.quota = quota
        self.strict_quota = strict_quota

    def has_quota(self):
        """If the rule has a quota associated."""
        return self.quota < 1

    def has_strict_quota(self):
        """If the rule has a strict quota associated."""
        return self.quota < 1 and self.strict_quota

    def has_flexible_quota(self):
        """If the rule has a flexible quota associated."""
        return not self.has_strict_quota()


