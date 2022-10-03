from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys, os
from PyQt5 import uic, QtGui
import pyrebase


thisPath = os.path.dirname(os.path.abspath(__file__))
uiPath = os.path.join(thisPath, 'ui')

firebaseConfig = {
  "apiKey": "AIzaSyDkciGQD5dqLBciewRUFNO9GV3s9_r8W4U",
  "authDomain": "redshiftindex.firebaseapp.com",
  "projectId": "redshiftindex",
  "storageBucket": "redshiftindex.appspot.com",
  "messagingSenderId": "234120744788",
  "appId": "1:234120744788:web:9bc96b22d4d384c9c9c2c1",
  "measurementId": "G-SYC9E2Q4QR",
  "databaseURL": "https://redshiftindex-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
