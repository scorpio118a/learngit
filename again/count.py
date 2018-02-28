#coding:utf-8

class Count:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def addition(self):
        return self.a+self.b
    def minus(self):
        return self.a-self.b

if __name__=="__main__":
    A=Count(1,2)
    print A.addition()