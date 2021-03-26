#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 310)
        Form.setMaximumSize(QtCore.QSize(300, 310))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        Form.setFont(font)


        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 310, 310))
        self.frame.setStyleSheet("background-color: rgb(33, 235, 218);")

        self.le_hour = QtWidgets.QLineEdit(Form)
        self.le_hour.setGeometry(QtCore.QRect(40, 80, 81, 41))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(20)
        self.le_hour.setFont(font)
        self.le_hour.setStyleSheet("background-color: rgb(105, 238, 227);\n"
                                   "border: 2px solid;\n"
                                   "border-color: rgb(47, 107, 102);\n"
                                   "border-radius: 8")
        self.le_hour.setAlignment(QtCore.Qt.AlignCenter)
        self.le_hour.setObjectName("le_hour")
        self.le_min = QtWidgets.QLineEdit(Form)
        self.le_min.setGeometry(QtCore.QRect(170, 80, 81, 41))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(20)
        self.le_min.setFont(font)
        self.le_min.setStyleSheet("background-color: rgb(105, 238, 227);\n"
                                  "border: 2px solid;\n"
                                  "border-color: rgb(47, 107, 102);\n"
                                  "border-radius: 8")
        self.le_min.setAlignment(QtCore.Qt.AlignCenter)
        self.le_min.setObjectName("le_min")
        self.lbl_hour = QtWidgets.QLabel(Form)
        self.lbl_hour.setGeometry(QtCore.QRect(40, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.lbl_hour.setFont(font)
        self.lbl_hour.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_hour.setObjectName("lbl_hour")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.btn_h_min = QtWidgets.QPushButton(Form)
        self.btn_h_min.setGeometry(QtCore.QRect(40, 130, 31, 31))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_h_min.setFont(font)
        self.btn_h_min.setStyleSheet("QPushButton {\n"
                                     "border: 1px solid;\n"
                                     "border-color: rgb(47, 107, 102);\n"
                                     "border-radius: 15;    \n"
                                     "background-color: rgb(26, 184, 170);\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "    background-color: rgb(9, 135, 129);\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "    background-color: rgb(6, 89, 85);\n"
                                     "}")
        self.btn_h_min.setObjectName("btn_h_min")
        self.btn_h_plus = QtWidgets.QPushButton(Form)
        self.btn_h_plus.setGeometry(QtCore.QRect(90, 130, 31, 31))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_h_plus.setFont(font)
        self.btn_h_plus.setStyleSheet("QPushButton {\n"
                                      "border: 1px solid;\n"
                                      "border-color: rgb(47, 107, 102);\n"
                                      "border-radius: 15;    \n"
                                      "background-color: rgb(26, 184, 170);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    background-color: rgb(9, 135, 129);\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    background-color: rgb(6, 89, 85);\n"
                                      "}")
        self.btn_h_plus.setObjectName("btn_h_plus")
        self.btn_m_plus = QtWidgets.QPushButton(Form)
        self.btn_m_plus.setGeometry(QtCore.QRect(220, 130, 31, 31))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(20)
        self.btn_m_plus.setFont(font)
        self.btn_m_plus.setStyleSheet("QPushButton {\n"
                                      "border: 1px solid;\n"
                                      "border-color: rgb(47, 107, 102);\n"
                                      "border-radius: 15;    \n"
                                      "background-color: rgb(26, 184, 170);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    background-color: rgb(9, 135, 129);\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    background-color: rgb(6, 89, 85);\n"
                                      "}")
        self.btn_m_plus.setObjectName("btn_m_plus")
        self.btn_m_min = QtWidgets.QPushButton(Form)
        self.btn_m_min.setGeometry(QtCore.QRect(170, 130, 31, 31))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(20)
        self.btn_m_min.setFont(font)
        self.btn_m_min.setStyleSheet("QPushButton {\n"
                                     "border: 1px solid;\n"
                                     "border-color: rgb(47, 107, 102);\n"
                                     "border-radius: 15;    \n"
                                     "background-color: rgb(26, 184, 170);\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "    background-color: rgb(9, 135, 129);\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "    background-color: rgb(6, 89, 85);\n"
                                     "}")
        self.btn_m_min.setObjectName("btn_m_min")
        self.lbl_delimetr = QtWidgets.QLabel(Form)
        self.lbl_delimetr.setGeometry(QtCore.QRect(140, 80, 8, 42))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        self.lbl_delimetr.setFont(font)
        self.lbl_delimetr.setObjectName("lbl_delimetr")
        self.btn_run = QtWidgets.QPushButton(Form)
        self.btn_run.setGeometry(QtCore.QRect(40, 170, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.btn_run.setFont(font)
        self.btn_run.setStyleSheet("QPushButton {\n"
                                   "border: 1px solid;\n"
                                   "border-color: rgb(47, 107, 102);\n"
                                   "background-color: rgb(26, 184, 170);\n"
                                   "border-radius: 8;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color: rgb(9, 135, 129);\n"
                                   "}\n"
                                   "QPushButton:pressed{\n"
                                   "background-color: rgb(6, 89, 85);\n"
                                   "}")
        self.btn_run.setObjectName("btn_run")

        self.btn_off = QtWidgets.QPushButton(Form)
        self.btn_off.setGeometry(QtCore.QRect(40, 230, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.btn_off.setFont(font)
        self.btn_off.setStyleSheet("QPushButton {\n"
                                   "border: 1px solid;\n"
                                   "border-color: rgb(47, 107, 102);\n"
                                   "background-color: rgb(26, 184, 170);\n"
                                   "border-radius: 8;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color: rgb(9, 135, 129);\n"
                                   "}\n"
                                   "QPushButton:pressed{\n"
                                   "background-color: rgb(6, 89, 85);\n"
                                   "}")
        self.btn_off.setObjectName("btn_off")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.le_hour.setText(_translate("Form", "0"))
        self.le_min.setText(_translate("Form", "0"))
        self.lbl_hour.setText(_translate("Form", "Часы"))
        self.label_2.setText(_translate("Form", "Минуты"))
        self.btn_h_min.setText(_translate("Form", "-"))
        self.btn_h_plus.setText(_translate("Form", "+"))
        self.btn_m_plus.setText(_translate("Form", "+"))
        self.btn_m_min.setText(_translate("Form", "-"))
        self.lbl_delimetr.setText(_translate("Form", ":"))
        self.btn_run.setText(_translate("Form", "Запустить"))
        self.btn_off.setText(_translate("Form", "Отменить"))
