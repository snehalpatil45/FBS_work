# Dictionary
#1.Denoted by {}
di = {1:'python',2:'java',3:'testing'}

#2.heterogenous
di = {'id':101,'name':'abc',5:45000.37}

#3.ordered

#4.element = mutable,value = mutable,key = immutable
di[6] = 34324
di[5] = 50000

#5. key are unique,values can be duplicate
di = {1:'python',2:'java',2:'c'}
print(di)

di = {1:'python',(1,2):'java',[10,20]:'c'}
print(di)