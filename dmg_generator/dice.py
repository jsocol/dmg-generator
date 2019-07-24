import functools
import operator
import random


__all__ = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20']


class D():
    """A die.

    Simulates an n-sided die, e.g. to create a d6, pass 6:

    >>> d4, d6, d8, d10, d12, d20 = D(4), D(6), D(8), D(10), D(12), D(20)

    To roll, you can call d6.roll() (or just d6()):

    >>> d6.roll()
    <<< 4
    >>> d6()
    <<< 2

    Or even just:

    >>> d6
    <<< 3

    (NB: I'm sure I owe someone an apology for that.)

    Need to roll with (dis) advantage?

    >>> d20, d20
    <<< (20, 13)

    But the best way to use these is to do math with dice. For example, if you
    need to roll 3d8 + 4:

    >>> 3 * d8 + 4
    <<< 22

    Or add dice:

    >>> d8 + d4
    <<< 9

    Remember these are random rolls, so the examples above are not guaranteed.

    """

    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        """Roll the dice!"""
        return random.randint(1, self.sides)

    def __call__(self):
        return self.roll()

    def __mul__(self, n):
        """Roll n (an integer) number of dice."""
        return functools.reduce(operator.add, [self.roll() for _ in range(n)])

    __rmul__ = __mul__

    def __add__(self, n):
        """Add an integer or another die."""
        if isinstance(n, D):
            n = n.roll()
        return n + self.roll()

    __radd__ = __add__

    def __repr__(self):
        return str(self.roll())


d4, d6, d8, d10, d12, d20 = D(4), D(6), D(8), D(10), D(12), D(20)
