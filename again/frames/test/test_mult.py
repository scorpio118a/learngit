#coding:utf-8

import sys
sys.path.append("..")
from again.frames import cal
import unittest

class test_mult(unittest.TestCase):
    def setUp(self):
        pass
    def test_mult1(self):
        self.A=cal.Cal(3,2)
        self.result=self.A.mult()
        self.assertEqual(self.result,6)

    def test_mult2(self):
        self.A=cal.Cal(0.2,1.7)
        self.result=self.A.mult()
        self.assertEqual(self.result,0.34)

    def test_mult3(self):
        self.A=cal.Cal(4,-5)
        self.result=self.A.mult()
        self.assertEqual(self.result,-20)

    def tearDown(self):
        pass

if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(test_mult("test_mult1"))
    suite.addTest(test_mult("test_mult2"))
    suite.addTest(test_mult("test_mult3"))
    runner=unittest.TextTestRunner()
    runner.run(suite)