from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox
from PyQt6.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moja aplikacja")
        
 

        self.widget = QSpinBox()
        self.widget.setMinimum(-20)
        self.widget.setMaximum(20)
        self.widget.setSuffix("C")
        self.widget.setSingleStep(2)

        self.widget.valueChanged.connect(self.zmiana_wartosci)
 
        self.setCentralWidget(self.widget)

    def zmiana_wartosci(self, i):
       # print(self.widget.text)
        print(i)



app = QApplication([])
window = MainWindow()
window.show()
app.exec()
