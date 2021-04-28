from mainwindow import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.btnSave.clicked.connect(self.zapisz_do_pliku)

    def zapisz_do_pliku(self):
        f = open("plik.txt", "a")
        tekst = self.plainTextEdit.toPlainText()
        f.write(tekst)
        f.close()
        print("zapisano")

  
app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()
