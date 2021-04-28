from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moja aplikacja")

        self.button = QPushButton("Kliknij")
        self.button.setFixedSize(200, 100)
        self.button.clicked.connect(self.button_klikniety)

        self.setCentralWidget(self.button)
        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(600, 450))

    def button_klikniety(self):
        self.button.setText("Zostałem już kliknięty")
        self.button.setEnabled(False)
        print("Kliknięto przycisk")


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
