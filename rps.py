import arcade

from rand import rand_rps
from red import Red_against
from blue import Blue_against
from timer import time
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
        self.x = self.rand.x
        self.y = self.rand.y
        self.sc = score()
        self.score_text = None
        print(self.x)
  #      self.x = rand_rps.x
   #     self.y = rand.rand_rps.y
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        output = f"Score : {self.sc.score}"
        if not self.score_text or self.score_text.text != output:
            self.score_text = arcade.create_text(output, arcade.color.BLACK, 30)
        arcade.render_text(self.score_text,100,100)
        if(self.x>=1):
            self.rock = arcade.Sprite('images/fist  red.png')
            self.rock.set_position(200,300)
            self.rock.draw()
            self.red = Red_against().Rock()

 #   def update(self)


 #   def update(self,delta):
  #      if(self.rand>=1 and self.rand<=3):


if __name__ == '__main__':
    window = gameWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()
