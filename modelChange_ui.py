# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modelChange_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form2(object):
    def setupUi(self, Form2):
        Form2.setObjectName("Form2")
        Form2.resize(620, 666)
        self.pushButtonChange = QtWidgets.QPushButton(Form2)
        self.pushButtonChange.setGeometry(QtCore.QRect(160, 610, 261, 23))
        self.pushButtonChange.setObjectName("pushButtonChange")
        self.label_6 = QtWidgets.QLabel(Form2)
        self.label_6.setGeometry(QtCore.QRect(220, 20, 161, 21))
        self.label_6.setObjectName("label_6")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form2)
        self.calendarWidget.setGeometry(QtCore.QRect(290, 60, 312, 271))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_12 = QtWidgets.QLabel(Form2)
        self.label_12.setGeometry(QtCore.QRect(10, 380, 281, 211))
        self.label_12.setObjectName("label_12")
        self.formLayoutWidget = QtWidgets.QWidget(Form2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 60, 271, 281))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.labelID = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelID.setText("")
        self.labelID.setObjectName("labelID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelID)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBoxProiz2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBoxProiz2.setObjectName("comboBoxProiz2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxProiz2)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.comboBoxModel2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBoxModel2.setObjectName("comboBoxModel2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBoxModel2)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBoxType2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBoxType2.setObjectName("comboBoxType2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBoxType2)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboBoxRegion2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBoxRegion2.setObjectName("comboBoxRegion2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBoxRegion2)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.comboBoxDiller2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBoxDiller2.setObjectName("comboBoxDiller2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBoxDiller2)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEditYear = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEditYear.setObjectName("lineEditYear")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEditYear)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEditCena = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEditCena.setObjectName("lineEditCena")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEditCena)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.labelbuydate = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelbuydate.setObjectName("labelbuydate")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.labelbuydate)
        self.pushButtonJPG = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButtonJPG.setObjectName("pushButtonJPG")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.pushButtonJPG)
        self.labelJPG = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelJPG.setObjectName("labelJPG")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.labelJPG)
        self.pushButtonTXT = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButtonTXT.setObjectName("pushButtonTXT")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.pushButtonTXT)
        self.labeltext = QtWidgets.QLabel(self.formLayoutWidget)
        self.labeltext.setObjectName("labeltext")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.labeltext)
        self.label_13 = QtWidgets.QLabel(Form2)
        self.label_13.setGeometry(QtCore.QRect(10, 640, 601, 16))
        self.label_13.setObjectName("label_13")
        self.textBrowser = QtWidgets.QTextBrowser(Form2)
        self.textBrowser.setGeometry(QtCore.QRect(290, 380, 311, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.labelnowdate = QtWidgets.QLabel(Form2)
        self.labelnowdate.setGeometry(QtCore.QRect(530, 10, 81, 20))
        self.labelnowdate.setObjectName("labelnowdate")
        self.label_10 = QtWidgets.QLabel(Form2)
        self.label_10.setGeometry(QtCore.QRect(0, 350, 291, 28))
        self.label_10.setObjectName("label_10")
        self.label_14 = QtWidgets.QLabel(Form2)
        self.label_14.setGeometry(QtCore.QRect(310, 350, 291, 28))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form2)
        self.label_15.setGeometry(QtCore.QRect(440, 10, 91, 16))
        self.label_15.setObjectName("label_15")

        self.retranslateUi(Form2)
        QtCore.QMetaObject.connectSlotsByName(Form2)

    def retranslateUi(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form2", "Добавить автомобиль в БД"))
        self.pushButtonChange.setText(_translate("Form2", "Отредактировать автомобиль в БД"))
        self.label_6.setText(_translate("Form2", "Редактирование автомобиля"))
        self.label_12.setText(_translate("Form2", "Картинка автомобиля"))
        self.label_9.setText(_translate("Form2", "ID"))
        self.label_4.setText(_translate("Form2", "Производитель"))
        self.label_5.setText(_translate("Form2", "Модель"))
        self.label.setText(_translate("Form2", "Тип"))
        self.label_8.setText(_translate("Form2", "Регион"))
        self.label_11.setText(_translate("Form2", "Диллер"))
        self.label_2.setText(_translate("Form2", "Год выпуска"))
        self.lineEditYear.setText(_translate("Form2", "2010"))
        self.label_3.setText(_translate("Form2", "Цена"))
        self.lineEditCena.setText(_translate("Form2", "700000"))
        self.label_7.setText(_translate("Form2", "Дата покупки"))
        self.labelbuydate.setText(_translate("Form2", "11-11-2020"))
        self.pushButtonJPG.setText(_translate("Form2", "Выбор картинки"))
        self.labelJPG.setText(_translate("Form2", "1.jpg"))
        self.pushButtonTXT.setText(_translate("Form2", "Выбор текста"))
        self.labeltext.setText(_translate("Form2", "2.jpg"))
        self.label_13.setText(_translate("Form2", "Системные сообщения"))
        self.labelnowdate.setText(_translate("Form2", "TextLabel"))
        self.label_10.setText(_translate("Form2", "                      ИЗОБРАЖЕНИЕ АВТОМОБИЛЯ"))
        self.label_14.setText(_translate("Form2", "                                 ТХ АВТОМОБИЛЯ"))
        self.label_15.setText(_translate("Form2", "Текущая дата:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form2 = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setupUi(Form2)
    Form2.show()
    sys.exit(app.exec_())
