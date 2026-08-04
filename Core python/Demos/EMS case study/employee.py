class Employee:
    def __init__(self,id,nm,sal,dept):
        self.id = id
        self.nm = nm
        self.sal = sal
        self.dept = dept

    def toTuple(self):
        return(self.id,self.no,self.sal,self.dept)

if(__name__ == '__main__'):
    e1 = Employee(101,'ABC',20000,'IT')
    res = e1.toTuple()
    print(type(res))
    print(res)