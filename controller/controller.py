from contract.imodel import IModel
from contract.iview import IView
from contract.icontroller import IController


class Controller(IController):
    # To be completed

    def __init__(self, model: IModel, view: IView):
        pass

    def setView(self, view: IView) -> None:
        pass

    def setModel(self, model: IModel) -> None:
        pass

    def start(self) -> None:
        pass
