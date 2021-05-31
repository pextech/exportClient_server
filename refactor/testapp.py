import unittest
import functions


class testAppSubmit(unittest.TestCase):

    def test_submit(self):
        test_password_term = ", password:" + "Password_1567"
        line = 'id:002,firstname:Alice,lastname:Brown'

        for each_character in test_password_term:
            line = line.rstrip() + each_character
        submit = functions.updated_students("final_students.txt", "a", line)
        self.assertTrue(submit)


class TestAppPassword(unittest.TestCase):

     def setUp(self):
        self.testfile = open('students.txt', 'r')
        self.testData = self.testfile.read()

     def tearDown(self):
        self.testfile.close()


     def test_password(self):
         password_valid = functions.password_validate()


         if password_valid != None:
            self.assertTrue(password_valid)

         else:
            self.assertFalse(password_valid)

