# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ocr.ui'
#
# Created by: PyQt5 UI code generator 5.11.3

# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from aip import AipOcr

def get_file(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def message(Title,Text):
    message = QMessageBox()
    message.addButton(QPushButton('确定'), QMessageBox.YesRole)
    message.setWindowTitle(Title)
    message.setText(Text)
    message.exec_()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.mod = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024,720)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("result")
        self.gridLayout.addWidget(self.textEdit,0,0,50,1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.gridLayout.addWidget(self.textEdit_2,0,1,1,3)
        self.textEdit_2.setObjectName("filepath")
        self.textEdit_2.isReadOnly()
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.gridLayout.addWidget(self.textEdit_3,3,1,1,3)
        self.textEdit_3.setObjectName("url")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton,2,2,1,1)
        self.pushButton.setObjectName("choose_filepath")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_2,49,3,1,1)
        self.pushButton_2.setObjectName("start_OCR")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_3,4,2,1,1)
        self.pushButton_3.setObjectName("set_url")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.pushButton_4,49,1,1,1)
        self.pushButton_4.setObjectName("set_url")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.gridLayout.addWidget(self.textEdit_4,5,1,1,2)
        self.textEdit_4.setObjectName("app_id")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label,5,3,1,1)
        self.label.setObjectName("set_app_id")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.gridLayout.addWidget(self.textEdit_5,6,1,1,2)
        self.textEdit_5.setObjectName("app_id")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_2,6,3,1,1)
        self.label_2.setObjectName("set_api_key")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.gridLayout.addWidget(self.textEdit_6,7,1,1,2)
        self.textEdit_6.setObjectName("secret_key")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_3,7,3,1,1)
        self.label_3.setObjectName("set_secret")
        self.radiobutton = QtWidgets.QRadioButton(self.centralwidget)
        self.gridLayout.addWidget(self.radiobutton,8,1,1,1)
        self.radiobutton.setChecked(True)
        self.radiobutton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.gridLayout.addWidget(self.radiobutton_2,8,2,1,1)
        self.radiobutton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.gridLayout.addWidget(self.radiobutton_3,9,1,1,1)
        self.radiobutton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.gridLayout.addWidget(self.radiobutton_4,9,2,1,1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.setFont(QtGui.QFont("华文新魏", 15))
        self.pushButton_2.setFont(QtGui.QFont("华文新魏", 15))
        self.pushButton_3.setFont(QtGui.QFont("华文新魏", 15))
        self.pushButton_4.setFont(QtGui.QFont("华文新魏", 15))
        self.textEdit.setFont(QtGui.QFont("", 10))
        self.textEdit.setText("识别前请填入app_id、api_key和secret_key\r\n"
                              "填入完成后选择本地文件或者输入网址\r\n"
                              "文字识别完成后会显示在这里\r\n"
                              "图片识别完成后是一个链接，打开下载到本地用Excel打开即可\r\n")
        self.textEdit_2.setFont(QtGui.QFont("华文新魏", 10))
        self.textEdit_2.setText("等待选择文件")
        self.textEdit_3.setFont(QtGui.QFont("华文新魏", 10))
        self.textEdit_3.setText("等待输入网址")
        self.textEdit_4.setFont(QtGui.QFont("华文新魏", 10))
        self.textEdit_4.setText("")#app_id
        self.textEdit_5.setFont(QtGui.QFont("华文新魏", 10))
        self.textEdit_5.setText("")#api_key
        self.textEdit_6.setFont(QtGui.QFont("华文新魏", 10))
        self.textEdit_6.setText("")#api_secert
        self.label.setText("APP_ID")
        self.label.setFont(QtGui.QFont("华文新魏",15))#设置字体样式
        self.label.setAlignment(QtCore.Qt.AlignCenter)#居中
        self.label_2.setText("API_KEY")
        self.label_2.setFont(QtGui.QFont("华文新魏", 15))  # 设置字体样式
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # 居中
        self.label_3.setText("SECRET")
        self.label_3.setFont(QtGui.QFont("华文新魏", 15))  # 设置字体样式
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)  # 居中
        self.radiobutton.setText("文字识别")
        self.radiobutton.setFont(QtGui.QFont("华文新魏", 13))
        self.radiobutton_2.setText("文字识别（高精度）")
        self.radiobutton_2.setFont(QtGui.QFont("华文新魏", 13))
        self.radiobutton_3.setText("表格识别")
        self.radiobutton_3.setFont(QtGui.QFont("华文新魏", 13))
        self.radiobutton_4.setText("表格识别（高精度）")
        self.radiobutton_4.setFont(QtGui.QFont("华文新魏", 13))

        self.pushButton.clicked.connect(self.choosefile)
        self.pushButton_2.clicked.connect(self.start)
        self.pushButton_3.clicked.connect(self.seturl)
        self.pushButton_4.clicked.connect(self.clear)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple OCR"))
        self.pushButton.setText(_translate("MainWindow", "选择文件"))
        self.pushButton_2.setText(_translate("MainWindow", "开始识别"))
        self.pushButton_3.setText(_translate("MainWindow","输入网址"))
        self.pushButton_4.setText(_translate("MainWindow", "清空"))

    def choosefile(self):
        self.filename,self.filetype = QFileDialog.getOpenFileName(directory="C:\\Users\\Administrator\\Desktop",filter="JPG Files (*.jpg);;PNG Files (*.png);;BMP Files (*.bmp)")
        self.textEdit_2.setText(self.filename)
        self.filepath = self.textEdit_2.toPlainText()
        self.filepath.replace("/","\\")
        self.mod = 1
        self.textEdit_3.setText("等待输入网址")

    def start(self):
        messageBox = QMessageBox()
        if self.textEdit_4.toPlainText() == "等待输入APP_ID" or self.textEdit_5.toPlainText() == "等待输入API_KEY"  or self.textEdit_6.toPlainText() ==  "等待输入SECRET_KEY":
            message('警告','请输入正确的信息')
        else:
            self.app_id = self.textEdit_4.toPlainText()
            self.api_key = self.textEdit_5.toPlainText()
            self.secert = self.textEdit_6.toPlainText()
            self.client = AipOcr(self.app_id,self.api_key,self.secert)
            if self.radiobutton.isChecked():
                #文字识别
                if self.mod == 1:
                    self.img = get_file(self.filepath)
                    self.result = self.client.basicGeneral(self.img)
                    self.words = self.result["words_result"]
                    self.textEdit.setText("")
                    self.content = ""
                    for self.word in self.words:
                        self.content = self.content + self.word["words"] + "\r\n"
                    self.textEdit.insertPlainText(self.content)
                elif self.mod == 2:
                    self.result = self.client.basicGeneralUrl(self.url)
                    self.words = self.result["words_result"]
                    self.textEdit.setText("")
                    self.content = ""
                    for self.word in self.words:
                        self.content = self.content + self.word["words"] + "\r\n"
                    self.textEdit.insertPlainText(self.content)
                else:
                    message('警告','请选择文件或输入网址')
            elif self.radiobutton_2.isChecked():
                #文字识别（高精度）
                if self.mod == 1:
                    self.img = get_file(self.filepath)
                    self.result = self.client.basicAccurate(self.img)
                    self.words = self.result["words_result"]
                    self.textEdit.setText("")
                    self.content = ""
                    for self.word in self.words:
                        self.content = self.content + self.word["words"] + "\r\n"
                    self.textEdit.insertPlainText(self.content)
                elif self.mod == 2:
                    message('警告','该模式不支持网络图片\r\n请选择本地图片')
                else:
                    message('警告','请选择文件或输入网址')
            elif self.radiobutton_3.isChecked():
                if self.mod == 1:
                    self.img = get_file(self.filepath)
                    self.result = self.client.tableRecognition(self.img)["result"]
                    self.result_data = self.result["result_data"]
                    self.textEdit.setText("网址为： "+ self.result_data + "\r\n请下载")
                elif self.mod == 2:
                    message('警告','该模式不支持网络图片\r\n请选择本地图片')
                else:
                    message('警告','请选择文件或输入网址')
                #表格识别
            elif self.radiobutton_4.isChecked():
                message('警告','该模式不可用')

    def seturl(self):
        if self.textEdit_3.toPlainText() == "等待输入网址":
            message('警告','请输入网址')
        else:
            self.url = self.textEdit_3.toPlainText()
            self.mod = 2
            self.textEdit_2.setText("等待选择文件")

    def clear(self):
        self.textEdit.setText("识别前请填入app_id、api_key和secret_key\r\n"
                              "填入完成后选择本地文件或者输入网址\r\n"
                              "文字识别完成后会显示在这里\r\n"
                              "图片识别完成后是一个链接，打开下载到本地用Excel打开即可\r\n")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
