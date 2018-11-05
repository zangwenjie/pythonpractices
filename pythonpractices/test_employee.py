import unittest
from give_raise import give_raise
from employee import Employee

class EmployeeTestCase(unittest.TestCase):

    def setUp(self):
        self.my_employee = Employee('xu','xiaoxiao',10000)


    def test_give_default_raise(self):
        re = give_raise(self.my_employee.money)
        self.assertEqual(re,15000)



    # def test_give_custom_raise(self):
    #     re = give_raise(self.my_employee.monye)
    #     self.assertEqual(re,)


if __name__ == '__main__':
    unittest.main()