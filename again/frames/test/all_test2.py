#coding:utf-8

import unittest

def all_test2():
    suite=unittest.TestSuite()
    filepath='E:\\test_selenium\\again\\frames\\test'
    discover=unittest.defaultTestLoader.discover(filepath,pattern='test*.py',top_level_dir=None)
    for testsuite in discover:
        for testcase in testsuite:
            suite.addTest(testcase)
            print suite
    return suite


if __name__=='__main__':
    suite=all_test2()
    runner=unittest.TextTestRunner()
    runner.run(suite)

