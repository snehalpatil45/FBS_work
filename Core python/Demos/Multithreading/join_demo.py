import time
from threading import Thread

def fun1(str):
    for i in str:
        print(i,end = ' ',flush = True)
        time.sleep(1)

def fun2(str):
    for j in str:
        print(j,end = ' ',flush = True)
        time.sleep(1)

t1 = Thread(name ='Thread1',target = fun1,args=('11111111',))
t2 = Thread(name ='Thread2',target = fun2,args=('22222222',))
t1.start()
t1.join(3)
t2.start()

print('This is from main thread')