import py_school_match as psm

import unittest


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student1 = psm.Student()
        self.student2 = psm.Student()

    def tearDown(self):
        psm.Student.reset_ids()

    def test_student_incremental_id(self):
        self.assertGreater(self.student2._id, self.student1._id)

    def test_add_characteristic(self):
        test_criteria_value = True

        test_criteria = psm.Criteria("test_criteria", bool)
        test_characteristic = psm.Characteristic(test_criteria, test_criteria_value)
        self.student1.add_characteristic(test_characteristic)

        get_criteria_test_value = self.student1.characteristics[test_criteria][0].value
        self.assertEqual(get_criteria_test_value, test_criteria_value)

    def test_get_characteristic(self):
        test_criteria_value = True

        test_criteria = psm.Criteria("test_criteria", bool)
        test_characteristic = psm.Characteristic(test_criteria, test_criteria_value)
        self.student1.add_characteristic(test_characteristic)

        get_criteria_test_value = self.student1.get_characteristic(test_criteria)[0].value
        self.assertEqual(get_criteria_test_value, test_criteria_value)

    def test_reset_ids(self):
        student1_id = self.student1.id
        psm.Student.reset_ids()
        new_student_id = psm.Student().id
        self.assertEqual(student1_id, new_student_id)
