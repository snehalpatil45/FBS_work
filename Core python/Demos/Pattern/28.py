row = int(input('Enter rows:'))
k = int(input('Enter value of k:'))
for i in range(1,row+1):
    for j in range(1,i+1):
        print('*',end= ' ')
    for j in range(1,k+1):
        print(' ',end= ' ')
    k -= 2
    for j in range(1,i+1):
        if(i != row or j != 1):
            print('*',end= ' ')
    print()