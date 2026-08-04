import time
from threading import Thread,Lock

def deposit(amount):
    lock.acquire()
    with open('C:/Users/ASUS/Desktop/FBS/Core python/Demos/Multithreading/balance.txt','r') as fp:
        balance = int(fp.read())
        balance += amount
    with open('C:/Users/ASUS/Desktop/FBS/Core python/Demos/Multithreading/balance.txt','w') as fp:
        fp.write(str(balance))
    lock.release()

def withdraw(amount):
    lock.acquire()
    with open('C:/Users/ASUS/Desktop/FBS/Core python/Demos/Multithreading/balance.txt','r') as fp:
        balance = int(fp.read())
        balance -= amount
    with open('C:/Users/ASUS/Desktop/FBS/Core python/Demos/Multithreading/balance.txt','w') as fp:
        fp.write(str(balance))
    lock.release()

lock = Lock()
t1 = Thread(name='Thread1',target=deposit,args=(5000,))
t2 = Thread(name='Thread2',target=withdraw,args=(3000,))
t1.start()
t2.start()