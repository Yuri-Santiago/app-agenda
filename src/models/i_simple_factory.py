from abc import ABC, abstractmethod


class ISimpleFactory(ABC):
    @abstractmethod
    def criar(self, dados, usuario):
        pass
