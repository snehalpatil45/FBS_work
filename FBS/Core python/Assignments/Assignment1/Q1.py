# write a program to calculate the percentage of student based on marks of any 5 subjects.

s1 = int(input("Enter the marks of physics:"))
s2 = int(input("Enter the marks of chemistry:"))
s3 = int(input("Enter the marks of maths:"))
s4 = int(input("Enter the marks of biology:"))
s5 = int(input("Enter the marks of geography:"))
total = s1 + s2 + s3 + s4 + s5
percentage = total / 5
print( "Total of marks is:", total)
print( "Percentage of student is:", percentage)