import sys
from PyQt5.QtWidgets import QApplication
from view import View
from controller import Controller
from model import Model

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Model()
    controller = Controller(model)
    window = View(controller)
    sys.exit(app.exec_())