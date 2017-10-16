'''
A rock
S paper
D scissor
'''
import arcade
import random
#from rand import rand_rps

# Enumeration of RPS
class RPS:
    ROCK_RED = 1
    PAPER_RED = 2
    SCISSOR_RED = 3
    ROCK_BLUE = 4
    PAPER_BLUE = 5
    SCISSOR_BLUE = 6

class check_win_lost :
    def __init__(self):
        self.x = random.randint(1, 6)
        self.is_A_pressed = False
        self.is_S_pressed = False
        self.is_D_pressed = False
        self.is_W_pressed = False
        self.score = 0
      
    def on_key_press(self,key,key_modifiers):
        if key == arcade.key.A:
            self.is_A_pressed = True
            print("A PRESSED")
            #self.is_A_pressed = self.rand.on_key_press(key,key_modifiers)
        elif key == arcade.key.S:
            self.is_S_pressed = True
            print("S PRESSED")
            #self.is_S_pressed = self.rand.on_key_press(key,key_modifiers)
        elif key == arcade.key.D:
            print("D PRESSED")
            self.is_D_pressed = True
            #self.is_D_pressed = self.rand.on_key_press(key,key_modifiers)
        elif key == arcade.key.W:
            print("W PRESSED")
            self.is_W_pressed = True
            #self.is_W_pressed = self.rand.on_key_press(key,key_modifiers)
        
    def update(self,delta):
        x = self.x
        is_change_question = self.is_A_pressed or self.is_S_pressed or self.is_D_pressed or self.is_W_pressed

        if x == RPS.ROCK_RED : 
            if self.is_D_pressed:
                #print("D PRESSED: red rock")
                self.score += 10
                self.is_D_pressed = False
            elif is_change_question:
                self.score -= 5
        elif x == RPS.PAPER_RED :
            if self.is_A_pressed:
                #print("A PRESSED: red paper")
                self.score +=10
                self.is_A_pressed = False
        elif x == RPS.SCISSOR_RED :
            if self.is_S_pressed:
                #print("S PRESSED: red scissor")
                self.score +=10
                self.is_S_pressed = False
        elif x == RPS.ROCK_BLUE : 
            if self.is_S_pressed:
                #print("S PRESSED: blue rock")
                self.score +=10
                self.is_S_pressed = False
        elif x == RPS.PAPER_BLUE :
            if self.is_D_pressed:
                #print("D PRESSED: blue paper")
                self.score +=10
                self.is_D_pressed = False
        elif x == RPS.SCISSOR_BLUE :
            if self.is_A_pressed:
                #print("A PRESSED: blue scissor")
                self.score +=10
                self.is_A_pressed = False

        if is_change_question:
            print("CHANGE")
            self.x = random.randint(1, 6)
            self.is_A_pressed = False
            self.is_D_pressed = False
            self.is_S_pressed = False
            self.is_W_pressed = False

        return self.score
'''
class Red :
    def __init__(self,x)
        self.x = x
        ### RED ###
        if self.x == 1 : 
        #    print("red rock")
            if self.is_D_pressed:
                self.score +=10
                self.is_D_pressed = False
            else :
                self.score -= 5
        elif self.x == 2 :
            if self.is_A_pressed:
                self.score +=10
                self.is_A_pressed = False
            else :
                self.score -= 5
        elif self.x == 3 :
            if self.is_S_pressed:
                self.score +=10
                self.is_S_pressed = False
            else :
                self.score -= 5
        return self.score
class Blue :
        ### BLUE ###
        elif self.x == 4 : 
            if self.is_S_pressed:
                self.score +=10
                self.is_S_pressed = False
            else :
                self.score -= 5
        elif self.x == 5 :
            if self.is_D_pressed:
                self.score +=10
                self.is_D_pressed = False
            else :
                self.score -= 5
        elif self.x == 6 :
            if self.is_A_pressed:
                self.score +=10
                self.is_A_pressed = False
            else :
                self.score -= 5
        
        return self.score
#                print("correct")
#                self.score+=10
#            else :
#                self.score-=5
'''   
'''        
    def Rock(self):
        if self.is_D_pressed :
            self.sc.score += 10
            self.is_D_pressed = False
#            return True
        else:
            self.sc.score -= 5
#            return False
    
    def Paper(self):
        if self.is_A_pressed :
            self.sc.score += 10
            self.is_A_pressed = False
#            return True
        else:
            self.sc.score -= 5
#            return False

    def Scissor(self):
        if self.is_S_pressed :
            self.sc.score += 10
            self.is_S_pressed = False
#            return True
        else:
            self.sc.score -= 5
#            return False
'''