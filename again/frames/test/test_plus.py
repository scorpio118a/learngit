#coding:utf-8

import sys,unittest
sys.path.append("..")
from again.frames import cal

class test_plus(unittest.TestCase):
    def setUp(self):
        pass
    def test_plus1(self):
        '''integer plus'''
        self.A=cal.Cal(2,3)
        self.result=self.A.plus()
        self.assertEqual(self.result,5)

    def test_plus2(self):
        self.A=cal.Cal(0.5,1.2)
        self.result=self.A.plus()
        self.assertEqual(self.result,1.7)

    def test_plus3(self):
        self.A=cal.Cal('hello','world')
        self.result=self.A.plus()
        self.assertEqual(self.result,'helloworld')

    def tearDown(self):
        pass

if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(test_plus("test_plus1"))
    suite.addTest(test_plus("test_plus2"))
    suite.addTest(test_plus("test_plus3"))
    runner=unittest.TextTestRunner()
    runner.run(suite)


