from contract.iview import IView
from contract.imodel import IModel
from contract.icontroller import IController


class View(IView):
    __model: IModel
    __controller: IController

    def setModel(self, model: IModel) -> None:
        self.__model = model

    def showMessage(self, message: str) -> None:
        print(message)

    def setController(self, controller: IController) -> None:
        self.__controller = controller

    def askUserChoice(self) -> int:
        userChoice = -1
        while 0 > userChoice or userChoice > 2:
            print("Entrez votre choix (0, 1 ou 2)")
            userChoice = int(input())
        return userChoice
