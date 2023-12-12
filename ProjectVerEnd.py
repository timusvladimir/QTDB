# -*- coding: utf-8 -*-
import sys
import sqlite3
import time

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QSplashScreen, QProgressBar
from PyQt5.QtGui import QPainter, QPixmap

from searchcars_ui import Ui_MainWindow
import modelAdd
import modelChange
import modelDel

#основное окно
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("Market.sqlite")

        # задание словарей для вывода в комбобоксы
        self.dictType = {}
        self.dictModel = {}
        self.dictRegion = {}
        self.dictProiz = {}

        self.pushButtonFilter.clicked.connect(self.filter)
        self.pushButtonClsFilter.clicked.connect(self.install)

        self.pushButtonAdd.clicked.connect(self.modelAdd)
        self.pushButtonChange.clicked.connect(self.modelChange)
        self.pushButtonDel.clicked.connect(self.modelDel)
        self.pushButtonUpdate.clicked.connect(self.install)

        self.comboBoxProizvod.currentIndexChanged.connect(self.ChangedComboProizvod)
        self.comboBoxModel.currentIndexChanged.connect(self.ChangedComboModel)
        self.comboBoxType.currentIndexChanged.connect(self.ChangedComboType)
        self.comboBoxRegion.currentIndexChanged.connect(self.ChangedComboRegion)
        self.tableWidget.cellClicked.connect(self.cellClick)

        self.tabWidget.tabBarClicked.connect(self.tab2)

        #инициализация переменных программы и основной формы
        self.install()

        self.cell = []
        self.row, self.col = 0, 0
        self.pixmap = QPixmap()

    #функция скрытия комбобоксов при филтрации
    def ChangedComboProizvod(self):
        self.comboBoxModel.setEnabled(False)
        self.comboBoxType.setEnabled(False)
        self.comboBoxRegion.setEnabled(False)

    # функция скрытия комбобоксов при филтрации
    def ChangedComboModel(self):
        self.comboBoxType.setEnabled(False)
        self.comboBoxRegion.setEnabled(False)
        self.comboBoxProizvod.setEnabled(False)

    # функция скрытия комбобоксов при филтрации
    def ChangedComboType(self):
        self.comboBoxModel.setEnabled(False)
        self.comboBoxRegion.setEnabled(False)
        self.comboBoxProizvod.setEnabled(False)

    # функция скрытия комбобоксов при филтрации
    def ChangedComboRegion(self):
        self.comboBoxType.setEnabled(False)
        self.comboBoxModel.setEnabled(False)
        self.comboBoxProizvod.setEnabled(False)

    #инициализация комбобоксов формы поиска
    def initcombobox(self):
        self.dictProiz.clear()
        self.comboBoxProizvod.clear()
        self.con = sqlite3.connect("Market.sqlite")
        cur = self.con.cursor()
        self.dictProiz[''] = ''
        for value, key in cur.execute("SELECT * from Proiz").fetchall():
            self.dictProiz[key] = value
        self.comboBoxProizvod.addItems(list(self.dictProiz.keys()))

        self.dictModel.clear()
        self.comboBoxModel.clear()
        self.con = sqlite3.connect("Market.sqlite")
        cur = self.con.cursor()
        self.dictModel[''] = ''
        for value, key in cur.execute("SELECT * from Model").fetchall():
            self.dictModel[key] = value
        self.comboBoxModel.addItems(list(self.dictModel.keys()))

        self.dictType.clear()
        self.comboBoxType.clear()
        self.con = sqlite3.connect("Market.sqlite")
        cur = self.con.cursor()
        self.dictType[''] = ''
        for value, key in cur.execute("SELECT * from Type").fetchall():
            self.dictType[key] = value
        # lenght = len(self.dictType)
        self.comboBoxType.addItems(list(self.dictType.keys()))

        self.dictRegion.clear()
        self.comboBoxRegion.clear()
        self.con = sqlite3.connect("Market.sqlite")
        cur = self.con.cursor()
        self.dictRegion[''] = ''
        for value, key in cur.execute("SELECT * from Region").fetchall():
            self.dictRegion[key] = value
        self.comboBoxRegion.addItems(list(self.dictRegion.keys()))

    # функция отрисовка картинки
    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        self.pixmap = self.pixmap.scaled(300, 200)
        #p.drawPixmap(50, 420, self.pixmap)
        p.scale(0.5, 0.5)
        self.label_12.resize(self.pixmap.size())
        self.label_12.setPixmap(self.pixmap)
        p.end()

    # функция основной инсталляци формы
    def install(self):
        self.initcombobox()
        self.comboBoxType.setEnabled(True)
        self.comboBoxModel.setEnabled(True)
        self.comboBoxRegion.setEnabled(True)
        self.comboBoxProizvod.setEnabled(True)
        self.tableWidget.clear()
        self.cell = []
        self.row, self.col = 0, 0
        try:
            self.con = sqlite3.connect("Market.sqlite")
            self.count = 0
            request = """SELECT Cars.ID, Proiz.Proiz, Type.Type, Model.Model, Price, Region.Region, 
                      Dillers.Name, Year, DateBuy
                      FROM Cars 
                      LEFT JOIN Proiz ON Cars.ProizID = Proiz.ID
                      LEFT JOIN Type ON Cars.TypeID = Type.ID
                      LEFT JOIN Model ON Cars.ModelID = Model.ID
                      LEFT JOIN Region ON Cars.RegionID = Region.ID
                      LEFT JOIN Dillers ON Cars.DillersID = Dillers.ID
                      """
            cur = self.con.cursor()
            result = cur.execute(request).fetchall()
            self.tableWidget.setColumnCount(len(result[0]))
            self.tableWidget.setHorizontalHeaderLabels(["ID", "Производитель", "Тип", "Название", "Цена", "Регион",
                                                        "Диллер", "Год", "Дата покупки"])
            self.tableWidget.setRowCount(len(result))
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                self.count += 1
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.setSortingEnabled(True)
            if self.count != 0:
                self.stroka = ('Нашлось ' + str(self.count) + ' записей!')
                self.statusBar().showMessage(self.stroka)
        except Exception:
            self.tableWidget.clear()
            self.stroka2 = ('Не найдено не одной записи!')
            self.statusBar().showMessage(self.stroka2)
        self.con.close()

    #функция выбора данных из БД при выделении строки в таблице
    def cellClick(self, row, col):
        self.row = row
        self.col = col
        #self.row2 = 0
        #self.row2 = row + 1
        self.tableWidget.selectRow(self.tableWidget.currentRow())

        self.ID = self.tableWidget.item(row, 0).text()
        request = f"""SELECT Cars.ImagePath, Cars.TXTPath
                      FROM Cars 
                      WHERE ID = {self.ID}
                      """
        self.con = sqlite3.connect("Market.sqlite")
        cur = self.con.cursor()
        result = cur.execute(request).fetchone()
        try:
            self.pixmap = QPixmap(result[0])
            self.repaint()

            self.filetxt = open(result[1], 'r', encoding='utf8')
            self.txt = self.filetxt.read()
            self.textBrowser.setText(self.txt)
            self.filetxt.close()

            self.stroka = ('Вывод рисунка и технических данных об автомобиле!')
            self.statusBar().showMessage(self.stroka)
        except:
            self.stroka = ('Отсутствуют данные в БД!')
            self.statusBar().showMessage(self.stroka)
            self.textBrowser.clear()

    #функция фильтрации данных в окне таблицы
    def filter(self):
        self.con = sqlite3.connect("Market.sqlite")
        self.tableWidget.clear()
        self.cell = []
        self.row, self.col = 0, 0
        try:
            self.count = 0
            self.proiz = self.dictProiz.get(self.comboBoxProizvod.currentText())
            self.type = self.dictType.get(self.comboBoxType.currentText())
            self.model = self.dictModel.get(self.comboBoxModel.currentText())
            self.region = self.dictRegion.get(self.comboBoxRegion.currentText())
            if self.proiz != '':
                request = f"""SELECT Cars.ID, Proiz.Proiz, Type.Type, Model.Model, Price, Region.Region, Dillers.Name, DateBuy
                         FROM Cars 
                         LEFT JOIN Proiz ON Cars.ProizID = Proiz.ID
                         LEFT JOIN Type ON Cars.TypeID = Type.ID
                         LEFT JOIN Model ON Cars.ModelID = Model.ID
                         LEFT JOIN Region ON Cars.RegionID = Region.ID
                         LEFT JOIN Dillers ON Cars.DillersID = Dillers.ID
                         WHERE Cars.ProizID = {self.proiz}"""
            elif self.model != '':
                request = f"""SELECT Cars.ID, Proiz.Proiz, Type.Type, Model.Model, Price, Region.Region, Dillers.Name, DateBuy
                                         FROM Cars 
                                         LEFT JOIN Proiz ON Cars.ProizID = Proiz.ID
                                         LEFT JOIN Type ON Cars.TypeID = Type.ID
                                         LEFT JOIN Model ON Cars.ModelID = Model.ID
                                         LEFT JOIN Region ON Cars.RegionID = Region.ID
                                         LEFT JOIN Dillers ON Cars.DillersID = Dillers.ID
                                         WHERE Cars.ModelID = {self.model}"""
            elif self.type != '':
                request = f"""SELECT Cars.ID, Proiz.Proiz, Type.Type, Model.Model, Price, Region.Region, Dillers.Name, DateBuy
                                         FROM Cars 
                                         LEFT JOIN Proiz ON Cars.ProizID = Proiz.ID
                                         LEFT JOIN Type ON Cars.TypeID = Type.ID
                                         LEFT JOIN Model ON Cars.ModelID = Model.ID
                                         LEFT JOIN Region ON Cars.RegionID = Region.ID
                                         LEFT JOIN Dillers ON Cars.DillersID = Dillers.ID
                                         WHERE Cars.TypeID = {self.type}"""
            elif self.region != '':
                request = f"""SELECT Cars.ID, Proiz.Proiz, Type.Type, Model.Model, Price, Region.Region, Dillers.Name, DateBuy
                                         FROM Cars 
                                         LEFT JOIN Proiz ON Cars.ProizID = Proiz.ID
                                         LEFT JOIN Type ON Cars.TypeID = Type.ID
                                         LEFT JOIN Model ON Cars.ModelID = Model.ID
                                         LEFT JOIN Region ON Cars.RegionID = Region.ID
                                         LEFT JOIN Dillers ON Cars.DillersID = Dillers.ID
                                         WHERE Cars.RegionID = {self.region}"""

            cur = self.con.cursor()
            result = cur.execute(request).fetchall()
            self.tableWidget.setColumnCount(len(result[0]))
            #columns = [column[0] for column in cur.description]
            self.tableWidget.setHorizontalHeaderLabels(
                ["ID", "Производитель", "Тип", "Название", "Цена", "Регион", "Диллер",
                 "Дата покупки"])
            # self.tableWidget.setHorizontalHeaderLabels(columns)
            self.tableWidget.setRowCount(len(result))
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                self.count += 1
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.setSortingEnabled(True)
            if self.count != 0:
                self.stroka = ('Нашлось ' + str(self.count) + ' записей!')
                self.statusBar().showMessage(self.stroka)
        except Exception:
            self.tableWidget.clear()
            self.stroka2 = ('Не найдено не одной записи!')
            self.statusBar().showMessage(self.stroka2)
        self.con.close()
        self.comboBoxProizvod.setEnabled(False)
        self.comboBoxModel.setEnabled(False)
        self.comboBoxType.setEnabled(False)
        self.comboBoxRegion.setEnabled(False)

    # вызов дочернего окна добавления данных нового автоиобиля
    def modelAdd(self):
        self.modelAdd = modelAdd.AddModel(self)
        self.modelAdd.show()

    # вызов дочернего окна редактирования данных выбранного автоиобиля с передачей данных о нём
    def modelChange(self):
        self.con = sqlite3.connect("Market.sqlite")
        cur = self.con.cursor()
        request = """SELECT Cars.ID, Proiz.Proiz, Type.Type, Model.Model, Price, Region.Region, 
                              Dillers.Name, Year, DateBuy
                              FROM Cars 
                              LEFT JOIN Proiz ON Cars.ProizID = Proiz.ID
                              LEFT JOIN Type ON Cars.TypeID = Type.ID
                              LEFT JOIN Model ON Cars.ModelID = Model.ID
                              LEFT JOIN Region ON Cars.RegionID = Region.ID
                              LEFT JOIN Dillers ON Cars.DillersID = Dillers.ID
                              """
        result = cur.execute(request).fetchone()
        self.cols = len(result)
        self.cell.clear()
        for col in range(self.cols):
            self.cell.append(self.tableWidget.item(self.row, col).text())
        cell = self.cell
        self.changeModel = modelChange.ChangeModel(self, cell)
        self.changeModel.show()

    # вызов дочернего окна удаления данных выбранного автоиобиля с передачей данных о нём
    def modelDel(self):
        self.con = sqlite3.connect("Market.sqlite")
        cur = self.con.cursor()
        request = """SELECT Cars.ID, Proiz.Proiz, Type.Type, Model.Model, Price, Region.Region, 
                              Dillers.Name, Year, DateBuy
                              FROM Cars 
                              LEFT JOIN Proiz ON Cars.ProizID = Proiz.ID
                              LEFT JOIN Type ON Cars.TypeID = Type.ID
                              LEFT JOIN Model ON Cars.ModelID = Model.ID
                              LEFT JOIN Region ON Cars.RegionID = Region.ID
                              LEFT JOIN Dillers ON Cars.DillersID = Dillers.ID
                              """
        result = cur.execute(request).fetchone()
        self.cols = len(result)
        self.cell.clear()
        for col in range(self.cols):
            self.cell.append(self.tableWidget.item(self.row, col).text())
        cell = self.cell
        self.deleteModel = modelDel.DelModel(self, cell)
        self.deleteModel.show()

    #вывод gif рисунка на второй закладке
    def tab2(self):
        self.pathgif = '.\Picture\gif.gif'
        self.gif = QtGui.QMovie(self.pathgif)
        self.labelGif.setScaledContents(True)
        self.labelGif.setMovie(self.gif)
        self.gif.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #инициализация первоначальной заставки
    zastavka_jpg = QPixmap('.\Picture\zastavka.jpg')
    splash = QSplashScreen(zastavka_jpg, Qt.WindowStaysOnTopHint)
    # инициализация шкалы загрузки
    progressBar = QProgressBar(splash)
    progressBar.setGeometry(QtCore.QRect(610, 600, 118, 23))
    #проценты отображаются посередине прогресс бара
    progressBar.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)

    splash.setMask(zastavka_jpg.mask())
    splash.showMessage('Загрузка приложения...', Qt.AlignHCenter | Qt.AlignBottom, Qt.green)
    #вывод заставки
    splash.show()
    #цикл времени и измения процентов шкалы загрузки
    for i in range(0, 101):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.03:
            app.processEvents()
    app.processEvents()
    #вывод основго окна и закрытие заставки
    ex = Window()
    splash.finish(ex)
    ex.show()

    sys.exit(app.exec())
