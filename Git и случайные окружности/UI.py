# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(867, 645)
        self.btn_draw = QtWidgets.QPushButton(Form)
        self.btn_draw.setGeometry(QtCore.QRect(230, 280, 331, 51))
        self.btn_draw.setObjectName("btn_draw")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_draw.setText(_translate("Form", "Нажми, чтобы появился кружочек"))
