
'''
A rock
S paper
D scrissor
'''
from random import randint
from scorer import score

import arcade.key
class Red:
    def __init__(self):
        self.x = random.x
        self.y = random.y

    def on_key_press(self,key,key_modifiers):
        self.A = (key == arcade.key.A)
        self.S = (key == arcade.key.S)
        self.D = (key == arcade.key.D)
        self.W = (key == arcade.key.W)

    def Rock(self):
        if(self.S):
            scorer.score+=10
            return True
        else:
            scorer.score-=5
            return False
    
    def Paper(self):
        if(self.D):
            scorer.score+=10
            return True
        else:
            scorer.score-=5
            return False

    def Scrissor(self):
        if(self.A):
            scorer.score+=10
            return True
        else:
            scorer.score-=5
            return False