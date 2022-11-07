from abc import ABC, abstractmethod
from contract.icontroller import IController
from contract.imodel import IModel


class IView(ABC):
    @abstractmethod
    def showMessage(self, message: str) -> None:
        pass

    @abstractmethod
    def setController(self, controller: IController) -> None:
        pass

    @abstractmethod
    def setModel(self, model: IModel) -> None:
        pass
