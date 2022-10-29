#       Configuring dBconf.py so it can be imported here as a module
import sys
import os
curDir = os.path.dirname(os.path.realpath(__file__))    #   Getting current directory
dbPath = os.path.join(curDir, 'database')               #   Joining database folder with curDir
sys.path.append(dbPath)                                 #   Adding the dBconf.py to sys


#       Importing dBconfig.py file from RedShift/database
import dBconf

from header import *
from fconfig import *

whichObj = []
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

        self.setWindowTitle("RedShift")
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

        #   Hiding Error Message initially
        self.errorMsg.hide()
        

        self.show()

        self.loginBtn.clicked.connect(self.methodLogin)
        self.regBtn.clicked.connect(self.goToReg)

    def methodLogin(self):
        un = self.uname.text()
        userNow[0] = un
        # un = un + "@red.shift"
        pwd = self.passwd.text()

        if un == "admin":
            dBconf.makeUserLoggedIn(un,pwd)
            if dBconf.makeUserLoggedIn.fetchError == False:
                userNow[0] = "adminrsdx"
                redirect("AdminPanel")
            else:
                self.wlcText.hide()
                self.errorMsg.show()
        else:
            dBconf.makeUserLoggedIn(un,pwd)

            if dBconf.makeUserLoggedIn.fetchError == False:
                redirect("HomePage")
            else:
                self.wlcText.hide()
                self.errorMsg.show()

        
        # try:
        #     # auth.sign_in_with_email_and_password(un, pwd)
        #     dBconf.makeUserLoggedIn(un,pwd)
        #     redirect("HomePage")
        # except:
        #     self.wlcText.hide()
        #     self.errorMsg.show()
        #     # UI.loginPage(self)
    def goToReg(self):
        rdTo = "RSDXRegPage"
        redirect(rdTo)

class RSDXRegPage(QMainWindow):
    def __init__(self):
        super(RSDXRegPage, self).__init__()


        uic.loadUi(uiPath+"/reg_page.ui", self)
        self.logo.setPixmap(QtGui.QPixmap('rsdx.png'))

        #   Hiding Error Message initially
        self.errorMsg.hide()

        self.show()
        self.regBtn.clicked.connect(self.verify)
        self.loginBtn.clicked.connect(self.gotAccount)


    def gotAccount(self):
        redirect("RSDXLoginPage")

    def verify(self):
        un = self.uname.text()
        unl = self.uname.text()
        # un = un + "@red.shift"
        pwd = self.passwd.text()
        pwd2 = self.passwd_2.text()
        if pwd == pwd2:
            # try:
            dBconf.makeUserRegistered(un,pwd)
            
            if dBconf.makeUserRegistered.fetchError == False:
                redirect("HomePage")
                unl = un
                userNow[0] = unl
                userLoggedIn = True
            else:
                self.wlcText.hide()
                self.errorMsg.show()
                
        else:
            self.wlcText.hide()
            self.errorMsg.show()


class HomePage(QMainWindow):
    def __init__(self):
        # print(userNow[0])
        super(HomePage, self).__init__()
        uic.loadUi(uiPath+"/homepage.ui", self)
        self.logo.setPixmap(QtGui.QPixmap('rsdx.png'))
        self.wlcText.setText("Welcome "+ userNow[0])
        self.imgMain.setPixmap(QtGui.QPixmap('saturn-v2.jpg'))
        # self.post.setWordWrap(True)
        # self.scrollArea.setWidget(self.post)      
        
        if not userLoggedIn:
            self.shutBtn.hide()
        self.show()

        self.shutBtn.clicked.connect(self.shutUser)
        self.nextPage.clicked.connect(lambda: self.nPage("Pluto"))
        self.gearBtn.clicked.connect(lambda: redirect("UserSettings"))

    def nPage(self, tag):
        tag = "saturn"
        if tag == "saturn":
            uic.loadUi(uiPath+"/addObject.ui", self)
            self.logo.setPixmap(QtGui.QPixmap('rsdx.png'))
            self.objName.setPlaceholderText("Name of Object")
            self.objMass.setPlaceholderText("Mass of Object")
            self.objRadius.setPlaceholderText("Radius of Object")
            self.objDisEarth.setPlaceholderText("Distance of Object from Earth")
            self.objMadeOf.setPlaceholderText("Object Made of")
            self.objLum.setPlaceholderText("Luminosity of Object")
            self.isVisible.setPlaceholderText("Visible in naked eye from earth?")
            self.briefInfo.setPlaceholderText("Write more about the Object briefly")
            # self.imgMain.setPixmap(QtGui.QPixmap('saturn-v2.jpg'))
            # self.imgMain_2.setPixmap(QtGui.QPixmap('saturn-v2.jpg'))
            # self.nextPage.clicked.connect(lambda: redirect("HomePage"))
            
        else:
            whichObj.append(tag)
            redirect("InfoPage")


    def shutUser(self):
        userNow[0] = "Anon"
        redirect("UI")

class InfoPage(QMainWindow):
    def __init__(self):
        super(InfoPage, self).__init__()
        uic.loadUi(uiPath+"/planet_info.ui", self)
        self.logo.setPixmap(QtGui.QPixmap('rsdx.png'))
        self.imgMain.setPixmap(QtGui.QPixmap('saturn-v2.jpg'))
        self.objName.setText("About "+ whichObj[0])
        


class AdminPanel(QMainWindow):
    def __init__(self):
        super(AdminPanel, self).__init__()
        self.addObj()
    def addObj(self):
        uic.loadUi(uiPath+"/addObject.ui", self)
        self.logo.setPixmap(QtGui.QPixmap('rsdx.png'))
        self.logo.setPixmap(QtGui.QPixmap('rsdx.png'))
        self.objName.setPlaceholderText("Name of Object")
        self.objMass.setPlaceholderText("Mass of Object")
        self.objRadius.setPlaceholderText("Radius of Object")
        self.objDisEarth.setPlaceholderText("Distance of Object from Earth")
        self.objMadeOf.setPlaceholderText("Object Made of")
        self.objLum.setPlaceholderText("Luminosity of Object")
        self.isVisible.setPlaceholderText("Visible in naked eye from earth?")
        self.briefInfo.setPlaceholderText("Write more about the Object briefly")

        self.addBtn.clicked.connect(self.addtoDB)
        self.browseBtn.clicked.connect(self.addThumb)
        self.discardBtn.clicked.connect(self.discardTo)

    def discardTo(self):
        redirect("AdminPanel")
    
    def addThumb(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath() , '*.jpg')
        self.thumbPath.setText(fileName)


    def addtoDB(self):
        name = self.objName.text()
        mass = self.objMass.text()
        radius = self.objRadius.text()
        disEarth = self.objDisEarth.text()
        madeOf = self.objMadeOf.text()
        lum = self.objLum.text()
        visible = self.isVisible.text()
        brinfo = self.briefInfo.toPlainText()
        thumbPath = self.thumbPath.text()
        # os.system(f"cp {thumbPath} {pk} {curDir}/images/thumbnails")
        # newThumbPath = str(curDir)+"/images/thumbnails/"
        # print(name,mass,radius,disEarth,madeOf,lum,visible,brinfo,thumbPath)
        if len(name) != 0:
            dBconf.addObjInfoToDB(name,mass,radius,disEarth,madeOf,lum,visible,brinfo,thumbPath)
        else:
            self.objName.setStyleSheet("border: 1px solid red")


class UserSettings(QMainWindow):

    def __init__(self):
        super(UserSettings, self).__init__()
        uic.loadUi(uiPath+"/user_settings.ui", self)
        self.logo.setPixmap(QtGui.QPixmap('rsdx.png'))

        self.updateUname.setDisabled(True)
        self.updateUname.setPlaceholderText(userNow[0])
        self.returnBtn.clicked.connect(lambda: redirect("HomePage"))
        self.show()



app = QApplication(sys.argv)
fontbase = QtGui.QFontDatabase()
eng = fontbase.addApplicationFont("/Bengali.ttf")
cascode = QtGui.QFont("Baloo Da 2", 12)
app.setFont(cascode)



rsdx = UI()
widget = QtWidgets.QStackedWidget()
widget.addWidget(rsdx)
widget.setWindowIcon(QtGui.QIcon('redshift_icon.png'))
widget.setWindowTitle("RedShift Index")
widget.setFixedHeight(550)
widget.setFixedWidth(720)
widget.show()
app.exec_()