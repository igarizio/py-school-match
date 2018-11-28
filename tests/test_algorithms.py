import py_school_match as psm

import unittest
import random


class TestAlgorithmsWithEmptyRuleset(unittest.TestCase):
    def setUp(self):
        random.seed(42)

        psm.Student.reset_ids()
        psm.School.reset_ids()

        self.st0 = psm.Student()
        self.st1 = psm.Student()
        self.st2 = psm.Student()

        self.students = [self.st0, self.st1, self.st2]

        self.sc0 = psm.School(1)
        self.sc1 = psm.School(1)
        self.sc2 = psm.School(1)

        self.schools = [self.sc0, self.sc1, self.sc2]

        self.st0.preferences = [self.sc0, self.sc1, self.sc2]
        self.st1.preferences = [self.sc0, self.sc2, self.sc1]
        self.st2.preferences = [self.sc2, self.sc1, self.sc0]

        self.planner = psm.SocialPlanner(self.students, self.schools, psm.RuleSet())

    def test_dastb(self):
        self.planner.run_matching(psm.DASTB())
        self.assertEqual(self.st0.assigned_school.id, 0)
        self.assertEqual(self.st1.assigned_school.id, 1)
        self.assertEqual(self.st2.assigned_school.id, 2)

    def test_damtb(self):
        self.planner.run_matching(psm.DAMTB())
        self.assertEqual(self.st0.assigned_school.id, 0)
        self.assertEqual(self.st1.assigned_school.id, 2)
        self.assertEqual(self.st2.assigned_school.id, 1)

    def test_sic(self):
        self.planner.run_matching(psm.SIC())
        self.assertEqual(self.st0.assigned_school.id, 0)
        self.assertEqual(self.st1.assigned_school.id, 1)
        self.assertEqual(self.st2.assigned_school.id, 2)

    def test_ttc(self):
        self.planner.run_matching(psm.TTC())
        self.assertEqual(self.st0.assigned_school.id, 0)
        self.assertEqual(self.st1.assigned_school.id, 2)
        self.assertEqual(self.st2.assigned_school.id, 1)

    def test_nsic(self):
        self.planner.run_matching(psm.NSIC())
        self.assertEqual(self.st0.assigned_school.id, 0)
        self.assertEqual(self.st1.assigned_school.id, 1)
        self.assertEqual(self.st2.assigned_school.id, 2)

    def test_mnsic(self):
        self.planner.run_matching(psm.MNSIC())
        self.assertEqual(self.st0.assigned_school.id, 0)
        self.assertEqual(self.st1.assigned_school.id, 2)
        self.assertEqual(self.st2.assigned_school.id, 1)