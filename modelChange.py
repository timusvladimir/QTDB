import sys
import sqlite3
import re
import datetime

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QApplication, QFileDialog
from modelChange_ui import Ui_Form2

#дочерняя форма редактирования данных выбранного автомобиля в БД
class ChangeModel(QtWidgets.QWidget, Ui_Form2):
    def __init__(self, cell, parent=None):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.pixmap = QPixmap()

        #считывание текущей системной даты для проверки при внесении данных в БД
        self.nowdate = datetime.datetime.now()
        self.nowdate = self.nowdate.strftime("%d-%m-%Y")
        self.labelnowdate.setText(str(self.nowdate))
        self.labelbuydate.setText(str(self.nowdate))

        # задание словарей для вывода в комбобоксы
        self.dictType2 = {}
        self.dictModel2 = {}
        self.dictRegion2 = {}
        self.dictProiz2 = {}
        self.dictDiller2 = {}

        # инициализация загруженных значений из основного окна
        self.IDkey = parent[0]
        self.proizkey = parent[1]
        self.modelkey = parent[3]
        self.typekey = parent[2]
        self.regionkey = parent[5]
        self.dillerkey = parent[6]
        self.year = parent[7]
        self.cena = parent[4]
        self.date = parent[8]

        # инициализация комбобоксов на форме
        self.init()
        self.pushButtonChange.clicked.connect(self.update)
        self.pushButtonJPG.clicked.connect(self.JPG)
        self.pushButtonTXT.clicked.connect(self.TXT)
        self.comboBoxProiz2.currentIndexChanged.connect(self.changeModel)
        self.comboBoxModel2.currentIndexChanged.connect(self.changeType)

        self.calendarWidget.clicked.connect(self.calendarclick)

    def init(self):
        self.labelID.setText(self.IDkey)

        #загрузка картинки и текста выбранного автомобиля
        request = f"""SELECT * FROM Cars WHERE ID = {self.IDkey}"""
        self.con = sqlite3.connect("Market.sqlite")
        cur = self.con.cursor()
        result = cur.execute(request).fetchone()
        try:
            self.pixmap = QPixmap(result[6])
            self.repaint()

            self.pathjpg = re.split(r"/", result[6])
            self.labelJPG.setText(str(self.pathjpg[-1]))

            self.pathtxt = re.split(r"/", result[7])
            self.labeltext.setText(str(self.pathtxt[-1]))

            self.filetxt = open(result[7], 'r', encoding='utf8')
            self.txt = self.filetxt.read()
            self.textBrowser.setText(self.txt)
            self.filetxt.close()

            self.stroka = ('Вывод рисунка и технических данных об автомобиле!')
            self.label_13.setText(self.stroka)
        except:
            self.stroka = ('Отсутствуют данные в БД!')
            self.label_13.setText(self.stroka)

        #инициализация комбобоксов формы
        self.dictProiz2.clear()
        self.comboBoxProiz2.clear()
        self.con = sqlite3.connect("Market.sqlite")
        cur = self.con.cursor()
        for value, key in cur.execute("SELECT * from Proiz").fetchall():
            self.dictProiz2[key] = value
        self.comboBoxProiz2.addItems(list(self.dictProiz2.keys()))
        self.comboBoxProiz2.setCurrentIndex(self.dictProiz2[self.proizkey] - 1)

        self.dictModel2.clear()
        self.comboBoxModel2.clear()
        cur = self.con.cursor()
        key = self.comboBoxProiz2.currentText()
        proiz = self.dictProiz2[key]
        for value, key in cur.execute(f"""SELECT Model.ID, Model.Model FROM Model 
                                                     LEFT JOIN vzaim ON Model.ID = vzaim.id_model
                                                     WHERE vzaim.id_proiz = '{proiz}'""").fetchall():
            self.dictModel2[key] = value
        self.comboBoxModel2.addItems(list(self.dictModel2.keys()))
        self.comboBoxModel2.setCurrentText(self.modelkey)

        self.dictType2.clear()
        self.comboBoxType2.clear()
        cur = self.con.cursor()
        key = self.comboBoxModel2.currentText()
        model = self.dictModel2[key]
        for value, key in cur.execute(f"""SELECT Type.ID, Type.Type FROM Type 
                                                             LEFT JOIN vzaimType ON Type.ID = vzaimType.id_type
                                                             WHERE vzaimType.id_model = '{model}'""").fetchall():
            self.dictType2[key] = value
        self.comboBoxType2.addItems(list(self.dictType2.keys()))

        self.dictRegion2.clear()
        self.comboBoxRegion2.clear()
        self.con = sqlite3.connect("Market.sqlite")
        cur = self.con.cursor()
        for value, key in cur.execute("SELECT * from Region").fetchall():
            self.dictRegion2[key] = value
        self.comboBoxRegion2.addItems(list(self.dictRegion2.keys()))
        self.comboBoxRegion2.setCurrentIndex(self.dictRegion2[self.regionkey] - 1)

        self.dictDiller2.clear()
        self.comboBoxDiller2.clear()
        self.con = sqlite3.connect("Market.sqlite")
        cur = self.con.cursor()
        for value, key in cur.execute("SELECT * from Dillers").fetchall():
            self.dictDiller2[key] = value
        self.comboBoxDiller2.addItems(list(self.dictDiller2.keys()))
        self.comboBoxDiller2.setCurrentIndex(self.dictDiller2[self.dillerkey] - 1)

    #выбор и загрузка новой картинки
    def JPG(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '.\Picture', 'Картинка (*.jpg)')[0]
        self.pathjpg = re.split(r"/", self.filename)
        self.labelJPG.setText(str(self.pathjpg[-1]))
        try:
            self.pixmap = QPixmap(self.filename)
            self.repaint()
        except:
            self.stroka = ('Ошибка открытия файла!')
            self.label_13.setText(self.stroka)

    # выбор и загрузка нового текста
    def TXT(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Выбрать текст', '.\TX', 'Текст (*.txt)')[0]
        self.pathtxt = re.split(r"/", self.filename)
        self.labeltext.setText(str(self.pathtxt[-1]))
        try:
            filetxt = open(self.filename, 'r', encoding='utf8')
            txt = filetxt.read()
            self.textBrowser.setText(txt)
            filetxt.close()
        except:
            self.stroka = ('Ошибка открытия файла!')
            self.label_13.setText(self.stroka)

    #функция отрисовка картинки
    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        self.pixmap = self.pixmap.scaled(270, 210)
        p.scale(0.5, 0.5)
        self.label_12.resize(self.pixmap.size())
        self.label_12.setPixmap(self.pixmap)
        p.end()

    #вывод выбранной даты на форму
    def calendarclick(self):
        self.date = self.calendarWidget.selectedDate()
        self.stroka = self.date.toString('dd-MM-yyyy')
        self.labelbuydate.setText(str(self.stroka))

    #создание словаря моделей по выбранному значению производителя
    def changeModel(self):
        self.dictModel2.clear()
        self.comboBoxModel2.clear()
        cur = self.con.cursor()
        key = self.comboBoxProiz2.currentText()
        proiz = self.dictProiz2[key]
        for value, key in cur.execute(f"""SELECT Model.ID, Model.Model FROM Model 
                                      LEFT JOIN vzaim ON Model.ID = vzaim.id_model
                                      WHERE vzaim.id_proiz = '{proiz}'""").fetchall():
            self.dictModel2[key] = value
        self.comboBoxModel2.addItems(list(self.dictModel2.keys()))
        self.changeType()

    # создание словаря типов по выбранному значению модели
    def changeType(self):
        self.dictType2.clear()
        self.comboBoxType2.clear()
        cur = self.con.cursor()
        try:
            key = self.comboBoxModel2.currentText()
            model = self.dictModel2[key]
            for value, key in cur.execute(f"""SELECT Type.ID, Type.Type FROM Type 
                                          LEFT JOIN vzaimType ON Type.ID = vzaimType.id_type
                                          WHERE vzaimType.id_model = '{model}'""").fetchall():
                self.dictType2[key] = value
            self.comboBoxType2.addItems(list(self.dictType2.keys()))
        except:
            pass

    #обновление отредактированных данных автомобиля в БД
    def update(self):
        try:
            self.con = sqlite3.connect("Market.sqlite")
            cur = self.con.cursor()

            self.proiz = self.dictProiz2[self.comboBoxProiz2.currentText()]
            self.model = self.dictModel2[self.comboBoxModel2.currentText()]
            self.type = self.dictType2[self.comboBoxType2.currentText()]
            self.region = self.dictRegion2[self.comboBoxRegion2.currentText()]
            self.diller = self.dictDiller2[self.comboBoxDiller2.currentText()]
            self.year = self.lineEditYear.text()
            self.cena = self.lineEditCena.text()
            self.date = self.labelbuydate.text()
            self.ImagePath = './Picture/' + self.labelJPG.text()
            self.TXTPath = './TX/' + self.labeltext.text()

            int(self.cena)
            if int(self.year) < 1910 or int(self.year) > 2021:
                raise Exception

            if self.cena != '' and self.year != '':
                request = f"""UPDATE cars SET ProizID = '{self.proiz}', TypeID = '{self.type}', ModelID = '{self.model}',
                RegionID = '{self.region}', Price = '{self.cena}', ImagePath = '{self.ImagePath}', 
                TXTPath = '{self.TXTPath}', DillersID = '{self.diller}', DateBuy = '{self.date}', Year = '{self.year}' 
                WHERE ID = {self.IDkey}"""
                cur.execute(request)
            self.con.commit()
            self.con.close()
            self.close()

        except Exception:
            self.stroka = ('Не верно заполнена форма!')
            self.label_13.setText(self.stroka)


if __name__ == '__main__':
    changeModel_app = QApplication(sys.argv)
    changeModel_window = ChangeModel()
    changeModel_window.show()
    sys.exit(changeModel_app.exec_())