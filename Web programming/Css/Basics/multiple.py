class Dancer:
    def __init__(self):
        print("Dancer ready")

    def dance(self):
        print("Dancing ")


class Singer:
    def __init__(self):
        print("Singer ready")

    def sing(self):
        print("Singing ")


class Performer(Dancer, Singer):
    def __init__(self):
        Dancer.__init__(self)   # call Dancer constructor
        Singer.__init__(self)   # call Singer constructor
        print("Performer ready")

    def perform(self):
        self.dance()   # from Dancer
        self.sing()    # from Singer


p = Performer()
p.perform()