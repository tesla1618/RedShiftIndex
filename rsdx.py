import sys, os, random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("REDSHIFT Index")
window.setFixedWidth(900)
window.setFixedHeight(650)

grid = QGridLayout()



#       ASSETS STORED GLOBALLY

assets = {
    "logo": [],
    "login_button": [],
    "reg_button": [],
    "anon_button": [],
    "uname_tbox": [],
    "passwd_tbox": [],
    "txt": []
}

#       LOGO PATH


thisPath = os.path.dirname(os.path.abspath(__file__))
logoPath = os.path.join(thisPath, 'assets','img','logo','rsdx.png')
# print(logoPath)

images = {
    "logo": [logoPath]
}

#       RESET ITEMS OF WINDOWS

def reset_window():
    for asset in assets:
        if assets[asset] != []:
            assets[asset][-1].hide()
        for i in range(0, len(assets[asset])):
            assets[asset].pop()
        




#       CUSTOM PAGE FUNCTIONS
class LoginPage(QDialog):
    

    def __init__(self):
        super(LoginPage, self).__init__()
        reset_window()
        print(f"CLICKED")
        window.setStyleSheet(
        "background: #1e1f1e;"
        )

        logo = QLabel()
        thisPath = os.getcwd()
        image = QPixmap(str(logoPath))
        print(thisPath)
        image = image.scaled(199,50)
        logo.setPixmap(image)
        logo.setAlignment(Qt.AlignTop)
        logo.setStyleSheet(
            "margin: 30px 0 0 30px;"
            "text-align: center;"
        )

        assets["logo"].append(logo)


        login_menu_text = QLabel("Login to your existing account!")
        login_menu_text.setStyleSheet(
            "margin: 3px 30px 4px 30px;"
            "color: white;"
        )

        assets["txt"].append(login_menu_text)

        self.uname = QLineEdit()
        self.uname.setAlignment(Qt.AlignLeft)
        self.uname.setPlaceholderText("NAME")
        self.uname.setStyleSheet(
            "border: 1px solid gray;"
            "padding: 18px;"
            "color: #303030;"
            "background: white;"
            "margin:3px 180px 3px 180px;"
            "border-radius: 8px;"
        )

        

        assets["uname_tbox"].append(self.uname)

        passwd = QLineEdit()
        passwd.setAlignment(Qt.AlignLeft)
        passwd.setPlaceholderText("PASSWORD")
        passwd.setStyleSheet(
            "border: 1px solid gray;"
            "padding: 18px;"
            "color: #303030;"
            "background: white;"
            "margin:3px 180px 3px 180px;"
            "border-radius: 8px;"
        )

        assets["passwd_tbox"].append(passwd)


        self.login_button = QPushButton("LOGIN")
        self.login_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.login_button.setStyleSheet(
            "* {border: 1px solid '#239e79';"
            "background: #239e79;" 
            "color:white;" 
            "font-size: 20px;" 
            "border-radius:8px;"
            "margin: 3px 180px 250px 180px;"
            "padding:20px;}" 
            " *:hover{ background: none; color: 'white'; } "
        )
        assets["login_button"].append(self.login_button)
        self.login_button.clicked.connect(homescreen)

        grid.addWidget(assets["logo"][-1],1,1)
        grid.addWidget(assets["txt"][-1],2,1)
        grid.addWidget(assets["uname_tbox"][-1],3,1)
        grid.addWidget(assets["passwd_tbox"][-1],4,1)
        grid.addWidget(assets["login_button"][-1],5,1)

    def clickTest(self):
        x = self.uname.text()
        prSt()
    def prSt(self):
        print(f"Success Code: 1000 - Connection done! ")



#HOMESCREEN FUNCTION

def homescreen():

    reset_window()

    window.setStyleSheet(
    "background: #1e1f1e;"
    "background-image: url('/home/tesla/SOFTDEV2/RSDX/assets/gifs/bg.jpg');"
    "background-repeat: no-repeat;"
    "background-position: center;"
    )

    logo = QLabel()
    # print(fullPath)
    image = QPixmap(str(logoPath))
    # print(thisPath)
    image = image.scaled(199,50)
    logo.setPixmap(image)
    logo.setAlignment(Qt.AlignHCenter)
    logo.setStyleSheet(
        "margin: 30px 0;"
    )

    assets["logo"].append(logo)



    #           LOGIN / SIGNUP / GUEST BUTTONS

    login_button = QPushButton("LOGIN")
    login_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    login_button.setStyleSheet(
        "* {border: 1px solid '#239e79';" 
        "color:white;" 
        "font-size: 20px;" 
        "border-radius:30px;"
        "margin: 0px 180px 5px 180px;"
        "padding:20px;}" 
        " *:hover{ background: '#239e79'; color: 'white'; } "
    )
    assets["login_button"].append(login_button)
    login_button.clicked.connect(LoginPage)

    reg_button = QPushButton("SIGN UP")
    reg_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    reg_button.setStyleSheet(
        "* {border: 1px solid '#4387ba';"
        "color:white;"
        "font-size: 20px;" 
        "border-radius:30px;"
        "margin: 0px 180px 5px 180px;"
        "padding:20px;}" 
        " *:hover{ background: '#4387ba'; color: 'white'; } "
    )

    assets["reg_button"].append(reg_button)


    anon_button = QPushButton("BROWSE ANONYMOUSLY")
    anon_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    anon_button.setStyleSheet(
        "* {border: 1px solid '#575757';"
        "color:white;"
        "font-size: 20px;" 
        "border-radius:30px;"
        "margin: 0px 180px 150px 180px;"
        "padding:20px;}" 
        " *:hover{ background: '#575757'; color: 'white'; } "
    )

    assets["anon_button"].append(anon_button)



    grid.addWidget(assets["logo"][-1], 0, 0)
    grid.addWidget(assets["login_button"][-1],1,0)
    grid.addWidget(assets["reg_button"][-1], 2, 0)
    grid.addWidget(assets["anon_button"][-1], 3, 0)


homescreen()
window.setLayout(grid)
window.show()
sys.exit(app.exec())
