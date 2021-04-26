from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt
from random import choice

tytuly_okna = [
    'Moja aplikacja',
    'Mój soft',
    'Mój soft 2',
    'Aplikacja test',
    'Przykład',
    'Koniec',
    'Coś niespodziewanego'
]


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

        self.windowTitleChanged.connect(self.zmiana_tytulu)
        

    def button_klikniety(self):
        nowy_tytul_okna = choice(tytuly_okna)
        self.setWindowTitle(nowy_tytul_okna)

        print("Kliknięto przycisk")

    def zmiana_tytulu(self, tytul_okna):
        print(f"Tytuł się zmienił: {tytul_okna}")

        if tytul_okna == 'Koniec':
            self.button.setDisabled(True)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
