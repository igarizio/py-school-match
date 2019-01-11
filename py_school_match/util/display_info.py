"""This module implements methods to visualize
assignations easily
"""

from collections import defaultdict


def get_positions_stat(planner):
    """Returns a dictionary with positions as keys and student count as values."""
    ranking_stat = defaultdict(int)
    for student in planner.students:
        if student.assigned_school:
            ranking = student.preferences.index(student.assigned_school) + 1
            ranking_stat[ranking] += 1
        else:
            ranking_stat["NA"] += 1

    return ranking_stat


def display_assignation(positions):
    """Shows the assignation."""
    for r in positions:
        for s in range(positions[r]):
            if r != "NA":
                print(r + 1)
            else:
                print("NA")


def display_assignation_from_planner(planner):
    """Shows an assignation."""
    ranking_stat = get_positions_stat(planner)
    display_assignation(ranking_stat)


def display_positions(positions):
    """Shows the positions."""
    if "NA" in positions:
        print(positions["NA"], end=", ")
    else:
        print(0, end=", ")
    positions_n = [str(positions[r]) for r in positions if r != "NA"]

    print(", ".join(positions_n))


def display_positions_from_planner(planner):
    """Shows the positions."""
    ranking_stat = get_positions_stat(planner)
    display_positions(ranking_stat)


def save_positions(positions, algorithm, alpha, iteration, file="distribution.csv"):
    """Saves positions to a file. Algorithms, alpha and iteration are used as text."""
    positions_n = []

    if "NA" in positions:
        positions_n.append(positions["NA"])
        del positions["NA"]
    else:
        positions_n[0].append(0)

    positions_n.extend([positions[r] for r in sorted(positions)])

    with open(file, "a+") as f:
        line_desc = "{}, {}, {}".format(algorithm, alpha, iteration)
        line_values = ", ".join([str(p) for p in positions_n])
        line_text = "{}, {}".format(line_desc, line_values)

        f.write(line_text + "\n")


def save_data_from_planner(planner, algorithm, alpha, iteration, file="all_distributions.csv"):
    """Saves positions from a social planner to a file. Algorithms, alpha and iteration are used as text."""
    ranking_stat = get_positions_stat(planner)
    save_positions(ranking_stat, algorithm, alpha, iteration, file)

