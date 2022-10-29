import sys, os

try:
  from PyQt5 import QtWidgets
  from PyQt5.QtWidgets import *
  from PyQt5 import uic, QtGui, QtCore
  import pyrebase
  from PyQt5.QtGui import *
  from PyQt5.QtCore import *

except:
  os.system("pip install -r requirements.txt")


thisPath = os.path.dirname(os.path.abspath(__file__))
uiPath = os.path.join(thisPath, 'ui')

userNow = ["Anon"]