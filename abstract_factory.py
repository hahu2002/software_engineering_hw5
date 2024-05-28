# abstract_factory.py
from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_container( self , name , level ):
        pass

    @abstractmethod
    def create_leaf(self, name):
        pass
