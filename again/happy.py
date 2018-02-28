#coding:utf-8

class M():
    def miss(self,a="red"):
        self.a = raw_input("input your color")
        return self.a

if __name__=="__main__":
    test = M()
    print test.miss()