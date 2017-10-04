
import arcade

class time():
    def __init__(self,time):
        self.total_time = time
        self.timer_text = None
        self.minutes = int(self.total_time) // 60
        self.seconds = int(self.total_time) % 60

    def update(self, delta_time):
        self.total_time -= delta_time
