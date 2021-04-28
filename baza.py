#from PyQt6.QtCore import QSize, Qt
#from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from mainwindow import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
db = QSqlDatabase("QSQLITE")
db.setDatabaseName("./baza/chinook.db")
db.open()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.btnSave.clicked.connect(self.zapisz_do_bazy)

        self.model = QSqlTableModel(db=db)
        self.tableView.setModel(self.model)
        self.model.setTable("artists")
        self.model.select()
        # self.setCentralWidget(self.table)

    def zapisz_do_bazy(self):
        # f = open("plik.txt", "a")
        # tekst = self.plainTextEdit.toPlainText()
        # f.write(tekst)
        # f.close()
        parametr_Name = self.plainTextEdit.toPlainText()
        sql_insert = f"""INSERT INTO artists (Name) 
                      VALUES ('{parametr_Name}');"""

        wynik = db.exec(sql_insert)
        self.model.select()


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()
