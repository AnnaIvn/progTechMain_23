import unittest
import my_program as prog

class TestMyProgram(unittest.TestCase):

    # basic setup
    def setUp(self):
        self.prog = prog

    # test for checking format 
    def test_check_format(self):
        self.assertTrue(prog.check_format('6Ben Schaefer'))     # correct
        self.assertTrue(prog.check_format('7Findlay Shaffer'))  # correct
        self.assertTrue(prog.check_format('8Kara Moss'))        # correct
        self.assertFalse(prog.check_format('Pen'))              # no age + incorrect length
        self.assertFalse(prog.check_format('Emre Walls'))       # no age
        self.assertFalse(prog.check_format('5Asa Rojas'))       # incorrect age
        self.assertFalse(prog.check_format('9Casey Long'))      # incorrect age
        self.assertFalse(prog.check_format('9E'))               # incorrect length

    # test for adding ':' character if needed
    def test_two_dot_formating(self):
        self.assertEqual(prog.two_dot_formating('6Anna Rou'), '6:Anna Rou')          # changed
        self.assertEqual(prog.two_dot_formating('6:Reg Realmer'), '6:Reg Realmer')   # unchanged

    # test group distribution
    def test_distrib_by_age(self):
        self.assertEqual(prog.distrib_by_age('6: Andreas Pittman'), '6: Andreas Pittman -> 1st grade')
        self.assertEqual(prog.distrib_by_age('7: Blake Bowman'), '7: Blake Bowman -> 2nd grade')
        self.assertEqual(prog.distrib_by_age('8: Ruth Roy'), '8: Ruth Roy -> 3rd grade')
        self.assertEqual(prog.distrib_by_age('5: Katie Rivera'), '5: Katie Rivera -> Incorrect age')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
