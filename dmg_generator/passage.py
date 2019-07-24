from dmg_generator.map_object import MapObject


class _NoExit():
    pass


NoExit = _NoExit()


class Intersection(MapObject):
    def __init__(self, passage):
        super().__init__()
        self.exits = [passage, None, None, None]
        self.connect(passage)



class TIntersection(Intersection):
    def __init__(self, passage):
        super().__init__(passage)
        self.exits[2] = NoExit


class CornerLeft(Intersection):
    def __init__(self, passage):
        super().__init__(passage)
        self.exits[2] = self.exits[3] = NoExit


class CornerRight(Intersection):
    def __init__(self, passage):
        super().__init__(passage)
        self.exits[1] = self.exits[2] = NoExit


class SideLeft(Intersection):
    def __init__(self, passage):
        super().__init__(passage)
        self.exits[3] = NoExit


class SideRight(Intersection):
    def __init__(self, passage):
        super().__init__(passage)
        self.exits[1] = NoExit


def _make_20_door_right():
    p1 = Passage(20)
    s = SideRight(p1)
    p2 = Passage(10)
    d = Door()
    s.exits[2] = p2
    s.exits[3] = d
    s.connect(d)
    s.connect(p2)
    return p1


def _make_20_door_left():
    p1 = Passage(20)
    s = SideLeft(p1)
    p2 = Passage(10)
    d = Door()
    s.exits[1] = d
    s.exits[2] = p2
    s.connect(d)
    s.connect(p2)
    return p1


def _make_20_door():
    p1 = Passage(20)
    d = Door()
    p1.connect(d)
    return p1


class Passage(MapObject):
    TABLE = {
        1: lambda: Passage(30),
        2: lambda: Passage(30),
        3: _make_20r,
        4: _make_20l,
    }

    def __init__(self, length):
        super().__init__()
        self.length = length

    @classmethod
    def roll(cls):
        pass


class Door(Passage):
    def __init__(self):
        super().__init__(0)

