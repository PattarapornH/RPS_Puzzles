import arcade

s_width = 500
s_height = 650

class gameWindow(arcade.Window):
    def __init__ (self,width,height):
        super().__init__(width,height)
        arcade.set_background_colo(arcade.color.AERO_BLUE)
    
    def on_draw(self):
        arcade.start_render()

if __name__ == '__main__':
    window = gameWindow(s_width,s_height)
    arcade.run() 