# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'User_Ui_2ANwNIP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(787, 459)
        icon = QIcon()
        icon.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color: transparent;\n"
"color:#fff;\n"
"}\n"
"#centralwidget{\n"
"background-color:#040f13;\n"
"border-color:5px;\n"
"}\n"
"\n"
"#close_window_btn:hover, #minimize_window_btn:hover, #resize_window_btn:hover,#info_btn:hover,#menu_open_close_btn:hover{\n"
"padding-right:3px;\n"
"padding-top:2px;\n"
"} \n"
"\n"
"#close_window_btn:pressed, #minimize_window_btn:pressed, #resize_window_btn:pressed,#info_btn:pressed, #menu_open_close_btn:pressed{\n"
"padding-left:3px;\n"
"padding-bottom:2px;\n"
"} \n"
"\n"
"QPushButton#pushButton_2,#pushButton_3,#pushButton_4,#pushButton_5,#pushButton_6,#pushButton_7,#pushButton_8,#pushButton_9,#pushButton_10,#pushButton_11{\n"
"	background-color:rgba(0,0,0,0);\n"
"	color: rgba(105, 118, 132, 200);\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover,#pushButton_3:hover,#pushButton_4:hover,#pushButton_5:hover,#pushButton_6:hover,#pushButton_7:hover,#pushButton_8:hover,#pushButton_9:hover,#pushButton_10:hover,#pushButton_11:hover{\n"
"	color: rgba(155,"
                        " 168, 182, 200);\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed,#pushButton_3:pressed,#pushButton_4:pressed,#pushButton_5:pressed,#pushButton_6:pressed,#pushButton_7:pressed,#pushButton_8:pressed,#pushButton_9:pressed,#pushButton_10:pressed,#pushButton_11:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color: rgba(105,128,142,0);\n"
"}\n"
"")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_open_close_frame = QFrame(self.header_frame)
        self.menu_open_close_frame.setObjectName(u"menu_open_close_frame")
        self.menu_open_close_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_open_close_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu_open_close_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_open_close_btn = QPushButton(self.menu_open_close_frame)
        self.menu_open_close_btn.setObjectName(u"menu_open_close_btn")
        font = QFont()
        font.setFamily(u"MS PMincho")
        font.setPointSize(14)
        self.menu_open_close_btn.setFont(font)
        self.menu_open_close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_open_close_btn.setIcon(icon1)
        self.menu_open_close_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.menu_open_close_btn, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.menu_open_close_frame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.name_frame = QFrame(self.header_frame)
        self.name_frame.setObjectName(u"name_frame")
        font1 = QFont()
        font1.setPointSize(12)
        self.name_frame.setFont(font1)
        self.name_frame.setFrameShape(QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.name_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.label = QLabel(self.name_frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamily(u"MS PMincho")
        font2.setPointSize(19)
        self.label.setFont(font2)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.name_frame, 0, Qt.AlignVCenter)

        self.components_frame = QFrame(self.header_frame)
        self.components_frame.setObjectName(u"components_frame")
        self.components_frame.setFrameShape(QFrame.StyledPanel)
        self.components_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.components_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.minimize_window_btn = QPushButton(self.components_frame)
        self.minimize_window_btn.setObjectName(u"minimize_window_btn")
        self.minimize_window_btn.setMaximumSize(QSize(28, 24))
        font3 = QFont()
        font3.setFamily(u"Music")
        self.minimize_window_btn.setFont(font3)
        self.minimize_window_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_btn.setIcon(icon2)
        self.minimize_window_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.minimize_window_btn)

        self.resize_window_btn = QPushButton(self.components_frame)
        self.resize_window_btn.setObjectName(u"resize_window_btn")
        self.resize_window_btn.setMaximumSize(QSize(24, 20))
        self.resize_window_btn.setFont(font3)
        self.resize_window_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.resize_window_btn.setIcon(icon3)
        self.resize_window_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.resize_window_btn)

        self.close_window_btn = QPushButton(self.components_frame)
        self.close_window_btn.setObjectName(u"close_window_btn")
        self.close_window_btn.setMaximumSize(QSize(28, 24))
        self.close_window_btn.setFont(font3)
        self.close_window_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_btn.setIcon(icon4)
        self.close_window_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.close_window_btn)


        self.horizontalLayout.addWidget(self.components_frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.body_frame = QFrame(self.centralwidget)
        self.body_frame.setObjectName(u"body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body_frame.sizePolicy().hasHeightForWidth())
        self.body_frame.setSizePolicy(sizePolicy)
        self.body_frame.setStyleSheet(u"\n"
"border-radius:20px ;")
        self.body_frame.setFrameShape(QFrame.StyledPanel)
        self.body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.body_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, -1, -1, -1)
        self.main_body_menu_widget = QCustomSlideMenu(self.body_frame)
        self.main_body_menu_widget.setObjectName(u"main_body_menu_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_body_menu_widget.sizePolicy().hasHeightForWidth())
        self.main_body_menu_widget.setSizePolicy(sizePolicy1)
        self.main_body_menu_widget.setMinimumSize(QSize(0, 0))
        self.main_body_menu_widget.setMaximumSize(QSize(0, 16777215))
        font4 = QFont()
        font4.setPointSize(13)
        self.main_body_menu_widget.setFont(font4)
        self.main_body_menu_widget.setStyleSheet(u"QPushButton{\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover{\n"
"padding-right:5px;\n"
"padding-top:3px;\n"
"	color: rgba(105, 211, 188, 155);\n"
"	background-color: rgba(19, 21, 30, 205);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-bottom:3px;\n"
"	color: rgba(255, 181, 238, 255);\n"
"}\n"
"\n"
"")
        self.verticalLayout_8 = QVBoxLayout(self.main_body_menu_widget)
        self.verticalLayout_8.setSpacing(17)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 11, 0, 7)
        self.home_btn = QPushButton(self.main_body_menu_widget)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(0, 25))
        font5 = QFont()
        font5.setFamily(u"Narkisim")
        font5.setPointSize(16)
        self.home_btn.setFont(font5)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn.setIcon(icon5)
        self.home_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_8.addWidget(self.home_btn)

        self.bazadagi_mahsulotlar_btn = QPushButton(self.main_body_menu_widget)
        self.bazadagi_mahsulotlar_btn.setObjectName(u"bazadagi_mahsulotlar_btn")
        self.bazadagi_mahsulotlar_btn.setMinimumSize(QSize(0, 25))
        self.bazadagi_mahsulotlar_btn.setFont(font5)

        self.verticalLayout_8.addWidget(self.bazadagi_mahsulotlar_btn)

        self.yangi_mahsulotlar_qushish_btn = QPushButton(self.main_body_menu_widget)
        self.yangi_mahsulotlar_qushish_btn.setObjectName(u"yangi_mahsulotlar_qushish_btn")
        self.yangi_mahsulotlar_qushish_btn.setMinimumSize(QSize(0, 25))
        self.yangi_mahsulotlar_qushish_btn.setFont(font5)

        self.verticalLayout_8.addWidget(self.yangi_mahsulotlar_qushish_btn)

        self.mahsulotlarni_sotish_btn = QPushButton(self.main_body_menu_widget)
        self.mahsulotlarni_sotish_btn.setObjectName(u"mahsulotlarni_sotish_btn")
        self.mahsulotlarni_sotish_btn.setMinimumSize(QSize(0, 25))
        self.mahsulotlarni_sotish_btn.setFont(font5)

        self.verticalLayout_8.addWidget(self.mahsulotlarni_sotish_btn)

        self.hisob_kitob_btn = QPushButton(self.main_body_menu_widget)
        self.hisob_kitob_btn.setObjectName(u"hisob_kitob_btn")
        self.hisob_kitob_btn.setMinimumSize(QSize(0, 25))
        self.hisob_kitob_btn.setFont(font5)

        self.verticalLayout_8.addWidget(self.hisob_kitob_btn)

        self.yaroqlilik_muddati_btn = QPushButton(self.main_body_menu_widget)
        self.yaroqlilik_muddati_btn.setObjectName(u"yaroqlilik_muddati_btn")
        self.yaroqlilik_muddati_btn.setMinimumSize(QSize(0, 25))
        self.yaroqlilik_muddati_btn.setFont(font5)

        self.verticalLayout_8.addWidget(self.yaroqlilik_muddati_btn)

        self.info_open_close_btn = QPushButton(self.main_body_menu_widget)
        self.info_open_close_btn.setObjectName(u"info_open_close_btn")
        self.info_open_close_btn.setMinimumSize(QSize(0, 25))
        font6 = QFont()
        font6.setPointSize(19)
        self.info_open_close_btn.setFont(font6)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.info_open_close_btn.setIcon(icon6)
        self.info_open_close_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_8.addWidget(self.info_open_close_btn, 0, Qt.AlignBottom)


        self.horizontalLayout_5.addWidget(self.main_body_menu_widget, 0, Qt.AlignLeft|Qt.AlignTop)

        self.main_body_frame = QFrame(self.body_frame)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy2)
        self.main_body_frame.setStyleSheet(u"background-color:#071e26;\n"
"border-radius:15px;")
        self.main_body_frame.setFrameShape(QFrame.StyledPanel)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_body_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.main_body_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        font7 = QFont()
        font7.setPointSize(14)
        self.stackedWidget.setFont(font7)
        self.stackedWidget.setStyleSheet(u"")
        self.mahsulotlarni_sotish_frame = QWidget()
        self.mahsulotlarni_sotish_frame.setObjectName(u"mahsulotlarni_sotish_frame")
        self.verticalLayout_12 = QVBoxLayout(self.mahsulotlarni_sotish_frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_48 = QLabel(self.mahsulotlarni_sotish_frame)
        self.label_48.setObjectName(u"label_48")
        font8 = QFont()
        font8.setPointSize(23)
        self.label_48.setFont(font8)

        self.verticalLayout_12.addWidget(self.label_48, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.mahsulotlarni_sotish_frame)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
        self.frame_7.setLayoutDirection(Qt.LeftToRight)
        self.frame_7.setStyleSheet(u"QLineEdit{\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-left-radius:8px;\n"
"border-top-right-radius:8px;\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(230, 0, 0, 205), stop:1 rgba(13, 189, 0, 244));\n"
"background-color: rgba(224, 255, 232, 30);\n"
"\n"
"}\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_7)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_63 = QLabel(self.frame_7)
        self.label_63.setObjectName(u"label_63")
        font9 = QFont()
        font9.setFamily(u"Palatino Linotype")
        font9.setPointSize(12)
        self.label_63.setFont(font9)
        self.label_63.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_63)

        self.comboBox_2 = QComboBox(self.frame_7)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy2.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy2)
        self.comboBox_2.setMinimumSize(QSize(150, 25))
        self.comboBox_2.setMaximumSize(QSize(150, 16777215))
        font10 = QFont()
        font10.setPointSize(10)
        self.comboBox_2.setFont(font10)
        self.comboBox_2.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_2.setStyleSheet(u"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-left-radius:8px;\n"
"border-top-right-radius:8px;\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(230, 0, 0, 205), stop:1 rgba(13, 189, 0, 244));\n"
"background-color: rgba(224, 255, 232, 30);")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_2.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox_2)

        self.label_61 = QLabel(self.frame_7)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font9)
        self.label_61.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_61)

        self.comboBox_3 = QComboBox(self.frame_7)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy2.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy2)
        self.comboBox_3.setMinimumSize(QSize(150, 25))
        self.comboBox_3.setMaximumSize(QSize(150, 16777215))
        self.comboBox_3.setFont(font10)
        self.comboBox_3.setStyleSheet(u"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-left-radius:8px;\n"
"border-top-right-radius:8px;\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(230, 0, 0, 205), stop:1 rgba(13, 189, 0, 244));\n"
"background-color: rgba(224, 255, 232, 30);")
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_3.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBox_3)

        self.label_62 = QLabel(self.frame_7)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font9)
        self.label_62.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_62)

        self.lineEdit_10 = QLineEdit(self.frame_7)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        sizePolicy2.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy2)
        self.lineEdit_10.setMinimumSize(QSize(150, 0))
        self.lineEdit_10.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_10.setFont(font9)
        self.lineEdit_10.setStyleSheet(u"")
        self.lineEdit_10.setMaxLength(35)
        self.lineEdit_10.setCursorPosition(0)
        self.lineEdit_10.setAlignment(Qt.AlignCenter)
        self.lineEdit_10.setDragEnabled(False)
        self.lineEdit_10.setReadOnly(False)
        self.lineEdit_10.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_10)

        self.label_65 = QLabel(self.frame_7)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font9)
        self.label_65.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_65)

        self.lineEdit_8 = QLineEdit(self.frame_7)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy2.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy2)
        self.lineEdit_8.setMinimumSize(QSize(150, 0))
        self.lineEdit_8.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_8.setFont(font9)
        self.lineEdit_8.setStyleSheet(u"")
        self.lineEdit_8.setMaxLength(35)
        self.lineEdit_8.setCursorPosition(0)
        self.lineEdit_8.setAlignment(Qt.AlignCenter)
        self.lineEdit_8.setDragEnabled(False)
        self.lineEdit_8.setReadOnly(False)
        self.lineEdit_8.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit_8)

        self.label_64 = QLabel(self.frame_7)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font9)
        self.label_64.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_64)

        self.lineEdit_7 = QLineEdit(self.frame_7)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy2.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy2)
        self.lineEdit_7.setMinimumSize(QSize(150, 0))
        self.lineEdit_7.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_7.setFont(font9)
        self.lineEdit_7.setStyleSheet(u"")
        self.lineEdit_7.setMaxLength(35)
        self.lineEdit_7.setCursorPosition(0)
        self.lineEdit_7.setAlignment(Qt.AlignCenter)
        self.lineEdit_7.setDragEnabled(False)
        self.lineEdit_7.setReadOnly(False)
        self.lineEdit_7.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lineEdit_7)


        self.verticalLayout_12.addWidget(self.frame_7, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.mahsulotlarni_sotish_frame)
        self.home_frame = QWidget()
        self.home_frame.setObjectName(u"home_frame")
        self.verticalLayout_9 = QVBoxLayout(self.home_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_11 = QLabel(self.home_frame)
        self.label_11.setObjectName(u"label_11")
        font11 = QFont()
        font11.setPointSize(18)
        self.label_11.setFont(font11)

        self.verticalLayout_9.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.horizontalFrame = QFrame(self.home_frame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.pushButton_3 = QPushButton(self.horizontalFrame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(30, 30))
        font12 = QFont()
        font12.setFamily(u"Social Media Circled")
        font12.setPointSize(16)
        self.pushButton_3.setFont(font12)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.horizontalFrame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(30, 30))
        self.pushButton_4.setFont(font12)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.horizontalFrame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(30, 30))
        self.pushButton_5.setFont(font12)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.horizontalFrame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(30, 30))
        self.pushButton_6.setFont(font12)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.pushButton_6)


        self.verticalLayout_9.addWidget(self.horizontalFrame, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.home_frame)
        self.hisob_kitob_frame = QWidget()
        self.hisob_kitob_frame.setObjectName(u"hisob_kitob_frame")
        self.verticalLayout_18 = QVBoxLayout(self.hisob_kitob_frame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.scrollArea_3 = QScrollArea(self.hisob_kitob_frame)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 704, 455))
        self.verticalLayout_19 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_13 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font8)

        self.verticalLayout_19.addWidget(self.label_13)

        self.label_14 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(300, 0))
        self.label_14.setMaximumSize(QSize(400, 16777215))
        self.label_14.setPixmap(QPixmap(u":/icons/icons/statistic2.png"))
        self.label_14.setScaledContents(True)

        self.verticalLayout_19.addWidget(self.label_14)

        self.label_16 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(300, 0))
        self.label_16.setMaximumSize(QSize(400, 16777215))
        self.label_16.setPixmap(QPixmap(u":/icons/icons/statistic1.png"))
        self.label_16.setScaledContents(True)

        self.verticalLayout_19.addWidget(self.label_16)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_18.addWidget(self.scrollArea_3)

        self.stackedWidget.addWidget(self.hisob_kitob_frame)
        self.bazadagi_mahsulotlar_frame = QWidget()
        self.bazadagi_mahsulotlar_frame.setObjectName(u"bazadagi_mahsulotlar_frame")
        self.verticalLayout_10 = QVBoxLayout(self.bazadagi_mahsulotlar_frame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.bazadagi_mahsulotlar_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"border-radius: 8px;\n"
"	background-color: rgba(49, 100, 92, 145);\n"
"	color: rgba(222, 248, 244, 155);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"padding-right:5px;\n"
"padding-top:2px;\n"
"background-color: rgba(49, 100, 92, 205);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-bottom:2px;\n"
"\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(20, 5, 20, 0)
        self.bazadagi_mahsulotlar_list_btn = QPushButton(self.frame_2)
        self.bazadagi_mahsulotlar_list_btn.setObjectName(u"bazadagi_mahsulotlar_list_btn")
        font13 = QFont()
        font13.setPointSize(12)
        font13.setItalic(True)
        self.bazadagi_mahsulotlar_list_btn.setFont(font13)
        self.bazadagi_mahsulotlar_list_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.bazadagi_mahsulotlar_list_btn)

        self.bazadagi_mahsulotlar_grafik_btn = QPushButton(self.frame_2)
        self.bazadagi_mahsulotlar_grafik_btn.setObjectName(u"bazadagi_mahsulotlar_grafik_btn")
        self.bazadagi_mahsulotlar_grafik_btn.setFont(font13)
        self.bazadagi_mahsulotlar_grafik_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.bazadagi_mahsulotlar_grafik_btn)


        self.verticalLayout_10.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.bazadagi_mahsulotlar_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.frame_3)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.bazadagi_mahsulotlar_list_frame = QWidget()
        self.bazadagi_mahsulotlar_list_frame.setObjectName(u"bazadagi_mahsulotlar_list_frame")
        self.verticalLayout_15 = QVBoxLayout(self.bazadagi_mahsulotlar_list_frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.bazadagi_mahsulotlar_list_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 739, 351))
        self.horizontalLayout_8 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget.rowCount() < 9):
            self.tableWidget.setRowCount(9)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem21)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/check-circle (3).svg", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setIcon(icon7);
        self.tableWidget.setItem(0, 6, __qtablewidgetitem22)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"color: rgb(255, 0, 34);\n"
"background-color: rgba(174, 255, 217, 155);")

        self.horizontalLayout_8.addWidget(self.tableWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_15.addWidget(self.scrollArea)

        self.stackedWidget_2.addWidget(self.bazadagi_mahsulotlar_list_frame)
        self.bazadagi_mahsulotlar_grafik_frame = QWidget()
        self.bazadagi_mahsulotlar_grafik_frame.setObjectName(u"bazadagi_mahsulotlar_grafik_frame")
        self.verticalLayout_14 = QVBoxLayout(self.bazadagi_mahsulotlar_grafik_frame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.bazadagi_mahsulotlar_grafik_frame)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy1.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy1)
        font14 = QFont()
        font14.setPointSize(7)
        self.scrollArea_2.setFont(font14)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 740, 2064))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font8)
        self.label_15.setPixmap(QPixmap(u":/icons/icons/diagramma1.png"))

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_15)

        self.label_30 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font8)
        self.label_30.setPixmap(QPixmap(u":/icons/icons/diagramma2.jpg"))
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_30)

        self.label_35 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font8)
        self.label_35.setPixmap(QPixmap(u":/icons/icons/diagramma6.png"))

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.label_35)

        self.label_34 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font8)
        self.label_34.setPixmap(QPixmap(u":/icons/icons/diagramma1.jpg"))
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.label_34)

        self.label_33 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font8)
        self.label_33.setPixmap(QPixmap(u":/icons/icons/diagramma4.jpg"))

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.label_33)

        self.label_32 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font8)
        self.label_32.setPixmap(QPixmap(u":/icons/icons/diagramma6.png"))
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.label_32)

        self.label_31 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font8)
        self.label_31.setPixmap(QPixmap(u":/icons/icons/diagramma2.jpg"))

        self.formLayout.setWidget(15, QFormLayout.SpanningRole, self.label_31)

        self.label_43 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font8)
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.label_43)

        self.label_42 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font8)

        self.formLayout.setWidget(20, QFormLayout.SpanningRole, self.label_42)

        self.label_41 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font8)
        self.label_41.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(22, QFormLayout.FieldRole, self.label_41)

        self.label_40 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font8)

        self.formLayout.setWidget(25, QFormLayout.SpanningRole, self.label_40)

        self.label_39 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font8)
        self.label_39.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(27, QFormLayout.FieldRole, self.label_39)

        self.label_38 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font8)

        self.formLayout.setWidget(30, QFormLayout.LabelRole, self.label_38)

        self.label_36 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font8)
        self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(32, QFormLayout.FieldRole, self.label_36)

        self.label_45 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font8)

        self.formLayout.setWidget(35, QFormLayout.LabelRole, self.label_45)

        self.label_47 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font8)
        self.label_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(36, QFormLayout.FieldRole, self.label_47)

        self.label_44 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font8)

        self.formLayout.setWidget(39, QFormLayout.LabelRole, self.label_44)

        self.label_46 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font8)
        self.label_46.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(40, QFormLayout.FieldRole, self.label_46)

        self.label_37 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font8)

        self.formLayout.setWidget(41, QFormLayout.SpanningRole, self.label_37)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_14.addWidget(self.scrollArea_2)

        self.stackedWidget_2.addWidget(self.bazadagi_mahsulotlar_grafik_frame)

        self.verticalLayout_11.addWidget(self.stackedWidget_2)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.bazadagi_mahsulotlar_frame)
        self.yangi_mahsulot_qushish_frame = QWidget()
        self.yangi_mahsulot_qushish_frame.setObjectName(u"yangi_mahsulot_qushish_frame")
        self.verticalLayout_16 = QVBoxLayout(self.yangi_mahsulot_qushish_frame)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.yangi_mahsulot_qushish_frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy4)
        self.frame_5.setStyleSheet(u"QLineEdit{\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-left-radius:8px;\n"
"border-top-right-radius:8px;\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(230, 0, 0, 205), stop:1 rgba(13, 189, 0, 244));\n"
"background-color: rgba(224, 255, 232, 30);\n"
"\n"
"}\n"
"\n"
"#saqlash_btn:hover{\n"
"padding-right:3px;\n"
"padding-top:2px;\n"
"background-color: rgba(224, 255, 252, 20);\n"
"\n"
"}\n"
"#saqlash_btn:pressed{\n"
"padding-left:3px;\n"
"padding-bottom:2px;\n"
"background-color: rgba(224, 255, 252, 50);\n"
"\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_6)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 20)
        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font8)

        self.verticalLayout_17.addWidget(self.label_12, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_6, 0, 0, 1, 1)

        self.label_51 = QLabel(self.frame_5)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font9)
        self.label_51.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_51, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.frame_5)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)
        self.comboBox.setMinimumSize(QSize(180, 0))
        self.comboBox.setMaximumSize(QSize(300, 16777215))
        self.comboBox.setStyleSheet(u"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-left-radius:8px;\n"
"border-top-right-radius:8px;\n"
"border-bottom:2px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(230, 0, 0, 205), stop:1 rgba(13, 189, 0, 244));\n"
"background-color: rgba(224, 255, 232, 30);")
        self.comboBox.setEditable(True)
        self.comboBox.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 6)

        self.label_52 = QLabel(self.frame_5)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font9)
        self.label_52.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_52, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy2.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy2)
        self.lineEdit_3.setMinimumSize(QSize(180, 0))
        self.lineEdit_3.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_3.setFont(font9)
        self.lineEdit_3.setStyleSheet(u"")
        self.lineEdit_3.setMaxLength(35)
        self.lineEdit_3.setCursorPosition(0)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_3.setDragEnabled(False)
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_3.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 6)

        self.label_53 = QLabel(self.frame_5)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font9)
        self.label_53.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_53, 3, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy2.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy2)
        self.lineEdit_4.setMinimumSize(QSize(180, 0))
        self.lineEdit_4.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_4.setFont(font9)
        self.lineEdit_4.setStyleSheet(u"")
        self.lineEdit_4.setMaxLength(35)
        self.lineEdit_4.setCursorPosition(0)
        self.lineEdit_4.setAlignment(Qt.AlignCenter)
        self.lineEdit_4.setDragEnabled(False)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_4.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 6)

        self.label_54 = QLabel(self.frame_5)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font9)
        self.label_54.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_54, 4, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy2.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy2)
        self.lineEdit_5.setMinimumSize(QSize(180, 0))
        self.lineEdit_5.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_5.setFont(font9)
        self.lineEdit_5.setStyleSheet(u"")
        self.lineEdit_5.setMaxLength(35)
        self.lineEdit_5.setCursorPosition(0)
        self.lineEdit_5.setAlignment(Qt.AlignCenter)
        self.lineEdit_5.setDragEnabled(False)
        self.lineEdit_5.setReadOnly(False)
        self.lineEdit_5.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 6)

        self.label_55 = QLabel(self.frame_5)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font9)
        self.label_55.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_55, 5, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_5)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy2.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy2)
        self.lineEdit_6.setMinimumSize(QSize(180, 0))
        self.lineEdit_6.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_6.setFont(font9)
        self.lineEdit_6.setStyleSheet(u"")
        self.lineEdit_6.setMaxLength(35)
        self.lineEdit_6.setCursorPosition(0)
        self.lineEdit_6.setAlignment(Qt.AlignCenter)
        self.lineEdit_6.setDragEnabled(False)
        self.lineEdit_6.setReadOnly(False)
        self.lineEdit_6.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout.addWidget(self.lineEdit_6, 5, 1, 1, 6)

        self.label_56 = QLabel(self.frame_5)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout.addWidget(self.label_56, 7, 2, 2, 1)

        self.label_57 = QLabel(self.frame_5)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(20, 50))
        font15 = QFont()
        font15.setPointSize(17)
        self.label_57.setFont(font15)

        self.gridLayout.addWidget(self.label_57, 7, 3, 2, 4)

        self.label_58 = QLabel(self.frame_5)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(20, 50))
        self.label_58.setFont(font15)

        self.gridLayout.addWidget(self.label_58, 8, 4, 2, 3)

        self.label_59 = QLabel(self.frame_5)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(20, 50))
        self.label_59.setFont(font15)

        self.gridLayout.addWidget(self.label_59, 9, 5, 1, 1)

        self.label_60 = QLabel(self.frame_5)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout.addWidget(self.label_60, 9, 6, 1, 1)

        self.saqlash_btn = QPushButton(self.frame_5)
        self.saqlash_btn.setObjectName(u"saqlash_btn")
        self.saqlash_btn.setMinimumSize(QSize(0, 30))
        self.saqlash_btn.setFont(font4)
        self.saqlash_btn.setStyleSheet(u"border-radius:8px;\n"
"")

        self.gridLayout.addWidget(self.saqlash_btn, 10, 1, 1, 6)

        self.label_50 = QLabel(self.frame_5)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout.addWidget(self.label_50, 9, 3, 1, 1)


        self.verticalLayout_16.addWidget(self.frame_5, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.stackedWidget.addWidget(self.yangi_mahsulot_qushish_frame)
        self.yaroqlilik_muddati_frame = QWidget()
        self.yaroqlilik_muddati_frame.setObjectName(u"yaroqlilik_muddati_frame")
        self.label_49 = QLabel(self.yaroqlilik_muddati_frame)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(30, 40, 261, 181))
        self.label_49.setFont(font8)
        self.stackedWidget.addWidget(self.yaroqlilik_muddati_frame)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout_5.addWidget(self.main_body_frame)

        self.main_body_info_widget = QWidget(self.body_frame)
        self.main_body_info_widget.setObjectName(u"main_body_info_widget")
        self.main_body_info_widget.setMinimumSize(QSize(0, 0))
        self.main_body_info_widget.setMaximumSize(QSize(0, 16777215))
        self.main_body_info_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(10, 15, 5);\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.main_body_info_widget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 10)
        self.info_top_frame = QFrame(self.main_body_info_widget)
        self.info_top_frame.setObjectName(u"info_top_frame")
        sizePolicy1.setHeightForWidth(self.info_top_frame.sizePolicy().hasHeightForWidth())
        self.info_top_frame.setSizePolicy(sizePolicy1)
        font16 = QFont()
        font16.setFamily(u"Narkisim")
        font16.setPointSize(15)
        self.info_top_frame.setFont(font16)
        self.info_top_frame.setStyleSheet(u"")
        self.info_top_frame.setFrameShape(QFrame.StyledPanel)
        self.info_top_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.info_top_frame)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.info_top_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 65))
        self.label_3.setMaximumSize(QSize(111111, 50))
        self.label_3.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.label_3.setFrameShape(QFrame.StyledPanel)
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setLineWidth(10)
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setPixmap(QPixmap(u":/icons/icons/ICT_academy_02.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)
        self.label_3.setMargin(3)
        self.label_3.setIndent(-1)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_7.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.info_top_frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy5)
        font17 = QFont()
        font17.setFamily(u"Narkisim")
        font17.setPointSize(10)
        font17.setBold(False)
        font17.setItalic(True)
        font17.setUnderline(False)
        font17.setWeight(50)
        font17.setStrikeOut(False)
        font17.setKerning(True)
        font17.setStyleStrategy(QFont.PreferAntialias)
        self.label_4.setFont(font17)
        self.label_4.setMouseTracking(False)
        self.label_4.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_7.addWidget(self.label_4)

        self.label_5 = QLabel(self.info_top_frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy5.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy5)
        self.label_5.setFont(font17)
        self.label_5.setMouseTracking(False)
        self.label_5.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.info_top_frame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy5.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy5)
        self.label_6.setFont(font17)
        self.label_6.setMouseTracking(False)
        self.label_6.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_7.addWidget(self.label_6)

        self.label_7 = QLabel(self.info_top_frame)
        self.label_7.setObjectName(u"label_7")
        sizePolicy5.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy5)
        self.label_7.setFont(font17)
        self.label_7.setMouseTracking(False)
        self.label_7.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_7.addWidget(self.label_7)

        self.label_8 = QLabel(self.info_top_frame)
        self.label_8.setObjectName(u"label_8")
        sizePolicy5.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy5)
        self.label_8.setFont(font17)
        self.label_8.setMouseTracking(False)
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setInputMethodHints(Qt.ImhHiddenText)

        self.verticalLayout_7.addWidget(self.label_8)

        self.label_9 = QLabel(self.info_top_frame)
        self.label_9.setObjectName(u"label_9")
        sizePolicy5.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy5)
        self.label_9.setFont(font17)
        self.label_9.setMouseTracking(False)
        self.label_9.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_7.addWidget(self.label_9)

        self.label_10 = QLabel(self.info_top_frame)
        self.label_10.setObjectName(u"label_10")
        sizePolicy5.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy5)
        self.label_10.setFont(font17)
        self.label_10.setMouseTracking(False)
        self.label_10.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_7.addWidget(self.label_10)

        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_6.raise_()

        self.verticalLayout_5.addWidget(self.info_top_frame, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_4 = QFrame(self.main_body_info_widget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_4)

        self.horizontalFrame_2 = QFrame(self.main_body_info_widget)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 14)
        self.pushButton_8 = QPushButton(self.horizontalFrame_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(30, 30))
        font18 = QFont()
        font18.setFamily(u"Social Media Circled")
        font18.setPointSize(14)
        self.pushButton_8.setFont(font18)
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.horizontalFrame_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(30, 30))
        self.pushButton_9.setFont(font18)
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.horizontalFrame_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(30, 30))
        self.pushButton_10.setFont(font18)
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.horizontalFrame_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(30, 30))
        self.pushButton_11.setFont(font18)
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.pushButton_11)


        self.verticalLayout_5.addWidget(self.horizontalFrame_2)

        self.pushButton_7 = QPushButton(self.main_body_info_widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy6)
        self.pushButton_7.setFont(font7)
        self.pushButton_7.setStyleSheet(u"border-radius:6px;")

        self.verticalLayout_5.addWidget(self.pushButton_7, 0, Qt.AlignBottom)


        self.horizontalLayout_5.addWidget(self.main_body_info_widget)


        self.verticalLayout.addWidget(self.body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 0, 0, 1)
        self.version_frame = QFrame(self.footer_frame)
        self.version_frame.setObjectName(u"version_frame")
        self.version_frame.setFrameShape(QFrame.StyledPanel)
        self.version_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.version_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.version_frame)
        self.label_2.setObjectName(u"label_2")
        font19 = QFont()
        font19.setPointSize(9)
        self.label_2.setFont(font19)

        self.verticalLayout_4.addWidget(self.label_2, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.version_frame, 0, Qt.AlignLeft)

        self.footer_center_frame = QFrame(self.footer_frame)
        self.footer_center_frame.setObjectName(u"footer_center_frame")
        self.footer_center_frame.setMinimumSize(QSize(150, 15))
        self.footer_center_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_center_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.footer_center_frame)

        self.frame = QFrame(self.footer_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.info_btn = QPushButton(self.frame)
        self.info_btn.setObjectName(u"info_btn")
        sizePolicy1.setHeightForWidth(self.info_btn.sizePolicy().hasHeightForWidth())
        self.info_btn.setSizePolicy(sizePolicy1)
        self.info_btn.setMinimumSize(QSize(15, 15))
        self.info_btn.setFont(font4)
        self.info_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.info_btn.setIconSize(QSize(16, 16))

        self.verticalLayout_13.addWidget(self.info_btn)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignRight)

        self.grip_frame = QFrame(self.footer_frame)
        self.grip_frame.setObjectName(u"grip_frame")
        self.grip_frame.setMinimumSize(QSize(10, 10))
        self.grip_frame.setMaximumSize(QSize(10, 10))
        font20 = QFont()
        font20.setPointSize(15)
        self.grip_frame.setFont(font20)
        self.grip_frame.setFrameShape(QFrame.StyledPanel)
        self.grip_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.grip_frame)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"User's Page", None))
        self.menu_open_close_btn.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"User's Pages", None))
        self.minimize_window_btn.setText("")
#if QT_CONFIG(shortcut)
        self.minimize_window_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.resize_window_btn.setText("")
#if QT_CONFIG(shortcut)
        self.resize_window_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.close_window_btn.setText("")
#if QT_CONFIG(shortcut)
        self.close_window_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"  Home", None))
        self.bazadagi_mahsulotlar_btn.setText(QCoreApplication.translate("MainWindow", u"Bazadagi Mahsulotlar", None))
        self.yangi_mahsulotlar_qushish_btn.setText(QCoreApplication.translate("MainWindow", u"Yangi mahsulot\n"
"qo'shish", None))
        self.mahsulotlarni_sotish_btn.setText(QCoreApplication.translate("MainWindow", u"Sotildi", None))
        self.hisob_kitob_btn.setText(QCoreApplication.translate("MainWindow", u"Hisobot", None))
        self.yaroqlilik_muddati_btn.setText(QCoreApplication.translate("MainWindow", u"Yaroqlilik muddati", None))
        self.info_open_close_btn.setText(QCoreApplication.translate("MainWindow", u" Info", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"sale", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Turi:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Oziq - ovqat", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Maishiy texnika", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Qurilish materiali", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Gazmollar", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Kasmetika", None))

        self.comboBox_2.setPlaceholderText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Nomi:", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Olma", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Anor", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Behi", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Uzum", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Nok", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"Limon", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"Ananas", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"Xurmo", None))

        self.comboBox_3.setPlaceholderText("")
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Miqdori:", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"kg", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Narhi:", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"minimal summa:", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"sdcs", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"oy", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Hi, Jaloliddin", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Xisobot", None))
        self.label_14.setText("")
        self.label_16.setText("")
        self.bazadagi_mahsulotlar_list_btn.setText(QCoreApplication.translate("MainWindow", u"list", None))
        self.bazadagi_mahsulotlar_grafik_btn.setText(QCoreApplication.translate("MainWindow", u"diagramma", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Turi", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nomi", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Qolgani", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Sotilgani", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Jami", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Sana", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Yaroqliligi", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"10", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem16 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Oziq-ovqat", None));
        ___qtablewidgetitem17 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Olma", None));
        ___qtablewidgetitem18 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"300", None));
        ___qtablewidgetitem19 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"500", None));
        ___qtablewidgetitem20 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"800", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"21.12.21", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"10", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_15.setText("")
        self.label_30.setText("")
        self.label_35.setText("")
        self.label_34.setText("")
        self.label_33.setText("")
        self.label_32.setText("")
        self.label_31.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Widget 4/2", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Turi:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Oziq - ovqat", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Maishiy texnika", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Qurilish materiali", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Gazmollar", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Kasmetika", None))

        self.comboBox.setPlaceholderText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Nomi:", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type ", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Miqdori:", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"kg", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Narhi:", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"so'm", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Yaroqlilik muddati:", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"oy", None))
        self.label_56.setText("")
        self.label_57.setText("")
        self.label_58.setText("")
        self.label_59.setText("")
        self.label_60.setText("")
        self.saqlash_btn.setText(QCoreApplication.translate("MainWindow", u"Saqlash", None))
        self.label_50.setText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"yaroqlilik muddati", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Name: Base Name", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"First Name: User Fisrt Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Last Name: User Last Name", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Number Stores: Number Of Stores", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Adress: Adress", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Email: Email", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Telephone: Telephone", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | CopyRight", None))
        self.info_btn.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

