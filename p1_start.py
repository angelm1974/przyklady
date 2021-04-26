from PyQt6.QtWidgets import QApplication, QWidget

import sys  # komentarz

app = QApplication(sys.argv)

window = QWidget()
window.show()

app.exec()
