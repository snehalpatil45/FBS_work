from abc import ABC ,abstractmethod

class vehicle:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    @abstractmethod
    def stop(self):
        pass

class Car(vehicle):
    def __init__(self, brand, price,sunroof):
        super().__init__(brand, price)
        self.sunroof = sunroof

    def stop(self):
        print('Car stopped.')

c1 = Car('BMW',50000000,'yes')