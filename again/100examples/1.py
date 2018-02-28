#coding:utf-8

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (k!=j)&(k!=i)&(j!=i):
                print i*100+j*10+k


