from dmg_generator import dice, room, passage


def _make_t():
    p = passage.Passage(10)
    passage.TIntersection(p)
    return p


def _make_4():
    p = passage.Passage(10)
    passage.Intersection(p)
    return p


class StartingArea():
    TABLE = {
        1: lambda: room.Square(20),
        2: lambda: room.Square(20),
        3: lambda: room.Square(40),
        4: lambda: room.Rectangle(80, 20),
        5: lambda: room.Rectangle(20, 40),
        6: lambda: room.Circle(40),
        7: lambda: room.Circle(40),
        8: lambda: room.Square(20),
        9: _make_t,
        10: _make_4,
    }

    @classmethod
    def roll(cls):
        idx = dice.d10()
        return cls.TABLE[idx]()
