
'''
A rock
S paper
D scissor
'''
from rand import rand_rps
from scorer import score

import arcade.key
class Blue_against:
    def __init__(self):
        self.x = rand_rps().x
        self.y = rand_rps().y
        self.A = False
        self.S = False
        self.D = False
        self.W = False

    def on_key_press(self,key,key_modifiers):
        if key == arcade.key.A:
            self.A = True
        elif key == arcade.key.S:
            self.S = True
        elif key == arcade.key.D:
            self.D = True
        elif key == arcade.key.W:
            self.W = True

    def Rock(self):
        if(self.S):
            return True
        else:
            return False
    
    def Paper(self):
        if(self.D):
            return True
        else:
            return False

    def Scissor(self):
        if(self.A):
            return True
        else:
            return False