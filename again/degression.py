#coding:utf-8

import happy
from test import sushi
class A:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
class B(A):
    def mul(self,c,d):
        return c*d
    def divs(self,c,d):
        return c/d

element=B()
#testD=happy.M()
#print testD.miss()
print element.add(1,2)
test2=sushi.food()
print test2.sushi("a")
