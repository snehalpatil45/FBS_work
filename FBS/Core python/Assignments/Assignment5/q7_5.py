#e.x-x^2/3+x^3/5-x^4/7+...

x = int(input('Enter x:'))
n = int(input('Enter number of terms:'))
sum = 0
sign = 1
deno = 1
for i in range(1,n+1):
    sum = sum+sign*(x**i)/deno
    sign = sign * -1
    deno = deno + 2
print(f'sum:{sum}')