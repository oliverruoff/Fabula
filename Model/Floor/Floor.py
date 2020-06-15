class Floor:
    def __init__(self, name, x, y, is_walkable=True):
        self.img = 'Assets/grass.png'
        self.name = name
        self.is_walkable = is_walkable
        self.x = x
        self.y = y