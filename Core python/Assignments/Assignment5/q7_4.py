#d.a+a^2/2+a^3/3+.....a^10/10.

a = int(input('Enter value of a:'))
sum = 0
for i in range(1,11):
    sum = sum+(a**i)/i
print(f'sum:{sum}')