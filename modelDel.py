import sys
import sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from modelDel_ui import Ui_Form3


#дочерняя форма удаления данных выбранного автомобиля из БД
class DelModel(QtWidgets.QWidget, Ui_Form3):
    def __init__(self, cell, parent=None):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        #задание словарей для вывода в комбобоксы
        self.dictType2 = {}
        self.dictModel2 = {}
        self.dictRegion2 = {}
        self.dictProiz2 = {}
        self.dictDiller2 = {}

        #инициализация комбобоксов на форме
        self.init()

        self.pushButtonDel.clicked.connect(self.delete)
        # инициализация загруженных значений из основного окна
        self.labelProiz.setText(parent[1])
        self.labelModel.setText(parent[3])
        self.labelType.setText(parent[2])
        self.labelRegion.setText(parent[5])
        self.labelDiller.setText(parent[6])
        self.labelYear.setText(parent[7])
        self.labelCena.setText(parent[4])
        self.labelDate.setText(parent[8])

    def init(self):
        # инициализация комбоксов на экране формы
        self.dictProiz2.clear()
        self.con = sqlite3.connect("Market.sqlite")
        cur = self.con.cursor()
        for value, key in cur.execute("SELECT * from Proiz").fetchall():
            self.dictProiz2[key] = value

        self.dictModel2.clear()
        self.con = sqlite3.connect("Market.sqlite")
        cur = self.con.cursor()
        for value, key in cur.execute("SELECT * from Model").fetchall():
            self.dictModel2[key] = value

        self.dictType2.clear()
        self.con = sqlite3.connect("Market.sqlite")
        cur = self.con.cursor()
        for value, key in cur.execute("SELECT * from Type").fetchall():
            self.dictType2[key] = value

        self.dictRegion2.clear()
        self.con = sqlite3.connect("Market.sqlite")
        cur = self.con.cursor()
        for value, key in cur.execute("SELECT * from Region").fetchall():
            self.dictRegion2[key] = value

        self.dictDiller2.clear()
        self.con = sqlite3.connect("Market.sqlite")
        cur = self.con.cursor()
        for value, key in cur.execute("SELECT * from Dillers").fetchall():
            self.dictDiller2[key] = value

    #функция удаления карточки автомобиля из БД
    def delete(self):
        try:
            self.con = sqlite3.connect("Market.sqlite")
            cur = self.con.cursor()
            self.proiz = self.dictProiz2[self.labelProiz.text()]
            self.model = self.dictModel2[self.labelModel.text()]
            self.type = self.dictType2[self.labelType.text()]
            self.region = self.dictRegion2[self.labelRegion.text()]
            self.diller = self.dictDiller2[self.labelDiller.text()]
            self.year = self.labelYear.text()
            self.cena = self.labelCena.text()
            self.date = self.labelDate.text()
            request = f"""DELETE FROM Cars WHERE ProizID = '{self.proiz}' AND TypeID = '{self.type}' 
            AND ModelID = '{self.model}' AND RegionID = '{self.region}' AND Price = '{self.cena}' 
            AND DillersID = '{self.diller}' AND DateBuy = '{self.date}' AND Year = '{self.year}'"""
            cur.execute(request)
            self.con.commit()
            self.con.close()
            self.close()
        except Exception:
            self.stroka = ('Нет автомобиля в БД')
            self.label_5.setText(self.stroka)


if __name__ == '__main__':
    delModel_app = QApplication(sys.argv)
    delModel_window = DelModel()
    delModel_window.show()
    sys.exit(delModel_app.exec_())