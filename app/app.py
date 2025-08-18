import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton , QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QUrl , QResource , QEventLoop
from PySide6.QtCore import QResource
from PySide6.QtGui import QPixmap , QGuiApplication
from PySide6.QtMultimedia import QSoundEffect



import app.resource.resources
from app.controller.DiceController import DiceController


class App(object):

    def __init__(self):

        self.__controller = DiceController()

        self.app = QApplication(sys.argv)
        self.loader = QUiLoader()
        self.window = self.loader.load("app/views/MainWindow.ui")

        self.__initiate_signals()
        self.__connect_signals()

    def __initiate_signals(self):

        self.roll_once_button: QPushButton = self.window.findChild(
            QPushButton, "RollOnceButton"
        )
        self.roll_twice_button: QPushButton = self.window.findChild(
            QPushButton, "RollTwiceButton"
        )

        self.first_dice: QLabel = self.window.findChild(QLabel, "FirstDicePixmap")
        self.second_dice: QLabel = self.window.findChild(QLabel, "SecondDicePixmap")

    def __connect_signals(self):
        self.roll_once_button.clicked.connect(lambda: self.__roll_once())
        self.roll_twice_button.clicked.connect(lambda: self.__roll_twice())

    def __roll_once(self):
        result = self.__controller.roll_dice_once()
        self.first_dice.setPixmap(QPixmap(f":/Dices/assets/diceGreenAlt{result}.png"))
        

    def __roll_twice(self):
        result = self.__controller.roll_dice_twice()
        self.first_dice.setPixmap(
            QPixmap(f":/Dices/assets/diceGreenAlt{result[0]}.png")
        )
        self.second_dice.setPixmap(
            QPixmap(f":/Dices/assets/diceGreenAlt{result[1]}.png")
        )

    def run(self):
        self.window.show()
        sys.exit(self.app.exec())
