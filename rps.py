import arcade

from rand import rand_rps
from red import Red_against
from blue import Blue_against
#from timer import time
from scorer import score

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
'''
class time():
    def __init__(self,time):
        self.total_time = time
        self.timer_text = None
        self.minutes = int(self.total_time) // 60
        self.seconds = int(self.total_time) % 60

    def update(self, delta_time):
        self.total_time -= delta_time
'''
class gameWindow(arcade.Window):
    def __init__ (self,width,height):
        super().__init__(width,height)
        self.background = arcade.load_texture("images/bg1.jpg")
        self.rand = rand_rps()
    #    self.x = 1
    #    self.y = self.rand.y
        self.a = Red_against()
    #    self.sc = score()
        self.score = 0
        self.score_text = None
     #   print(self.x)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        output = f"Score : {self.score}"
        if not self.score_text or self.score_text.text != output:
            self.score_text = arcade.create_text(output, arcade.color.BLACK, 30)
        arcade.render_text(self.score_text,100,100)
        ##RED
        if(self.x == 1):
            self.rock = arcade.Sprite('images/fist  red.png')
            self.rock.set_position(200,300)
            self.rock.draw()
        elif(self.x == 2):
            self.paper = arcade.Sprite('images/hand red.png')
            self.paper.set_position(200,300)
            self.paper.draw()
        elif(self.x == 3):
            self.scissor = arcade.Sprite('images/victory-sign (1).png')
            self.scissor.set_position(200,300)
            self.scissor.draw()
        ##BLUE
        elif(self.x == 4):
            self.rock = arcade.Sprite('images/fist blue.png')
            self.rock.set_position(200,300)
            self.rock.draw()
        elif(self.x == 5):
            self.paper = arcade.Sprite('images/hand blue.png')
            self.paper.set_position(200,300)
            self.paper.draw()
        elif(self.x == 6):
            self.scissor = arcade.Sprite('images/victory-sign.png')
            self.scissor.set_position(200,300)
            self.scissor.draw()

    def on_key_press(self,key,key_modifier):
        Red_against().on_key_press(key,key_modifier)

    def update(self,delta):
        self.x = rand_rps().x
        self.y = rand_rps().y
        ##RED
        if(self.x==1):
            self.red = Red_against().Rock()
            if(self.red):
                self.score+=10
            else:
                self.score-=5
        elif(self.x==2):
            self.red = Red_against().Paper()
            if(self.red):
                self.score+=10
            else:
                self.score-=5
        elif(self.x==3):
            self.red = Red_against().Scissor()
            if(self.red):
                self.score+=10
            else:
                self.score-=5

        ##BLUE
        elif(self.x==4):
            self.blue = Blue_against().Rock()
            if(self.blue):
                self.score+=10
            else:
                self.score-=5
        elif(self.x==5):
            self.blue = Blue_against().Paper()
            if(self.blue):
                self.score+=10
            else:
                self.score-=5       
        elif(self.x==6):
            self.blue = Blue_against().Scissor()
            if(self.blue):
                self.score+=10
            else:
                self.score-=5
        ##set score
        if(self.score<0):
            self.score = 0

if __name__ == '__main__':
    window = gameWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()
