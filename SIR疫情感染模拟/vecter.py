class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def uniform(self, length):
        return Vector(-(self.x / self.length * length), -(self.y / self.length * length))

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    @property
    def length(self):
        return (self.x * self.x + self.y * self.y) ** 0.5

    def __sub__(self, other):
        return Vector(other.x - self.x, other.y - self.y)

    def __add__(self, other):
        return Vector(other.x + self.x, other.y + self.y)

    def copy(self):
        return Vector(self.x, self.y)
