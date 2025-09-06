from PySide2.QtWidgets import QMainWindow, QApplication
from mainwindow import MainWindow
import sys

# Aplicacion de Qt
app = QApplication()

#Crea nueva ventana de Qmainwindow
window = MainWindow()

# Se hace visible la ventana
window.show()

# Qt loop
sys.exit(app.exec_())