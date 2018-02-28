#coding=utf-8
class calculator(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a +self.b
    def minus(self):
        return self.a - self.b
    def division(self):
        return self.a/self.b
if __name__=="__main__":
    test_a = 5.0
    test_b = 6.0
    cal = calculator(test_a,test_b)
    print cal.addition()
    print cal.minus()
    print cal.division()
