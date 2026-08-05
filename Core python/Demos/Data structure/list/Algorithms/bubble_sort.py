def bubbleSort():
    for i in range(1,len(li)):
        for j in range(0,len(li)-i):
            if(li[j] > li[j+1]):
                li[j],li[j+1] = li[j+1],li[j]

li = [60,50,40,30,20,10]
print(f'Before swapping li:{li}')
bubbleSort()
print(f'After swapping li:{li}')