class Student:
    count = 0
    def __init__(self,roll_no,name,age):
        Student.count += 1
        self.rn = roll_no
        self.nm = name
        self.age = age 

    def getData(self):
        print('Roll No:',self.rn)
        print('Name:',self.nm)
        print('Age:',self.age)

    def totalCount():  # static method
        return Student.count

obj1 = Student(4,'snehal',21)
obj2 = Student(5,'bhumi',22)
obj3 = Student(4,'snehal',21)
obj4 = Student(5,'bhumi',22)

obj1.getData()
print('##################')
obj2.getData()
print('##################')
print('Total no. of students:',Student.totalCount())