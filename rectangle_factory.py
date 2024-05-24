from container import RectangleContainer
from leaf import RectangleLeaf
from abstract_factory import AbstractFactory

class RectangleFactory(AbstractFactory):
    def __init__(self, icon_family):
        self.icon_family = icon_family

    def create_container(self, icon, name, level):
        return RectangleContainer(self.icon_family.get_icon('container'), name, level)

    def create_leaf(self, name):
        return RectangleLeaf(self.icon_family.get_icon('leaf'), name)
