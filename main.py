from controller.controller import Controller
from model.model import Model
from view.view import View


controller = Controller(Model(), View())
controller.start()
