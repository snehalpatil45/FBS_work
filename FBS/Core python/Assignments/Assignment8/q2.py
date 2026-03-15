# 2. Write a program to calculate area of circle
def area_circle(r):
    area = 3.14 * r * r
    return area

radius = int(input("Enter radius: "))
print(f'Area of circle : {area_circle(radius)} ')
