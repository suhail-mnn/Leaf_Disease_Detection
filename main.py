from PyQt5 import QtCore, QtWidgets
from Detection import Ui_Detection
from Training_CNN import build_model
class Ui_Main(object):
    def train_model(self):
        build_model()
        self.showMessageBox("Information", "CNN model is created successfully..!")

    def detection_bus(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Detection()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(673, 529)
        Dialog.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 180, 301, 41))
        self.pushButton.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n" "color: rgb(255, 255, 255);\n" "background-color: rgb(148, 98, 73);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.train_model)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 300, 301, 41))
        self.pushButton_2.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n" "color: rgb(255, 255, 255);\n" "background-color: rgb(148, 98, 73);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.detection_bus)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 30, 521, 81))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n" "font: 18pt \"Franklin Gothic Heavy\";")
        self.label.setObjectName("label")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Main"))
        self.pushButton.setText(_translate("Dialog", "Train CNN Model"))
        self.pushButton_2.setText(_translate("Dialog", " Disease Detection"))
        self.label.setText(_translate("Dialog", "Tomato Leaf Disease Detection"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Main()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())