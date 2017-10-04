
from random import randint


class rand_rps:
    def __init__(self):
        self.x = randint(1,7)
        self.y = randint(8,12)

    '''
    x = 1               red rock 
    x = 2               red paper
    x = 3               red scrisor      
    x = 4               blue rock
    x = 5               blue paper
    x = 6               blue scrissor
    x = 7 and y=8       add time
    '''