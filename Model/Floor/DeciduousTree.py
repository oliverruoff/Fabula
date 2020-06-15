from Model.Floor import Floor

class DeciduousTree(Floor.Floor):
    def __init__(self, x, y):
        super().__init__('deciduous tree', x, y, False)
        self.img = 'Assets/Floor/tree_32.png'