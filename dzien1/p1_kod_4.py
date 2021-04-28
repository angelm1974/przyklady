from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moja aplikacja")
        button = QPushButton("Kliknij")
        button.setFixedSize(200, 100)
        self.setCentralWidget(button)
        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(600, 450))


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
