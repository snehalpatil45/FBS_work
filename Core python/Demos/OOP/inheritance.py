class vehicle:
    def __init__(self,brand,color,price):
        self.brand = brand
        self.color = color
        self.price = price

    def getData(self):
        return f'BRAND:{self.brand}\nCOLOR:{self.color}\nPRICE:{self.price}\n'
    
class car(vehicle):
    def __init__(self,brand,color,price,sunroof):
        super().__init__(brand,color,price)
        self.sunroof = sunroof

    def getData(self):
        data = super().getData()
        data += f'SUNROOF:{self.sunroof}'
        return data
        #return super().getData()+f'SUNROOF:{self.sunroof}'

c1 = car('BMW','Black',200000000,'yes')
print(c1.getData())