from singer import Singer
from dancer import Dancer

class Performer(Singer,Dancer):
    def __init__(self,song_type,dance_style,exp):
        Singer.__init__(self,song_type)
        Dancer.__init__(self,dance_style)
        self.exp = exp

    def show(self):
        print('show method of performer.')

p1 = Performer('Classical','Katthak',50)
p1.display()