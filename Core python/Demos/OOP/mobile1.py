# constructor:
# 1. special method
# 2. called automatically when object of that class is created
# 3. use __init__ as method name
# 4. to execute mandatory task

# type of constructor - parameterized
class Mobile:
    def __init__(self,brand,processor,storage,price):
        self.brand = brand
        self.pro = processor
        self.sto = storage
        self.price = price

    def getData(self):
        print('Brand:',self.brand)
        print('Procesor:',self.pro)
        print('Storage:',self.sto)
        print('Price:',self.price)

m1 = Mobile('Samsung','Snapdragon 8-Gen','1 TB',170000)
m1.getData()