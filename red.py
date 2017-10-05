'''
A rock
S paper
D scrissor
'''
from rand import rand_rps
from scorer import score

import arcade.key

class Red_against():
    def __init__(self):
        self.x = rand_rps().x
        self.y = rand_rps().y
        self.A = False
        self.S = False
        self.D = False
        self.W = False
        self.sc = score()

    def on_key_press(self,key,key_modifiers):
        self.A = (key == arcade.key.A)
        self.S = (key == arcade.key.S)
        self.D = (key == arcade.key.D)
        self.W = (key == arcade.key.W)

    def Rock(self):
        if self.D:
            self.sc.score+=10
            return True
        else:
            self.sc.score-=5
            return False
    
    def Paper(self):
        if(self.A):
            self.sc.score+=10
            return True
        else:
            self.sc.score-=5
            return False

    def Scissor(self):
        if(self.S):
            self.sc.score+=10
            return True
        else:
            self.sc.score-=5
            return False