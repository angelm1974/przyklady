from PyQt6.QtWidgets import QApplication, QMainWindow, QSlider,QDial
from PyQt6.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moja aplikacja")
        
 

        self.widget = QSlider()
        self.widget.setMinimum(-20)
        self.widget.setMaximum(20)
         
         

        self.widget.valueChanged.connect(self.zmiana_wartosci)
        self.widget.sliderPressed.connect(self.slider_zlapany)
        self.widget.sliderReleased.connect(self.slider_puszczony)
 
        self.setCentralWidget(self.widget)

    def zmiana_wartosci(self, p):
       # print(self.widget.text)
        print("pozycja -", p)

    def slider_zlapany(self):
       # print(self.widget.text)
        print("Złapany")
    
    def slider_puszczony(self):
       # print(self.widget.text)
        print("Puszczony")
    
    


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
