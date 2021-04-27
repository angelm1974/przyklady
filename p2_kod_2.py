
from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt6.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moja aplikacja")
        self.setFixedSize(QSize(600, 450))

        widget = QCheckBox("Mój checkbox")
        widget.setCheckState(Qt.CheckState.Checked)
        widget.stateChanged.connect(self.pokaz_stan)
        self.setCentralWidget(widget)

    def pokaz_stan(self, s, a):
        print(s == Qt.CheckState.Checked)
        print(a)
        print(s)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
