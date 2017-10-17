
import arcade

from check import check_win_lost

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500

class gameWindow(arcade.Window):
    def __init__ (self,width,height):
        super().__init__(width,height)
        self.background = arcade.load_texture("images/bg1.jpg")
        self.check = check_win_lost()
        self.x = self.check.x
        self.score = 0
        self.score_text = None
        self.time = 60.0
        self.time_text = None
        self.screen_state = 1  # state = 1 -> show how to play and pressed to start
    
    def on_draw(self):
        arcade.start_render()
        '''
        #### HOW TO PLAY ####
        if self.screen_state == 1 :
            arcade.set_background_color(arcade.color.WHEAT)
            self.text1 = arcade.create_text("HOW TO PLAY", arcade.color.BLACK,30)
            self.text2 = arcade.create_text("BLUE : Win aganist the symbol",arcade.color.BLUE,20)
            self.text3 = arcade.create_text("RED : Lose aganist the symbol",arcade.color.RED,20)
            self.text4 = arcade.create_text("Press A to choose ROCK",arcade.color.GREEN,15)
            self.text5 = arcade.create_text("Press S to choose PAPER",arcade.color.GREEN,15)
            self.text6 = arcade.create_text("Press D to choose SCISSOR",arcade.color.GREEN,15)
            self.text7 = arcade.create_text("Press Q to start game",arcade.color.GREEN,15)
        '''
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

        #### SCORE ####
        output_score = f"Score : {self.score}"
        if not self.score_text or self.score_text.text != output_score:
            self.score_text = arcade.create_text(output_score, arcade.color.BLACK, 15)
        arcade.render_text(self.score_text,300,475)

        #### TIME ####
        output_time = f"Time : {round(self.time)}"
        if not self.time_text or self.time_text.text != output_time :
            self.time_text = arcade.create_text(output_time, arcade.color.BLACK, 15)
        arcade.render_text(self.time_text, 10, 475)

        if self.time == 0:
            arcade.stop_render()
   
    def on_key_press(self,key,key_modifiers):
        self.check.on_key_press(key,key_modifiers)

    def update(self,delta):
        self.score = self.check.update(delta)
        self.x = self.check.x
        #print(type(delta))
        self.time -= delta
        
if __name__ == '__main__':
    window = gameWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()
