
import arcade

class time():
    def __init__(self):
        """
        Set up the application.
        """
        self.total_time = 60.0
        self.timer_text = None
        self.minutes = int(self.total_time) // 60
        self.seconds = int(self.total_time) % 60

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        self.total_time -= delta_time
