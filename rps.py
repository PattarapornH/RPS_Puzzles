
import arcade
import time

from rand import rand_rps
from red import Red_against
from blue import Blue_against
from check import check_win_lost

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
        #self.rand = rand_rps()
        self.R = Red_against()
        self.B = Blue_against()
        self.check = check_win_lost()
        self.x = self.check.x
        self.score = 0
        self.score_text = None
     #   print(self.x)
    
    def on_draw(self):

        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        #### DRAW CHOICE ####
        self.rock = arcade.Sprite('images/rock.png')
        self.rock.set_position(100,100)
        self.rock.draw()

        self.paper = arcade.Sprite('images/paper.png')
        self.paper.set_position(200,100)
        self.paper.draw()

        self.scissor = arcade.Sprite('images/scissor.png')
        self.scissor.set_position(300,100)
        self.scissor.draw()

        #### RED ####
        if self.x == 1 :
            self.rock_red = arcade.Sprite('images/rock red.png')
            self.rock_red.set_position(200,300)
            self.rock_red.draw()
        elif self.x == 2 :
            self.paper_red = arcade.Sprite('images/paper red.png')
            self.paper_red.set_position(200,300)
            self.paper_red.draw()
        elif self.x == 3 :
            self.scissor_red = arcade.Sprite('images/scissor red.png')
            self.scissor_red.set_position(200,300)
            self.scissor_red.draw()
        #### BLUE ####
        elif self.x == 4 :
            self.rock_blue = arcade.Sprite('images/rock blue.png')
            self.rock_blue.set_position(200,300)
            self.rock_blue.draw()
        elif self.x == 5 :
            self.paper_blue = arcade.Sprite('images/paper blue.png')
            self.paper_blue.set_position(200,300)
            self.paper_blue.draw()
        elif self.x == 6 :
            self.scissor_blue = arcade.Sprite('images/scissor blue.png')
            self.scissor_blue.set_position(200,300)
            self.scissor_blue.draw()
        #### TIME ####
        elif self.x == 7:
            self.add_time = arcade.Sprite('images/scissor blue.png')
            self.add_time.set_position(200,300)
            self.add_time.draw()

        output = f"Score : {self.score}"
        if not self.score_text or self.score_text.text != output:
            self.score_text = arcade.create_text(output, arcade.color.BLACK, 30)
        arcade.render_text(self.score_text,100,400)

    
    
    def on_key_press(self,key,key_modifiers):
        #self.rand.on_key_press(key,key_modifiers)
        self.check.on_key_press(key,key_modifiers)
        #self.R.on_key_press(key,key_modifiers)
        #self.B.on_key_press(key,key_modifiers)

    def update(self,delta):
        self.score = self.check.update(delta)
        self.x = self.check.x
        
if __name__ == '__main__':
    window = gameWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()
