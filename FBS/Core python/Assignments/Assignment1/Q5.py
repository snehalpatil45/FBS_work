#write a program to enter p ,t, r  and calculate compound interest.

p = int(input("Enter the principal value:"))
t = int(input("Enter time:"))
r = int(input("Enter rate of interest:"))
amount = p * (1 + r / 100)**t
ci = amount - p 
print("compound interest is:", ci)