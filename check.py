'''
A rock
S paper
D scissor
'''
import arcade
import random

# Enumeration of RPS

ROCK_RED = 1
PAPER_RED = 2
SCISSOR_RED = 3
ROCK_BLUE = 4
PAPER_BLUE = 5
SCISSOR_BLUE = 6

GAME_PLAYED = 1
GAME_OVER = 2

class check_win_lost :
    def __init__(self, world):
        self.x = random.randint(1,6)
        self.is_A_pressed = False
        self.is_S_pressed = False
        self.is_D_pressed = False
        self.is_W_pressed = False
        self.back_to_game_played = None
        self.score = 0
        self.world = world

        #### SOUND ####
        self.sound_correct = arcade.sound.load_sound('sound/correct.mp3')
        self.sound_wrong = arcade.sound.load_sound('sound/wrong.mp3')
      
    def on_key_press(self,key,key_modifiers):
        if key == arcade.key.A:
            self.is_A_pressed = True
            print("A PRESSED")
        elif key == arcade.key.S:
            self.is_S_pressed = True
            print("S PRESSED")
        elif key == arcade.key.D:
            print("D PRESSED")
            self.is_D_pressed = True
        elif key == arcade.key.W:
            print("W PRESSED")
            self.is_W_pressed = True
        
    def update(self,delta):
        x = self.x
        if self.world.game_state == GAME_OVER :
            x = -1
        self.is_change_question = self.is_A_pressed or self.is_S_pressed or self.is_D_pressed
        self.back_to_game_played = self.is_W_pressed
        #### RED ####
        if x == ROCK_RED : 
            if self.is_D_pressed:
                #print("D PRESSED: red rock")
                self.score += 10
                self.is_D_pressed = False
                arcade.sound.play_sound(self.sound_correct)
            elif self.is_change_question:
                self.score -= 7
                arcade.sound.play_sound(self.sound_wrong)
        elif x == PAPER_RED :
            if self.is_A_pressed:
                #print("A PRESSED: red paper")
                self.score +=10
                self.is_A_pressed = False
                arcade.sound.play_sound(self.sound_correct)
            elif self.is_change_question:
                self.score -= 7
                arcade.sound.play_sound(self.sound_wrong)
        elif x == SCISSOR_RED :
            if self.is_S_pressed:
                #print("S PRESSED: red scissor")
                self.score +=10
                self.is_S_pressed = False
                arcade.sound.play_sound(self.sound_correct)
            elif self.is_change_question:
                self.score -= 7
                arcade.sound.play_sound(self.sound_wrong)
        #### BLUE ####
        elif x == ROCK_BLUE : 
            if self.is_S_pressed:
                #print("S PRESSED: blue rock")
                self.score +=10
                self.is_S_pressed = False
                arcade.sound.play_sound(self.sound_correct)
            elif self.is_change_question:
                self.score -= 7
                arcade.sound.play_sound(self.sound_wrong)
        elif x == PAPER_BLUE :
            if self.is_D_pressed:
                #print("D PRESSED: blue paper")
                self.score +=10
                self.is_D_pressed = False
                arcade.sound.play_sound(self.sound_correct)
            elif self.is_change_question:
                self.score -= 7
                arcade.sound.play_sound(self.sound_wrong)
        elif x == SCISSOR_BLUE :
            if self.is_A_pressed:
                #print("A PRESSED: blue scissor")
                self.score +=10
                self.is_A_pressed = False
                arcade.sound.play_sound(self.sound_correct)
            elif self.is_change_question:
                self.score -= 7
                arcade.sound.play_sound(self.sound_wrong)
        
        #### SET SCORE OR GAME OVER####
        if self.score < 0 or self.back_to_game_played:
            self.score = 0
            self.is_W_pressed = False

        #### RANDOM ####
        if self.is_change_question:
            print("CHANGE")
            self.x = random.randint(1, 6)
            self.is_A_pressed = False
            self.is_D_pressed = False
            self.is_S_pressed = False
        return self.score
