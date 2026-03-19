n = 5
for i in range(1,n+1):
    print(' '*4,end = '  ')
    for j in range(i):
        print('*',end = ' ')
    print()
for i in range(n-1,0,-1):
    print(' '*4,end = '  ')
    for j in range(i):
        print('*',end = ' ')
    print()