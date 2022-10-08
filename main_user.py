import sys, os
from PySide2 import *
from ui_User_Ui_2 import *

from Custom_Widgets.Widgets import *



class MainWindow_user(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # loadJsonStyle(self, self.ui)


        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(150)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,92,157,250))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)



##########################################################################################
########  RESIZE WINDOW #############
##########################################################################################
        QSizeGrip(self.ui.grip_frame)
##########################################################################################

##########################################################################################
##############   birinchi ochiladigan sahifalar ##################
##########################################################################################
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_frame)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.bazadagi_mahsulotlar_list_frame)


##########################################################################################
############## BUTTON CLICKED ACTIONS ############################
##########################################################################################
        self.ui.minimize_window_btn.clicked.connect(lambda:self.showMinimized())
        self.ui.close_window_btn.clicked.connect(lambda:self.close())
        self.ui.resize_window_btn.clicked.connect(lambda:self.restore_or_maximize_window())

        self.ui.info_open_close_btn.clicked.connect(lambda:self.slideInfo())
        self.ui.info_btn.clicked.connect(lambda:self.slideInfo())
        self.ui.menu_open_close_btn.clicked.connect(lambda:self.slideMenu())




        self.ui.home_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.home_frame))
        self.ui.bazadagi_mahsulotlar_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.bazadagi_mahsulotlar_frame))
        self.ui.yangi_mahsulotlar_qushish_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.yangi_mahsulot_qushish_frame))
        self.ui.mahsulotlarni_sotish_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.mahsulotlarni_sotish_frame))
        self.ui.hisob_kitob_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.hisob_kitob_frame))
        self.ui.yaroqlilik_muddati_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.yaroqlilik_muddati_frame))
        self.ui.bazadagi_mahsulotlar_list_btn.clicked.connect(lambda:self.ui.stackedWidget_2.setCurrentWidget(self.ui.bazadagi_mahsulotlar_list_frame))
        self.ui.bazadagi_mahsulotlar_grafik_btn.clicked.connect(lambda:self.ui.stackedWidget_2.setCurrentWidget(self.ui.bazadagi_mahsulotlar_grafik_frame))




##########################################################################################
##########################################################################################


##########################################################################################
   ######## WINDOW MOVE ########################
##########################################################################################
        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    #Move window
                    self.move(self.pos() + e.globalPos()- self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        #mouse clicked event
        self.ui.header_frame.mouseMoveEvent = moveWindow
##########################################################################################
##########################################################################################



    ############################################################################
    ################    RUNNING PROGRAMM     ##########################
    ############################################################################
        self.show()
    ############################################################################
    ############################################################################





    #########################################################################3
    ### mouse position
    ###########################################################################
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
    ############################################################################
    ############################################################################





##########################################################################################
################# Main command  --> resize window ################3
##########################################################################################
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.resize_window_btn.setIcon(QtGui.QIcon(u":/icons/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.resize_window_btn.setIcon(QtGui.QIcon(u":/icons/icons/minimize-2.svg"))
##########################################################################################
##########################################################################################




##########################################################################################
    ###########   SliDE MENU AND INFO FRAME ACTIONS ###################333
##########################################################################################

    def slideMenu(self):
        global frame
        frame = self.ui.main_body_menu_widget
        self.slide()


    def slideInfo(self):
        global frame
        frame = self.ui.main_body_info_widget
        self.slide()


    def slide(self):
        width = frame.width()
        if width == 0:
            newWidth = 200
        else:
            newWidth = 0
        self.animation = QPropertyAnimation(frame,b"minimumWidth")
        self.animation.setDuration(350)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.animation.start()

##########################################################################################
##########################################################################################




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())