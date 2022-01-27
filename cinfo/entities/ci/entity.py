from abc import ABC 
from abc import abstractmethod


class Entity(ABC):
    def __init__(self):
        self.entities = {self.name: object_address)}

    @abstractmethod
    def define_parser(self):
        pass