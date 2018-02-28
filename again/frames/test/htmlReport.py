#coding:utf-8

import test_plus,test_mult,test_minus,test_division
import unittest
import sys
sys.path.append("..")
from again.frames import cal
import HTMLTestRunner

suite=unittest.TestSuite()
suite.addTest(test_mult.test_mult("test_mult1"))
suite.addTest(test_mult.test_mult("test_mult2"))
suite.addTest(test_mult.test_mult("test_mult3"))
suite.addTest(test_plus.test_plus("test_plus1"))
suite.addTest(test_plus.test_plus("test_plus2"))
suite.addTest(test_plus.test_plus("test_plus3"))


if __name__=='__main__':
    filename='E:\\test_selenium\\again\\frames\\report.html'
    fp = file(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="my test report",description="yes,it is the description!")
    runner.run(suite)
    fp.close()