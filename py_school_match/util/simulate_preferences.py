from random import normalvariate, uniform, seed

from py_school_match.util.stat import get_variance


def simulate_preferences(students, schools, alpha, n_pref_probabilities, schools_factors=None):
    gen_utilities = {}
    for index, school in enumerate(schools):
        gen_utilities[school] = normalvariate(0, 1) if not schools_factors else schools_factors[index]

    for student in students:
        std_utilities = {}
        variance = 1 if not schools_factors else get_variance(schools_factors)
        for school in schools:
            std_utilities[school] = normalvariate(0, variance**0.5) * (1 - alpha) + gen_utilities[school] * alpha

        pref = sorted(std_utilities.keys(), key=lambda s: std_utilities[s], reverse=True)

        n_pref = weighted_choice([(v+1, p) for v, p in enumerate(n_pref_probabilities)])
        student.preferences = pref[:n_pref]


def weighted_choice(choices):
    total = sum(w for c, w in choices)
    r = uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w >= r:
            return c
        upto += w
    assert False, "Should not get here"
