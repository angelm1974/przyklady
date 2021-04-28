from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moja aplikacja")
        self.button_is_checked = True
        button = QPushButton("Kliknij")
        button.setCheckable(True)
        button.setFixedSize(200, 100)
        button.clicked.connect(self.button_klikniety)
        button.clicked.connect(self.button_przelaczony)
        self.setCentralWidget(button)
        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(600, 450))

    def button_klikniety(self):
        print("Kliknięto przycisk")

    def button_przelaczony(self, checked):
        self.button_is_checked = checked
        print("Zaznaczony przycisk? ", checked)
        


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
