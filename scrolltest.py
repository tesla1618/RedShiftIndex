from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        for i in range(1,50):
            object = QLabel("ব্ল্যাক হোল হচ্ছে মহাকাশের এমন একটি বিশেষ স্থান যেখান থেকে কোন কিছু এমনকি আলোও পর্যন্ত বের হয়ে আসতে পারে না। ব্ল্যাক হোল বা কৃষ্ণ বিবরের ভর এবং ঘনত্ব অনেক। মহাবিশ্বকে একটি বিছানার চাদরের মত তুলনা করলে এবং সেই বিছানার চাদরের উপর ভারী কোন বস্তু, ধরা যাক কিছু ভারী মার্বেল রাখা হলে চাদরটির উপরে যে সকল স্থানে মার্বেলগুলো রাখা হয়েছে দেখা যাবে সেসব স্থানে একটু নিচু গর্তের সৃষ্টি হয়েছে। মহাবিশ্বের ক্ষেত্রেও অনেকটা এমন।\n\nমহাবিশ্বের যেসকল স্থানে অসীম ভরের কোন বস্তুর উপস্থিতি থাকে সেখানেই এরূপ গর্তের সৃষ্টি হয় যা স্থানকালকে বাঁকিয়ে দেয়। কৃষ্ণ বিবর বা ব্ল্যাক হোলের মহাকর্ষ এত বেশি যে এর থেকে মহাশূন্যে আলোও বিকরিত হতে পারে না।\n\nআমরা জেনে গেছি ব্ল্যাকহোল কী। কিন্তু ব্ল্যাকহোল দেখতে কেমন?  আসলে ব্ল্যাকহোল দেখতে কেমন সেটা সঠিকভাবে বলা মুশকিল। কেননা ব্ল্যাকহোলের আকর্ষণ এতই বেশি যে ব্ল্যাকহোল থেকে আলোও বেঁচে ফিরতে পারেনা। আর আমরা সাধারণত সেসব বস্তুই দেখতে পাই যেগুলো থেকে আলো প্রতিফলিত হয়ে আমাদের চোখে ফিরে আসে। \n\n\nএখন আমরা জানব কেন ব্ল্যাকহোল থেকে আলো প্রতিফলিত হয়ে ফিরে আসতে পারে না। ")
            self.vbox.addWidget(object)

        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Scroll Area Demonstration')
        self.show()

        return

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()