import sys
import sqlite3
import re
import datetime

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog
from modelAdd_ui import Ui_Form

#дочерняя форма добавления данных нового автомобиля в БД
class AddModel(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pixmap = QPixmap()

        # считывание текущей системной даты для проверки при внесении данных в БД
        self.nowdate = datetime.datetime.now()
        self.nowdate = self.nowdate.strftime("%d-%m-%Y")
        self.labelbuydate.setText(str(self.nowdate))

        # задание словарей для вывода в комбобоксы
        self.dictType2 = {}
        self.dictModel2 = {}
        self.dictRegion2 = {}
        self.dictProiz2 = {}
        self.dictDiller2 = {}

        # инициализация комбобоксов на форме
        self.init()
        self.pushButton.clicked.connect(self.add)
        self.pushButtonJPG.clicked.connect(self.JPG)
        self.pushButtonTXT.clicked.connect(self.TXT)
        self.calendarWidget.clicked.connect(self.calendarclick)

        self.comboBoxProiz2.currentIndexChanged.connect(self.changeModel)
        self.comboBoxModel2.currentIndexChanged.connect(self.changeType)

    # создание словаря моделей по выбранному значению производителя
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

    # инициализация комбобоксов формы
    def init(self):
        self.dictProiz2.clear()
        self.comboBoxProiz2.clear()
        self.con = sqlite3.connect("Market.sqlite")
        cur = self.con.cursor()
        for value, key in cur.execute("SELECT * from Proiz").fetchall():
            self.dictProiz2[key] = value
        self.comboBoxProiz2.addItems(list(self.dictProiz2.keys()))

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

        self.dictDiller2.clear()
        self.comboBoxDiller2.clear()
        self.con = sqlite3.connect("Market.sqlite")
        cur = self.con.cursor()
        for value, key in cur.execute("SELECT * from Dillers").fetchall():
            self.dictDiller2[key] = value
        self.comboBoxDiller2.addItems(list(self.dictDiller2.keys()))

    # вывод выбранной даты на форму
    def calendarclick(self):
        self.date = self.calendarWidget.selectedDate()
        self.stroka = self.date.toString('dd-MM-yyyy')
        self.labelbuydate.setText(str(self.stroka))

    # выбор и загрузка новой картинки
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

    # функция отрисовка картинки
    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        self.pixmap = self.pixmap.scaled(270, 210)
        p.scale(0.5, 0.5)
        self.label_12.resize(self.pixmap.size())
        self.label_12.setPixmap(self.pixmap)
        p.end()

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

    # добавление новых данных автомобиля в БД
    def add(self):
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
            self.picture = './Picture/' + self.labelJPG.text()
            self.text = './TX/' + self.labeltext.text()

            int(self.cena)
            if int(self.year) < 1910 or int(self.year) > 2021:
                raise Exception
            if self.cena != '' and self.year != '':
                request = f"""SELECT * FROM Cars 
                WHERE ProizID = {self.proiz} AND TypeID = {self.type} AND ModelID = {self.model} AND RegionID = {self.region} 
                AND Price = {self.cena} AND ImagePath = '{self.picture}' AND TXTPath = '{self.text}' AND DillersID = {self.diller}
                AND DateBuy = '{self.date}' AND Year = '{self.year}'"""
                result = cur.execute(request).fetchone()
                if result == None:
                    request = f"""INSERT INTO Cars (ProizID, TypeID, ModelID, RegionID, Price, ImagePath, TXTPath,
                    DillersID, DateBuy, Year) VALUES('{self.proiz}', '{self.type}', '{self.model}', '{self.region}',
                    '{self.cena}', '{self.picture}', '{self.text}', '{self.diller}', '{self.date}', '{self.year}')"""
                    result = cur.execute(request).fetchone()
                    self.stroka = ('Автомобиль добавлен в базу!')
                    self.label_13.setText(self.stroka)
                    self.con.commit()
                else:
                    self.stroka = ('Такой автомобиль есть в базе!')
                    self.label_13.setText(self.stroka)
            #self.con.close()
            #self.close()
        except Exception:
            self.stroka = ('Не верно заполнена форма!')
            self.label_13.setText(self.stroka)


if __name__ == '__main__':
    addModel_app = QApplication(sys.argv)
    addModel_window = AddModel()
    addModel_window.show()
    sys.exit(addModel_app.exec_())