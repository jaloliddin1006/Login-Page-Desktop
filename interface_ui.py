import sys, images
# import sys, os
from PySide2 import *
from qt_material import *

from PyQt5 import QtCore, QtGui, QtWidgets

from main import *
from main_user import *

from ui_Admin_1 import *

from ui_User_Ui_2 import *




from Custom_Widgets.Widgets import *



class Ui_Form(object):
    def admin_window(self):
        self.newwin = QtWidgets.QWidget()
        self.ui = MainWindow_admin()
        self.ui.show()
        Form.hide()

    def user_window(self):
        self.newwin = QtWidgets.QWidget()
        self.ui = MainWindow_user()
        self.ui.show()
        Form.hide()



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(401, 573)

        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 40, 370, 480))
        self.widget.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.5050545, x2:1, y2:0.426, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.5050545, x2:1, y2:0.426, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color: rgba(105,118,132,200);\n"
"}\n"
"\n"
"QPushButton#pushButton_2,#pushButton_3,#pushButton_4,#pushButton_5,#pushButton_6{\n"
"    background-color:rgba(0,0,0,0);\n"
"    color: rgba(105, 118, 132, 200);\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover,#pushButton_3:hover,#pushButton_4:hover,#pushButton_5:hove,#pushButton_6:hoverr{\n"
"    color: rgba(155, 168, 182, 200);\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed,#pushButton_3:pressed,#pushButton_4:pressed,#pushButton_5:pressed,#pushButton_6:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color: rgba(105,128,142,0);\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 30, 300, 420))
        self.label.setStyleSheet("background-image: url(:/image/fon.jpg);\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 300, 420))
        self.label_2.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.511299, cy:0.363, radius:0.466, fx:0.511318, fy:0.369, stop:0.272727 rgba(0, 0, 0, 0), stop:0.460227 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 167));\n"
"border-radius:20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 280, 390))
        self.label_3.setStyleSheet("background-color:rgba(0,0,0,100);\n"
"border-radius:15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(135, 95, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.label_4.setObjectName("label_4")
        self.user_name = QtWidgets.QLineEdit(self.widget)
        self.user_name.setGeometry(QtCore.QRect(80, 165, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_name.setFont(font)
        self.user_name.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,238,252,255);\n"
"color: rgba(155, 225, 255, 235);\n"
"padding-bottom:7px;")
        self.user_name.setObjectName("user_name")
        self.get_password = QtWidgets.QLineEdit(self.widget)
        self.get_password.setGeometry(QtCore.QRect(80, 230, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.get_password.setFont(font)
        self.get_password.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,238,252,255);\n"
"color: rgba(155, 225, 255, 235);\n"
"padding-bottom:7px;")
        self.get_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.get_password.setObjectName("get_password")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.clicked.connect(lambda: self.password_test())

        self.pushButton.setGeometry(QtCore.QRect(80, 310, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(92, 361, 181, 16))
        self.label_5.setStyleSheet("color: rgba(255, 255, 255, 140);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 390, 160, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)


        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.clicked.connect(lambda: self.click())
        self.pushButton_6.setGeometry(QtCore.QRect(280, 30, 30, 30))
        self.pushButton_6.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(60, 35, 51, 21))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/image/ICT_academy_02.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")


        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))




       

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.user_name.setPlaceholderText(_translate("Form", " User Name"))
        self.get_password.setPlaceholderText(_translate("Form", " Password"))
        self.pushButton.setText(_translate("Form", "L o g  I n"))
        self.label_5.setText(_translate("Form", "Forgot your User Name or Password?"))
        self.pushButton_2.setText(_translate("Form", "E"))
        self.pushButton_3.setText(_translate("Form", "D"))
        self.pushButton_4.setText(_translate("Form", "M"))
        self.pushButton_5.setText(_translate("Form", "("))
        self.pushButton_6.setText(_translate("Form", "X"))


    def click(self):
        exit()
    def password_test(self):
        if self.user_name.text() == "admin" and self.get_password.text() == 'pass':
            print("admin")
            self.admin_window()
        elif self.user_name.text() == "user" and self.get_password.text() == 'root':
            print("user")
            self.user_window()
        else:
            print("xatolik")
        # pass
        # Form.showMinimized()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
