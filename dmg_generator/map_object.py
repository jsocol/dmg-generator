class MapObject():
    def __init__(self, x=0, y=0):
        self.position(x, y)
        self.connections = []

    def position(self, x, y):
        self.x = x
        self.y = y

    def find_position(self):
        pass

    def connect(self, other):
        if other not in self.connections:
            self.connections.push(other)
        other.connect(self)
