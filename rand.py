import arcade
from random import randint
#from red import Red_against
#from blue import Blue_against

class rand_rps:
    def __init__(self):
   #     self.red = Red_against()
   #     self.blue = Blue_against()
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
    
    def on_key_release(self,key,key_modifiers):
        if key == arcade.key.A:
            self.A = True
        elif key == arcade.key.S:
            self.S =  True
        elif key == arcade.key.D:
            self.D = True
        elif key == arcade.key.W:
            self.W = True

    def update(self,delta):
        if self.A or self.S or self.D :
            self.x = randint(1,7)
            self.A = False
            self.S = False
            self.D = False
            self.W = False
        return self.x

    '''
    x = 1               red rock 
    x = 2               red paper
    x = 3               red scrisor      
    x = 4               blue rock
    x = 5               blue paper
    x = 6               blue scrissor
    x = 7 and y=8       add time
    '''