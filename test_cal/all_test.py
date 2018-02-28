#coding=utf-8
import unittest
import test_Add
import test_Min

suite = unittest.TestSuite()
suite.addTest(test_Add.test_Add("test_add1"))
suite.addTest(test_Add.test_Add("test_add2"))
suite.addTest(test_Min.test_Min("test_min1"))
suite.addTest(test_Min.test_Min("test_min2"))

if __name__=="__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)