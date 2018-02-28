#coding:utf-8

import threading
import time

def music(num):
    for i in range(num):
        print "this is music ",i
        time.sleep(2)

def movie(number):
    for i in range(number):
        print "this is movie ",i
        time.sleep(2)

threads=[]
t1=threading.Thread(target=music,args=(3,))
threads.append(t1)
t2=threading.Thread(target=movie,args=(2,))
threads.append(t2)

if __name__=='__main__':
    print time.ctime()
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print time.ctime()













