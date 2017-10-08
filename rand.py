import arcade
import time
from random import randint

class rand_rps:
    def __init__(self):
        self.x = randint(1,7)
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

    def update(self,delta):
     #   time.sleep(0.1)
        if self.A or self.S or self.D :
            self.x = randint(1,7)
            self.A = False
            self.S = False
            self.D = False
            self.W = False
        return self.x

    '''
    x = 1   red rock 
    x = 2   red paper
    x = 3   red scrisor      
    x = 4   blue rock
    x = 5   blue paper
    x = 6   blue scrissor
    x = 7   add time
    '''