from abc import ABC, abstractmethod


class IObservador(ABC):
    @abstractmethod
    def renderizar(self, tela, usuario):
        pass
