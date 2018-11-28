"""This module defines a ruleset."""


class RuleSet:
    """This class defines ruleset. 
    A ruleset is a set of rules which are prioritized.
    """

    def __init__(self, new_rules=None):
        """Initializes a ruleset.

        :param new_rules: A list of rules.
        :type new_rules: list.
        """
        self.rules = new_rules if new_rules else []

    def add_rule(self, rule):
        """Adds a rule from the ruleset."""
        self.rules.append(rule)

    def add_rule_in_position(self, rule, position):
        """Adds a rule from the ruleset."""
        self.rules.insert(position, rule)

    def remove_rule(self, rule):
        """Removes a rule from the ruleset."""
        self.rules.remove(rule)

    def get_rules_prioritized(self):
        """Returns the rules of the ruleset."""
        return self.rules



