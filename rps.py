
import arcade

from check import check_win_lost

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
GAME_PLAYED = 1
GAME_OVER = 2

class gameWindow(arcade.Window):
    def __init__ (self,width,height):
        super().__init__(width,height,title = "RPS_Puzzles")
        self.background = arcade.load_texture("images/bg1.jpg")
        self.check = check_win_lost(self)
        self.x = self.check.x
        self.score = 0
        self.score_text = None
        self.time = 20.0
        self.time_text = None
        self.game_state = 1

        #### CHOICE ####
        self.rock = arcade.Sprite('images/rock.png')
        self.rock.set_position(100,100)
        self.text_A = arcade.create_text("A", arcade.color.BLACK,15)

        self.paper = arcade.Sprite('images/paper.png')
        self.paper.set_position(210,100)
        self.text_S = arcade.create_text("S", arcade.color.BLACK,15)

        self.scissor = arcade.Sprite('images/scissor.png')
        self.scissor.set_position(300,100)
        self.text_D = arcade.create_text("D", arcade.color.BLACK,15)

        #### RED ####
        self.rock_red = arcade.Sprite('images/rock red.png')
        self.rock_red.set_position(200,300)
        
        self.paper_red = arcade.Sprite('images/paper red.png')
        self.paper_red.set_position(200,300)

        self.scissor_red = arcade.Sprite('images/scissor red.png')
        self.scissor_red.set_position(200,300)          

        #### BLUE ####
        self.rock_blue = arcade.Sprite('images/rock blue.png')
        self.rock_blue.set_position(200,300)

        self.paper_blue = arcade.Sprite('images/paper blue.png')
        self.paper_blue.set_position(200,300)

        self.scissor_blue = arcade.Sprite('images/scissor blue.png')
        self.scissor_blue.set_position(200,300)
    def on_draw_game(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        #### DRAW CHOICE ####
        self.rock.draw()
        arcade.render_text(self.text_A,100,50)

        self.paper.draw()
        arcade.render_text(self.text_S,200,50)
        
        self.scissor.draw()
        arcade.render_text(self.text_D,300,50)

        #### DRAW RED ####
        if self.x == 1 : 
            self.rock_red.draw()
        elif self.x == 2 :
            self.paper_red.draw()
        elif self.x == 3 :
            self.scissor_red.draw()
        #### DRAW BLUE ####
        elif self.x == 4 :
            self.rock_blue.draw()
        elif self.x == 5 :
            self.paper_blue.draw()
        elif self.x == 6 :
            self.scissor_blue.draw()

        #### DRAW SCORE ####
        output_score = f"Score : {self.score}"
        if not self.score_text or self.score_text.text != output_score:
            self.score_text = arcade.create_text(output_score, arcade.color.BLACK, 15)
        arcade.render_text(self.score_text,300,475)
        #### DRAW TIME ####
        output_time = f"Time : {round(self.time)}"
        if not self.time_text or self.time_text.text != output_time :
            self.time_text = arcade.create_text(output_time, arcade.color.BLACK, 15)
        arcade.render_text(self.time_text, 10, 475)
    
    def on_draw_game_over(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        output_game_over = "GAME OVER"
        arcade.draw_text(output_game_over, 70, 400, arcade.color.BLACK, 40)
        output_last_score = f"Score : {round(self.score)}"
        arcade.draw_text(output_last_score,120,280,arcade.color.BLUE_VIOLET,25)
        output_restart = "Press W to restart"
        arcade.draw_text(output_restart, 80,175, arcade.color.BLUE_SAPPHIRE, 25)
        self.rock.draw()
        self.paper.draw()
        self.scissor.draw()
    
    def on_key_press(self,key,key_modifiers):
        self.check.on_key_press(key,key_modifiers)
    
    def on_draw(self):
        arcade.start_render()
        if self.game_state == GAME_PLAYED :
            self.on_draw_game()
        
        elif self.game_state == GAME_OVER :
            self.on_draw_game_over()
            if self.check.back_to_game_played :
                print("GAME OVER")
                self.time = 20.0
                self.game_state = 1
            
    def update(self,delta):
        self.score = self.check.update(delta)
        self.x = self.check.x
        self.time -= delta
        if round(self.time) == -1 :
            self.game_state = 2
        
if __name__ == '__main__':
    window = gameWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()
