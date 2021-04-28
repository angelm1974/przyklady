#from PyQt6.QtCore import QSize, Qt
#from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel
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
        
        query='''SELECT EmployeeId, LastName, FirstName FROM employees;'''    
        self.model = QSqlQueryModel()
        self.model.setQuery(query,db)
        self.tableView.setModel(self.model)


    def zapisz_do_bazy(self):

        parametr_Name = self.plainTextEdit.toPlainText()
        query=f'''SELECT EmployeeId, LastName, FirstName
                    FROM employees 
                    WHERE LastName Like '{parametr_Name}%';'''
     
        self.model.setQuery(query,db)
        self.tableView.setModel(self.model)


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()
