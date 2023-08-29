from PyQt5 import QtCore, QtWidgets
import os
import sys
import numpy as np
import keras
from keras.models import load_model
class Ui_Detection(object):
    def browse_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Photo")
        print(fileName)
        self.lineEdit.setText(fileName)

    def detection_img(self):
        CATEGORIES = ['Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']
        try:
            testimage = self.lineEdit.text()
            if testimage == "" or testimage == "null":
                self.showMessageBox("Information", "Please Select Image")
            else:
                model_path = os.path.join("/Users/sabehah/Desktop/ldd project/cnn_model.h5")
                model = load_model(model_path)
                test_image = keras.utils.load_img(testimage, color_mode='rgb',target_size=(224, 224))
                test_image = keras.utils.img_to_array(test_image)
                test_image=np.reshape(test_image,(1,224,224,3))
                test_image = test_image/255.0
                prediction = model.predict(test_image)
                res=CATEGORIES[np.argmax(prediction)]
                self.label_3.setText("Result : " + res)
        except Exception as e: 
            print("Exception:-",e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(758, 409)
        Dialog.setStyleSheet("background-color: rgb(113, 75, 56);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 50, 401, 71))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n""font: 12pt \"Georgia\";")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 170, 291, 31))
        self.lineEdit.setStyleSheet("font: 75 10pt \"Verdana\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(420, 170, 91, 31))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n" "font: 10pt \"Georgia\";\n" "background-color: rgb(57, 115, 172);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browse_file)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 230, 121, 31))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n" "font: 14pt \"Georgia\";\n" "background-color: rgb(57, 115, 172);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.detection_img)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 300, 511, 51))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n" "font: 16pt \"Georgia\";")
        self.label_3.setObjectName("label_3")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tomato Leaf Disease Detection"))
        self.label.setText(_translate("Dialog", "Tomato Leaf Disease Detection"))
        self.label_2.setText(_translate("Dialog", "Select Image"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.pushButton_3.setText(_translate("Dialog", "Detection"))
        self.label_3.setText(_translate("Dialog", "Result :"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    Dialog.ui= Ui_Detection()
    Dialog.exec_()
    Dialog.show()
    sys.exit(app.exec_())
