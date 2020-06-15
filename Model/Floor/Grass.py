
from Model.Floor import Floor

class Grass(Floor.Floor):

    def __init__(self, x, y):
        super().__init__('grass', x, y, True)
        self.img = 'Assets/Floor/grass_32.png'