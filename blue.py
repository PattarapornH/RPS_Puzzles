
'''
A rock
S paper
D scissor
'''
from random import randint
from scorer import score

import arcade.key
class Blue_against:
    def __init__(self):
        self.x = rand.x
        self.y = rand.y
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
        if(self.S):
            self.sc.score+=10
        else:
            self.sc.score-=5
    
    def Paper(self):
        if(self.D):
            self.sc.score+=10
        else:
            self.sc.score-=5

    def Scissor(self):
        if(self.A):
            self.sc.score+=10
        else:
            self.sc.score-=5