import pickle

di = {'id':101,'name':'ABC','sal':50000,'dept':'IT'}

fp = open('C:/Users/ASUS/Desktop/FBS/Core python/Demos/File handling/demo_pkl.txt','wb')
pickle.dump(di,fp,protocol=pickle.HIGHEST_PROTOCOL)
fp.close()