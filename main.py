from PyQt5.QtWidgets import QApplication, QDialog
from ui_main import *

app = QApplication([])

window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)
window.show()

app.exec_()
