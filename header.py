import sys, os

try:
  from PyQt5 import QtWidgets
  from PyQt5.QtWidgets import *
  from PyQt5 import uic, QtGui
  import pyrebase
  from PyQt5.QtGui import QFont, QFontDatabase

except:
  os.system("pip install -r requirements.txt")


thisPath = os.path.dirname(os.path.abspath(__file__))
uiPath = os.path.join(thisPath, 'ui')

userNow = ["Anon"]
