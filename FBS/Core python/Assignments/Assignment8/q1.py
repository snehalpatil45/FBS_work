#1. Write a program to calculate area of rectangle.
def area_rectangle(length, breadth):
    area = length * breadth
    return area

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
print(f'Area of rectangle :{area_rectangle(l,b)}')
