# wap to reverse three digit number.

n = int(input("Enter 3 digit number:"))
a = n // 100
b = (n // 10) % 10
c = n % 10
rev = c * 100 + b * 10 + a
print("Reverse:",rev)