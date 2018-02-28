#codign=utf-8
import unittest

from Calculator import calculator


class test_Add(unittest.TestCase):
    def setUp(self):
        pass
    def test_add1(self):
        '''the first test cases'''
        self.cal = calculator(2,0)
        self.add = self.cal.addition()
        self.assertEqual(self.add,2,'the count is not 5')
    def test_add2(self):
        self.cal = calculator(-2,-1)
        self.add = self.cal.addition()
        self.assertEqual(self.add,-3,'the count is not -3')
    def test_add3(self):
        self.cal = calculator(-2,-1)
        self.add = self.cal.addition()
        self.assertEqual(self.add,-1,'the count is not -3')
    def tearDown(self):
        pass
if __name__=="__main__":
    suite = unittest.TestSuite()
    suite.addTest(test_Add("test_add1"))
    suite.addTest(test_Add("test_add2"))
    suite.addTest(test_Add("test_add3"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

