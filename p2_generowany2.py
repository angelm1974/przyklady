
from PyQt6 import QtCore, QtGui, QtWidgets,uic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("interfejs_nr1.ui",self)


app=QtWidgets.QApplication([])
window=MainWindow() 
window.show()
app.exec()