from random import random, choice, seed

from py_school_match.entities.characteristic import Characteristic


def simulate_characteristics(students, schools, criteria_prob):
    for student in students:
        # This is VERY important, as the criteria_prob is a dict, any difference in this order is will be reflected in other random values
        sorted_criteria_prob = sorted(criteria_prob, key=lambda c: criteria_prob[c])

        for criteria in sorted_criteria_prob:
            if random() < criteria_prob[criteria]:
                value = True if criteria.criteria_type == bool else [choice(schools)]

                characteristic = Characteristic(criteria, value)
                student.add_characteristic(characteristic)