class Student:
    def setData(self,roll_no,name,age):
        self.rn = roll_no
        self.nm = name
        self.age = age 

    def getData(self):
        print('Roll No:',self.rn)
        print('Name:',self.nm)
        print('Age:',self.age)

obj1 = Student()
obj1.setData(4,'snehal',21)
obj1.getData()
print('##################')
obj2 = Student()
obj2.setData(5,'bhumi',22)
obj2.getData()