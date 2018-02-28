#coding:utf-8

class Cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def plus(self):
        return self.a+self.b
    def minus(self):
        return self.a-self.b
    def mult(self):
        return self.a*self.b
    def division(self):
        return self.a/self.b

if __name__=='__main__':
    A = Cal(1,2)
    print A.plus()