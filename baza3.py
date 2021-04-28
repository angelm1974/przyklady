import psycopg2
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel
from mainwindow import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QSize

connection = psycopg2.connect(host='localhost', user='postgres', password='Nana@1974', port ='5432', database='szkolenie')

db = QSqlDatabase.addDatabase("QPSQL")
db.setHostName('localhost')
db.setUserName('postgres')
db.setPassword('Nana@1974')
db.setDatabaseName('szkolenie')
db.open()
cursor = connection.cursor()

cursor.execute("Select Version();")
record =cursor.fetchone()
print("Podłączyleś się:",record)



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.btnSave.clicked.connect(self.zapisz_do_bazy)

        self.model = QSqlTableModel(db=db)
        self.tableView.setModel(self.model)
        self.model.setTable("test")
        #self.model.sort(2,Qt.SortOrder)
        self.tableView.setSortingEnabled(True)
        self.tableView.sortByColumn(1, Qt.SortOrder(1))
        self.model.select()
        
    def zapisz_do_bazy(self):

        parametr_Name = self.plainTextEdit.toPlainText()
        sql_insert = f"""INSERT INTO public.test(
                            nazwisko, imie)
                            VALUES ('{parametr_Name}', 'no name');"""

        wynik = db.exec(sql_insert)
        self.model.select()


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()
