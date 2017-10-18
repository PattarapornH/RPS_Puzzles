
class count_scorer():
    def __init__(self):
        self.score = 0
    def update(self,delta):
        if(self.score<0):
            self.score = 0