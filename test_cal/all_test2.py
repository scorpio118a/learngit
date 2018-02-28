#coding=utf-8
import unittest
import HTMLTestRunner
def createSuite():
    suiteunit = unittest.TestSuite()
    test_dir = r"E:\test_selenium\test_cal"
    discover = unittest.defaultTestLoader.discover(test_dir,"test*.py",top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            suiteunit.addTest(test_case)
    return suiteunit
if __name__=="__main__":
#    runner = unittest.TextTestRunner()
#    runner.run(createSuite())
    path = r"E:\test_selenium\test_cal\report.html"
    fp = file(path,"w")
    runner = HTMLTestRunner.HTMLTestRunner(fp,title="test report",description="test result is below: ")
    runner.run(createSuite())
    fp.close()