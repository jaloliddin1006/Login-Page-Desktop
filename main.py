import sys, os
from PySide2 import *
from qt_material import *
from ui_Admin_1 import *

from Custom_Widgets.Widgets import *


class MainWindow_admin(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

##############################################################
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,92,157,550))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
#####################################################################




        #####################################################################
        # header right frame
        #####################################################################
        self.ui.minimize_window_button.clicked.connect(lambda:self.showMinimized())
        self.ui.close_window_button.clicked.connect(lambda:self.close())
        self.ui.restore_window_button.clicked.connect(lambda:self.restore_or_maximize_window())
        #####################################################################
        #####################################################################



        ##### Asosiy ochiladigan sahifa########################
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_null_widget)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.null_base_info_widget)


        #####################################################################
        # menu button clicked change frame
        #####################################################################
        self.ui.add_new_base_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.create_new_base_widget))
        self.ui.add_new_base_btn_2.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.create_new_base_widget))
        self.ui.exists_bases_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.exists_bases_widget))
        self.ui.exists_bases_btn_2.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.exists_bases_widget))
        self.ui.base_statistic_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.statistic_widget))
        self.ui.base_statistic_btn_2.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.statistic_widget))




        self.ui.first_base_btn.clicked.connect(lambda:self.ui.stackedWidget_2.setCurrentWidget(self.ui.main_base_info_widget))
        self.ui.print_info.clicked.connect(lambda:self.clickMethod)


        # def basesss(self):
        for w in self.ui.left_info_frame.findChildren(QPushButton):
            if w.clicked:
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.main_base_info_widget)

                    # self.ui.stackedWidget.setCurrentWidget(self.ui.create_new_base_widget)




        self.setWindowIcon(QtGui.QIcon(":/icons/icons/tool.svg"))
        self.setWindowTitle("Admin Page")



        QSizeGrip(self.ui.grid_frame)

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    #Move window
                    self.move(self.pos() + e.globalPos()- self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        #mouse clicked event
        self.ui.header_frame.mouseMoveEvent = moveWindow

    


        #####################################################################
        # #menu slide button  // left menu toggle button
        #####################################################################
        self.ui.menu_open_close_btn.clicked.connect(lambda:self.slideLeftMenu())
        #####################################################################
        self.ui.new_base_save_btn.clicked.connect(lambda:self.create_and_save_new_base())
        self.ui.notification_closed_btn_1.clicked.connect(lambda:self.notification1())

        
        #####################################################################


        #####################################################################
        #menu slide button with json
        #####################################################################
        # loadJsonStyle(self, self.ui)
        #####################################################################
        #####################################################################


        # # #style clicked button
        # for w in self.ui.menu_frame.findChildren(QPushButton):
        #     print('aaaaa')
        #     w.clicked.connect(lambda:self.applyButtonStyle())


        #####################################################################
        #####################################################################
        #####################################################################
        ###################  Admin Pages componentes   ######################
        #####################################################################
        #####################################################################
        #####################################################################

        self.ui.user_password1.textChanged.connect(lambda: self.validatePassword1())
        self.ui.user_password2.textChanged.connect(lambda: self.validatePassword2())







        #####################################################################
        #####################################################################
        #####################################################################
        #######################          END           ######################
        #####################################################################
        #####################################################################
        #####################################################################


        self.show()

    def clickMethod(self):
        ret = QMessageBox.question(self, 'MessageBox', "Click a button", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)

        if ret == QMessageBox.Yes:
            print('Button QMessageBox.Yes clicked.')







    #####################################################################
    #####################################################################
    #####################################################################
    ##############  Admin Pages componentes functions  ##################
    #####################################################################
    #####################################################################
    #####################################################################

    ###############33333# Changed password ########################
    def validatePassword1(self):
        if len(self.ui.user_password1.text()) >= 8:
            self.ui.pass_test_lb1.setPixmap(QPixmap(u":/icons/icons/check-circle (3).svg"))
        elif self.ui.user_password1.text() == "":
            self.ui.pass_test_lb1.setPixmap(QPixmap(u":/icons/icons/null.svg"))

        else:
            self.ui.pass_test_lb1.setPixmap(QPixmap(u":/icons/icons/x-circle (2).svg"))
    #####################################################################


    ######################## Coniform  password ########################
    def validatePassword2(self):
        if self.ui.user_password1.text() == self.ui.user_password2.text() and len(self.ui.user_password2.text()) >= 8:
            self.ui.pass_test_lb2.setPixmap(QPixmap(u":/icons/icons/check-circle (3).svg"))
        elif self.ui.user_password2.text() == "":
            self.ui.pass_test_lb2.setPixmap(QPixmap(u":/icons/icons/null.svg"))

        else:
            self.ui.pass_test_lb2.setPixmap(QPixmap(u":/icons/icons/x-circle (2).svg"))
    #####################################################################

    #####################################################################
    #####################################################################
        ####3 new base Save button @###########################
    #####################################################################


    def create_and_save_new_base(self):
        s = 0
        for w in self.ui.create_new_base_frame.findChildren(QLineEdit):
            if w.text()  == "":
                s += 1

        if s == 0:
            self.ui.label_17.setText("Saved Succesfully")
            self.ui.label_18.setPixmap(QPixmap(u":/icons/icons/check-circle (3).svg"))
            self.ui.notification_widget.setStyleSheet(u"#notification_widget{\n"
"\n"
"border-radius: 15px;\n"
"border: 2px solid rgb(0, 255, 0);}\n"
"\n"
"*{ background-color: rgb(1, 154, 136);}")
        else:
            self.ui.label_17.setText("There Are Some Errors")
            self.ui.label_18.setPixmap(QPixmap(u":/icons/icons/x-circle (2).svg"))

            self.ui.notification_widget.setStyleSheet(u"#notification_widget{\n"
"\n"
"border-radius: 15px;\n"
"border: 2px solid rgb(255, 0, 0);}\n"
"\n"
"*{ background-color: rgba(154, 41, 86, 255);}")


        self.ui.create_new_base_frame.setEnabled(False)
        self.notification1()


        print("save")
        
    #########################################################################3


    def notification1(self):
        height = self.ui.notification_widget.height()
        if height == 0:
            newheight = 50
        else:
            self.ui.create_new_base_frame.setEnabled(True)

            newheight = 0
        self.animation = QPropertyAnimation(self.ui.notification_widget,b"maximumHeight")
        self.animation.setDuration(350)
        self.animation.setStartValue(height)
        self.animation.setEndValue(newheight)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.animation.start()



    #####################################################################
    #####################################################################
    #####################################################################
    #######################          END           ######################
    #####################################################################
    #####################################################################
    #####################################################################

    #########################################################################3
    ### apply button style
    ###########################################################################
    # def applyButtonStyle(self):
    #     print("cliced btn style")
    #     for w in self.ui.main_body_frame.findChildren(QPushButton):
    #         if w.objectName() != self.sender().objectName():
    #             style = w.styleSheet().replace("background-color: rgb(250, 250, 250)")
    #             #apply the deafult style
    #             w.setStyleSheet(style)
                
    #     #apply the new style
    #         # else:
    #         #     style = w.styleSheet().replace("background-color: rgb(0, 0, 250)")

    #     # self.sender().setStyleSheet("border-bottom: 5px solid rgb(250, 250, 250)")
    #         # self.sender().setStyleSheet("background-color: rgb(250, 250, 250)")
    #         # w.setStyleSheet(style)
    #     return
    #########################################################################3
    ###########################################################################



    #########################################################################3
    ### menu slide // left frame
    ###########################################################################
    def slideLeftMenu(self):
        width = self.ui.body_left_frame.width()
        if width == 50:
            newWidth = 200
        else:
            newWidth = 50
        self.animation = QPropertyAnimation(self.ui.body_left_frame,b"minimumWidth")
        self.animation.setDuration(350)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.animation.start()
    #########################################################################3

  
    ###########################################################################




        
    #########################################################################3
    ### mouse position
    ###########################################################################
    def mousePressEvent(self, event):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.null_base_info_widget)

        self.clickPosition = event.globalPos()
    ############################################################################



    #########################################################################3
    ### window maxsimized or minimized function
    ###########################################################################
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/minimize-2.svg"))
    #########################################################################3
    ###########################################################################     



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())