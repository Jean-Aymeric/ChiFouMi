import random
from abc import ABC, abstractmethod


class IModel(ABC):
    @abstractmethod
    def getComputerChoice(self) -> int:
        pass

    @abstractmethod
    def setComputerChoice(self, computerChoice: int):
        pass

    @abstractmethod
    def getUserChoice(self) -> int:
        pass

    @abstractmethod
    def setUserChoice(self, userChoice) -> None:
        pass

    @abstractmethod
    def getChoiceByNumber(self, number: int) -> str:
        pass
