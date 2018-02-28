#coding=utf-8
import os,time
os.chdir(r"E:\test_selenium\test_cal")
os.system('python all_test2.py')

while True:
    os.chdir(r"E:\test_selenium\test_cal")
    if time.strftime("%M") == "18":
        os.system("python all_test2.py")
        continue
    else:
        time.sleep(30)
        print time.localtime()