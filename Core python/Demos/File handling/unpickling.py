import pickle

fp = open('C:/Users/ASUS/Desktop/FBS/Core python/Demos/File handling/demo.txt','rb')
obj = pickle.load(fp)
print(obj)
fp.close()