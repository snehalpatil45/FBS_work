def selectionSort():
    for i in range(0,len(li)-1):
        ind = i
        for j in range(i+1,len(li)):
            if li[ind] > li[j]:
                ind = j
        li[i],li[ind] = li[ind],li[i]

li = [60,30,10,50,40,20]
print(f'Before swapping : {li}')
selectionSort()
print(f'After swapping :{li}')