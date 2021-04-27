from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox
from PyQt6.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moja aplikacja")
        
 

        self.widget = QComboBox()
        self.widget.addItems(['Mariusz','Olek','Roman','Jan'])
 
        self.widget.currentIndexChanged.connect(self.zmiana_indexu)
        self.widget.currentTextChanged.connect(self.zmiana_tekstu)
        self.setCentralWidget(self.widget)

    def zmiana_indexu(self, i):
        print(self.widget.itemText(i))
        print(i)
    
    def zmiana_tekstu(self, t):
        print(t)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
