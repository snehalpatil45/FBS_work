#write a program to enter p, t, r and calculate simple intrest.

p = int(input("Enter principal value:"))
t = int(input("Enter time:"))
r = int(input("Enter rate:"))
si = (p * t * r) / 100
print(" Simple interest is:",si)