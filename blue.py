
'''
A rock
S paper
D scissor
'''
import arcade
from rand import rand_rps
#from scorer import score

class Blue_against:
    def __init__(self):
        self.rand = rand_rps()
        self.x = self.rand.x
        self.A = False
        self.S = False
        self.D = False
        self.W = False
   
    def on_key_press(self,key,key_modifier):
        if key == arcade.key.A:
            self.A = True
        elif key == arcade.key.S:
            self.S = True
        elif key == arcade.key.D:
            self.D = True
        elif key == arcade.key.W:
            self.W = True    
           
    def Rock(self):
        if self.S :
            self.S = False
            return True
        else:
            return False
    
    def Paper(self):
        if self.D :
            self.D = False
            return True
        else:
            return False

    def Scissor(self):
        if self.A :
            self.A = False
            return True
        else:
            return False