from contract.iview import IView
from contract.imodel import IModel
from contract.icontroller import IController


class View(IView):
    def setModel(self, model: IModel) -> None:
        pass

    def showMessage(self, message: str) -> None:
        pass

    def setController(self, controller: IController) -> None:
        pass

    def unTruc(self):
        pass