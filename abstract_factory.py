from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_container(self, icon, name, level):
        pass

    @abstractmethod
    def create_leaf(self, name):
        pass
