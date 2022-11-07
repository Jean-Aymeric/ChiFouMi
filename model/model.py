import random

from contract.imodel import IModel


class Model(IModel):
    __computerChoice: int
    __userChoice: int
    __choices: [str]

    def __init__(self):
        self.__choices = ["Pierre", "Feuille", "Ciseaux"]

    def getComputerChoice(self) -> int:
        return self.__computerChoice

    def setComputerChoice(self, computerChoice: int):
        self.__computerChoice = computerChoice

    def getUserChoice(self) -> int:
        return self.__userChoice

    def setUserChoice(self, userChoice) -> None:
        self.__userChoice = userChoice

    def getChoiceByNumber(self, number: int) -> str:
        return self.__choices[number]
