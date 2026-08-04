# write a program to print folllowing patterns:

for i in range(1,21):
    for j in range(1,21):
        if(i == 1 or i == 20 or i+j == 21):
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()