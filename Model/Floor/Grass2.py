
from Model.Floor import Floor

class Grass2(Floor.Floor):

    def __init__(self, x, y):
        super().__init__('grass2', x, y, True)
        self.img = 'Assets/Floor/grass_32_2.png'