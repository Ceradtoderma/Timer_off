#!/usr/bin/python3
# -*- coding: utf-8 -*-

from usin import *
import sys
import os


class Timer(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('Таймер для Зефирки')
        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.ui.btn_h_min.clicked.connect(lambda: self.btn_down(self.ui.le_hour))
        self.ui.btn_h_plus.clicked.connect(lambda: self.btn_up(self.ui.le_hour))
        self.ui.btn_m_min.clicked.connect(lambda: self.btn_down(self.ui.le_min))
        self.ui.btn_m_plus.clicked.connect(lambda: self.btn_up(self.ui.le_min))
        self.ui.btn_run.clicked.connect(self.run)
        self.ui.btn_off.clicked.connect(self.off)

        self.show()

    def check_data(self, cnt):
        """
        Проверяет не введены ли буквы
        """
        try:
            cnt = int(cnt)
            if cnt > 58:
                cnt = 0
        except ValueError:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Только цифры')
            cnt = 0
        return cnt

    def btn_up(self, widget):
        num = self.check_data(widget.text())
        widget.setText(str(num + 1))

    def btn_down(self, widget):
        num = self.check_data(widget.text())
        if num == 0:
            widget.setText('0')
        else:
            widget.setText(str(num - 1))

    def run(self):

        h = self.check_data(self.ui.le_hour.text())
        m = self.check_data(self.ui.le_min.text())
        sec = (h * 3600) + (m * 60)

        msgbox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, "Подтвердите выключение",
                                       f"Ваш компьютер будет выключен через {h} часов {m} минут")
        msgbox.addButton(QtWidgets.QMessageBox.Yes)
        msgbox.addButton(QtWidgets.QMessageBox.No)
        msgbox.setDefaultButton(QtWidgets.QMessageBox.No)
        icon = QtGui.QPixmap('Attention.ico')
        msgbox.setIconPixmap(icon)

        reply = msgbox.exec_()
        if reply == QtWidgets.QMessageBox.Yes:
            os.system(f'shutdown -s -t {sec}')
            # self.close()


    def cancel(self):

        msgbox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, "Подтвердите отмену",
                                       "Вы уверены, что хотите отклбчить таймер?")
        msgbox.addButton(QtWidgets.QMessageBox.Yes)
        msgbox.addButton(QtWidgets.QMessageBox.No)
        msgbox.setDefaultButton(QtWidgets.QMessageBox.No)
        icon = QtGui.QPixmap('Attention.ico')
        msgbox.setIconPixmap(icon)

        reply = msgbox.exec_()
        if reply == QtWidgets.QMessageBox.Yes:
            os.system('shutdown -a')


app = QtWidgets.QApplication(sys.argv)
ex = Timer()
sys.exit(app.exec_())
