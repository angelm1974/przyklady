import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDial, QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moja aplikacja")
        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(0.5)
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)
        self.setCentralWidget(widget)
    def value_changed(self, i):
        print(i)
    def slider_position(self, p):
        print("pozycja", p)
    def slider_pressed(self):
        print("nacisnięty!")
    def slider_released(self):
        print("zwolniony")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()