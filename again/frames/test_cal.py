#coding:utf-8

import unittest
from cal import Cal

class test_cal(unittest.TestCase):
    def setUp(self):
        self.A=Cal(5,6)
    def test_add1(self):
        try:
            self.result= self.A.plus()
            self.assertEqual(self.result,11),'the result should be 11'
        except:
            raise "wrong"
    def tearDown(self):
        pass

if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(test_cal("test_add1"))
    runner=unittest.TextTestRunner()
    runner.run(suite)