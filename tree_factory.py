# tree_factory.py
from container import TreeContainer
from leaf import TreeLeaf
from abstract_factory import AbstractFactory

class TreeFactory(AbstractFactory):
    def __init__(self, icon_family):
        self.icon_family = icon_family

    def create_container(self, name, level):
        return TreeContainer(self.icon_family.get_icon('container'), name, level)

    def create_leaf(self, name):
        return TreeLeaf(self.icon_family.get_icon('leaf'), name)
