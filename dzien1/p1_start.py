from PyQt6.QtWidgets import QApplication, QWidget

import sys  # komentarz

app = QApplication(sys.argv)  # ([]) -bez argumentów

window = QWidget()
window.show()

app.exec()
