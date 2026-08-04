li = [30,70,25,84,32,90,20,10]
max = li[0]
for ind in range(1,len(li)):
    if(max < li[ind]):
        max = li[ind]
print(max)