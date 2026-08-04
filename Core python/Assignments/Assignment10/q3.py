# second largest element

def find_smax(li):
    max = li[0]
    smax = 0
    for i in range(len(li)):
        if(li[i] > max):
            smax = max
            max = li[i]
        elif(li[i] > smax):
            smax = li[i]
    return smax

li = [45,18,93,7,1,63]
smax = find_smax(li)
print(f'Smax:{smax}')