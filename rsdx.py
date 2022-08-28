import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("REDSHIFT Index")
window.setFixedWidth(800)
window.setFixedHeight(600)
window.setStyleSheet(
    "background: #1e1f1e;"
    )

#       REDSHIFT LOGO

grid = QGridLayout()
logo = QLabel()
thisPath = os.getcwd()
image = QPixmap(str(thisPath) + "/RSDX/assets/img/logo/rsdx.png")
print(thisPath)
image = image.scaled(180,50)
logo.setPixmap(image)
logo.setAlignment(Qt.AlignHCenter)
logo.setStyleSheet(
    "margin: 30px 0;"
)


#           WELCOME MESSAGE


wlcMsg = QLabel("Welcome to RedShift Index!")
wlcMsg.setStyleSheet(
    "background: white;"
    "color: gray;"
)



#           LOGIN / SIGNUP / GUEST BUTTONS

login_button = QPushButton("LOGIN")
login_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
login_button.setStyleSheet(
    "* {background: '#03fc66';" 
    "color:white;" 
    "font-size: 20px;" 
    "border-radius:10px;"
    "margin: 0px 100px 2px 100px;"
    "padding:20px;}" 
    " *:hover{ background: 'white'; color: 'black'; } "
)

reg_button = QPushButton("SIGN UP")
reg_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
reg_button.setStyleSheet(
    "* {background: '#03cafc';"
    "color:white;"
    "font-size: 20px;" 
    "border-radius:10px;"
    "margin: 0px 100px 2px 100px;"
    "padding:20px;}" 
    " *:hover{ background: 'white'; color: 'black'; } "
)


anon_button = QPushButton("BROWSE ANONYMOUSLY")
anon_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
anon_button.setStyleSheet(
    "* {background: '#575757';"
    "color:white;"
    "font-size: 20px;" 
    "border-radius:10px;"
    "margin: 0px 100px 150px 100px;"
    "padding:20px;}" 
    " *:hover{ background: 'white'; color: 'black'; } "
)



grid.addWidget(logo, 0, 0)
grid.addWidget(login_button,1,0)
grid.addWidget(reg_button, 2, 0)
grid.addWidget(anon_button, 3, 0)

window.setLayout(grid)
window.show()
sys.exit(app.exec())