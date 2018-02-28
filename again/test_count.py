#coding:utf-8
from count import Count
'''
class TestCount:
    def testAdd(self):
        try:
            a=Count(1,2)
            result=a.addition()
            assert result==4,"result is 3"
        except:
            print "wrong"
mytest=TestCount()
mytest.testAdd()
'''

import unittest
class testCount(unittest.TestCase):
    def setUp(self):
        self.a=Count(2,3)
    def testadd(self):
        self.result=self.a.addition()
        self.assertEqual(self.result,5,msg="it is wrong")
    def tearDown(self):
        pass
if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(testCount("testadd"))
    runner=unittest.TextTestRunner()
    runner.run(suite)
