# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patient.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 150)
        MainWindow.setMinimumSize(QtCore.QSize(500, 150))
        MainWindow.setMaximumSize(QtCore.QSize(500, 150))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sendbtn = QtWidgets.QPushButton(self.centralwidget)
        self.sendbtn.setGeometry(QtCore.QRect(310, 30, 161, 71))
        self.sendbtn.setObjectName("sendbtn")
        self.statuslbl = QtWidgets.QLabel(self.centralwidget)
        self.statuslbl.setGeometry(QtCore.QRect(60, 30, 111, 21))
        self.statuslbl.setObjectName("statuslbl")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 61, 21))
        self.label.setObjectName("label")
        self.connectbtn = QtWidgets.QPushButton(self.centralwidget)
        self.connectbtn.setGeometry(QtCore.QRect(20, 60, 121, 41))
        self.connectbtn.setObjectName("connectbtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Patient"))
        self.sendbtn.setText(_translate("MainWindow", "send"))
        self.statuslbl.setText(_translate("MainWindow", "Disconnected"))
        self.label.setText(_translate("MainWindow", "Status : "))
        self.connectbtn.setText(_translate("MainWindow", "connect"))

