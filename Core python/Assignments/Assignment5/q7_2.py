# b. N+N^2+N^3+.....N^n

n = int(input('Enter N:'))
sum = 0
for i in range(1,n+1):
    sum = sum + n**i
print(f'sum:{sum}')