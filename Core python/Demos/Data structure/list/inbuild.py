li = [5,4,1,18,50]
l3 = [5,4,1,18,50] 
li.append(10)
print(li)
# what is the name of the function
# how many parameter it takes
# what is the purpose of that parameter 
# what it returns 
# li.clear()
# print(li)
li1 = li.copy()
print(li1)
print(f'ID li : {id(li)}')
print(f'ID li1 : {id(li1)}')
print(li is l3)
print(li == l3)
print(li.count(18))
li.extend([100,200])
print(li)
li.insert(1,7)
print(li)