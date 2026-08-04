a = int(input('Enter number for a:'))
b = int(input('Enter number for b:'))
result = 1
for i in range(b):
    result = result*a
print(f'{a}*{b} : {result}')