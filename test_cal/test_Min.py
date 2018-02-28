#coding=utf-8
import unittest
from Calculator import calculator

class test_Min(unittest.TestCase):
    def setUp(self):
        pass
    def test_min1(self):
        self.cal = calculator(5,6)
        self.min = self.cal.minus()
        self.assertEqual(self.min,-1,msg= 'the result should be -1')
    def test_min2(self):
        self.cal = calculator(5,3)
        self.min = self.cal.minus()
        self.assertEqual(self.min,2,msg='the result should be 2')

if __name__=="__main__":
    suite = unittest.TestSuite()
    suite.addTest(test_Min("test_min1"))
    suite.addTest(test_Min("test_min2"))
    runner = unittest.TextTestRunner()
    runner.run(suite)