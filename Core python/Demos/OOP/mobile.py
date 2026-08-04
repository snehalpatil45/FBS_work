class Mobile:
    def __init__(self,id,name,price):
        self.id = id
        self.name = name
        self.price = price

    def showPrice(self):
        print('Price:',self.price)

    def mName(self):
        print('Name:',self.name)  

m = Mobile(1,'samsung',50000)
m.showPrice() 
m.mName() 