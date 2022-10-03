from header import *
userLoggedIn = True


'''
        This function is to redirect a user to specific class depending on their
        choices. Instead of writing these lines of code of the function for all choices,
        a function has been created so that the code becomes more efficient
'''
def redirect(rdTo):
    rdTo = eval(rdTo + "()")
    menu = rdTo
    widget.addWidget(menu)
    widget.setCurrentIndex(widget.currentIndex()+1)
    return rdTo



class UI(QMainWindow):

    def __init__(self):
        super(UI, self).__init__()


        uic.loadUi(uiPath+"/main_window.ui", self)
        self.img = self.findChild(QLabel, 'logo')
        self.img.setStyleSheet(
            "color:white;"
        )
        self.logo.setPixmap(QtGui.QPixmap('rsdx.png'))

        self.log_btn = self.findChild(QPushButton, 'loginBtn')


        self.log_btn.clicked.connect(self.loginPage)
        self.regBtn.clicked.connect(self.regPage)
        self.anonBtn.clicked.connect(self.anonGetway)

        self.show()
    def loginPage(self):
        redirect("RSDXLoginPage")
    
    def regPage(self):
        redirect("RSDXRegPage")

    def anonGetway(self):
        redirect("HomePage")


class RSDXLoginPage(QMainWindow):
    def __init__(self):
        super(RSDXLoginPage, self).__init__()


        uic.loadUi(uiPath+"/login_page.ui", self)
        self.img = self.findChild(QLabel, 'logo')
        self.img.setStyleSheet(
            "color:white;"
        )
        self.logo.setPixmap(QtGui.QPixmap('rsdx.png'))
        self.show()

        self.loginBtn.clicked.connect(self.methodLogin)
        self.regBtn.clicked.connect(self.goToReg)

    def methodLogin(self):
        un = self.uname.text()
        pwd = self.passwd.text()
        try:
            auth.sign_in_with_email_and_password(un, pwd)
            redirect("HomePage")
        except:
            UI.loginPage(self)
    def goToReg(self):
        rdTo = "RSDXRegPage"
        redirect(rdTo)

class RSDXRegPage(QMainWindow):
    def __init__(self):
        super(RSDXRegPage, self).__init__()


        uic.loadUi(uiPath+"/reg_page.ui", self)
        self.logo.setPixmap(QtGui.QPixmap('rsdx.png'))
        self.show()

        self.regBtn.clicked.connect(self.verify)
        self.loginBtn.clicked.connect(self.gotAccount)


    def gotAccount(self):
        redirect("RSDXLoginPage")

    def verify(self):
        un = self.uname.text()
        pwd = self.passwd.text()
        pwd2 = self.passwd_2.text()
        if pwd == pwd2:
            try:
                auth.create_user_with_email_and_password(un, pwd)
                userLoggedIn = True
                redirect("HomePage")
            except:
                userLoggedIn = False
                redirect("RSDXRegPage")
        else:
            redirect("RSDXRegPage")


class HomePage(QMainWindow):
    def __init__(self):
        super(HomePage, self).__init__()
        uic.loadUi(uiPath+"/homepage.ui", self)
        self.logo.setPixmap(QtGui.QPixmap('rsdx.png'))
        if not userLoggedIn:
            self.shutBtn.hide()
        self.show()

        self.shutBtn.clicked.connect(lambda: redirect("UI"))



app = QApplication(sys.argv)
rsdx = UI()
widget = QtWidgets.QStackedWidget()
widget.addWidget(rsdx)
widget.setWindowIcon(QtGui.QIcon('redshift_icon.png'))
widget.setFixedHeight(550)
widget.setFixedWidth(720)
widget.show()
app.exec_()
