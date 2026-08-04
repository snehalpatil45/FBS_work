# program to find the roots of a quadratic equation.

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))
r = ( b * b - 4 * a * c )** 0.5
r1 = (-b + r) /( 2 * a )
r2 = (-b - r) /( 2 * a )
print("Roots of quadratic equation is:",r1,r2)