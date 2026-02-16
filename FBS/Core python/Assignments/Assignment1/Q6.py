#write a program to input two angles from user and find third angle of the triange.

a1 = int(input("Enter first angle of triangle:"))
a2 = int(input("Enter second angle of triangle:"))
a3 = 180 - ( a1 + a2 )
print("Third angle of triangle is :",a3)