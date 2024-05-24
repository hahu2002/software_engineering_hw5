class Container:
    def __init__(self, icon, name, level):
        self.icon = icon
        self.name = name
        self.level = level
        self.children = []

    def add(self, component):
        self.children.append(component)

    def draw(self):
        raise NotImplementedError

class TreeContainer(Container):
    def draw(self, prefix=""):
        connector = "├── " if prefix else ""
        print(f"{prefix}{connector}{self.icon} Tree Container: {self.name} at level {self.level}")
        new_prefix = prefix + ("│   " if prefix else "")
        for i, child in enumerate(self.children):
            if i == len(self.children) - 1:
                child.draw(new_prefix + "└── ")
            else:
                child.draw(new_prefix + "├── ")

class RectangleContainer(Container):
    def draw(self):
        newstring = f"Rectangle Container: {self.name} at level {self.level}"
        border = f"{self.icon}" + " " + "+" + "-" * ( len(newstring) + 2) + "+"
        print(border)
        print(f"{self.icon} | Rectangle Container: {self.name} at level {self.level} |")
        for child in self.children:
            child.draw( len(newstring) )
        print(border)
