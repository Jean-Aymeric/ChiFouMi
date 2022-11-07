import random

from contract.imodel import IModel
from contract.iview import IView
from contract.icontroller import IController


class Controller(IController):
    __view: IView
    __model: IModel

    def __init__(self, model: IModel, view: IView):
        self.setModel(model)
        self.setView(view)
        self.__view.setModel(self.__model)
        self.__view.setController(self)

    def setView(self, view: IView) -> None:
        self.__view = view

    def setModel(self, model: IModel) -> None:
        self.__model = model

    def start(self) -> None:
        self.__model.setComputerChoice(random.randint(0, 2))
        self.__model.setUserChoice(self.__view.askUserChoice())
        self.__view.showMessage("Votre choix : " + self.__model.getChoiceByNumber(self.__model.getUserChoice()))
        self.__view.showMessage("Mon choix : " + self.__model.getChoiceByNumber(self.__model.getComputerChoice()))

        if self.__model.getComputerChoice() == self.__model.getUserChoice():
            self.__view.showMessage("Egalité")
        elif (self.__model.getUserChoice() - self.__model.getComputerChoice() + 3) % 3 == 2:
            self.__view.showMessage("Perdu")
        else:
            self.__view.showMessage("Gagné")
