from PySide6.QtWidgets import QApplication

import sys
sys.dont_write_bytecode = True

from app.app import App

app = App()

app.run()