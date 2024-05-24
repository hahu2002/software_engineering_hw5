class Leaf:
    def __init__(self, icon, name):
        self.icon = icon
        self.name = name

    def draw(self):
        raise NotImplementedError

class TreeLeaf(Leaf):
    def draw(self, prefix=""):
        print(f"{prefix}{self.icon} Tree Leaf: {self.name}")

class RectangleLeaf(Leaf):
    def draw(self , length = 0):
        newstring = f" ──── Rectangle Leaf: {self.name}"
        printstring = f"{self.icon}" + " |" + newstring + " " * ( length - len(newstring) + 2 ) + "|"
        print(printstring)
