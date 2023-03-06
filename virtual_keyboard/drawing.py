from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt, QThread, QSize

import sys

eng_lower = ['`','!','@','#','$','%','^','&&','*','(',')','_','+','⟵',
             'Tab', '','q','w','e','r','t','y','u','i','o','p','{','}',
             'Caps Lock','','a','s','d','f','g','h','j','k','l','"','Enter','',
             'Shift', '','z','x','c','v','b','n','m','<','>','?',':', '\\',
             'Ctrl','Win','Alt',' ','','','','','','','','','']
eng_upper = ['`','1','2','3','4','5','6','7','8','9','0','-','=','⟵',
             'Tab', '','Q','W','E','R','T','Y','U','I','O','P','[',']',
             'Caps Lock','','A','S','D','F','G','H','J','K','L',"'",'Enter','',
             'Shift', '','Z','X','C','V','B','N','M',',','.','/',';', '|',
             'Ctrl','Win','Alt',' ','','','','','','','','','']
rus_lower = ['`','!','@','#','$','%','^','&&','*','(',')','_','+','⟵',
             'Tab', '','й','ц','у','к','е','н','г','ш','щ','з','х','ъ',
             'Caps Lock','','ф','ы','в','а','п','р','о','л','д','э','Enter','',
             'Shift', '','я','ч','с','м','и','т','ь','б','ю','?','ж', '\\',
             'Ctrl','Win','Alt',' ','','','','','','','','','']
rus_upper = ['`','1','2','3','4','5','6','7','8','9','0','-','=','⟵',
             'Tab', '','Й','Ц','У','К','Е','Н','Г','Ш','Щ','З','Х','Ъ',
             'Caps Lock','','Ф','Ы','В','А','П','Р','О','Л','Д','Э','Enter','',
             'Shift', '','Я','Ч','С','М','И','Т','Ь','Б','Ю','/','Ж', '|',
             'Ctrl','Win','Alt',' ','','','','','','','','','']

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.shift_on = False
        self.alt_on   = False
        self.capsL_on = False
        self.rus_on   = False
        self.setWindowTitle('Экранная клавиатура')
        self.resize(900, 120)
        self.setStyleSheet("background-color: #636060;")

        self.initkey_b()
    def initkey_b(self):
        self.layout = QGridLayout()

        positions = [(i,j) for i in range(5) for j in range(14)]
        for position, name in zip(positions, eng_lower):
            if name == '': continue
            button = QPushButton(name)

            self.add_setstyle(button, position, '6e6b6b')

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
    def add_setstyle(self, button, position, color):
        button.setFont(QFont('Times', 16))
        button.clicked.connect(self.click_key)
        button.setMinimumHeight(60)
        button.setMaximumHeight(120)
        if position == (1,0) or position == (2,0) or position == (2,12): 
            button.setMinimumWidth(120)
            self.layout.addWidget(button, *position, 1, 2) 
        elif position == (4,3): 
            button.setMinimumWidth(120)
            self.layout.addWidget(button, *position, 1, 11) 
        elif position == (3,0): 
            button.setMinimumWidth(120)
            self.layout.addWidget(button, *position, 1, 2) 
        else:
            button.setMinimumWidth(60)
            self.layout.addWidget(button, *position, 1, 1)

        button.setStyleSheet(f"""QPushButton {{border :2px solid;background-color: #{color};color: white;
                                               border-color: black;border-radius: 6px}}""")
                        #"QPushButton::hover{background-color: #827f7f;}")
                        #"QPushButton::pressed{background-color: #827f7f;font: bold 25px;}")

    def click_key(self):
        text = self.sender().text()
        if text == 'Shift'    : self.click_shift()
        if text == 'Caps Lock': self.click_capsLock()
        if text == 'Alt'      : self.click_alt(self.sender())
    def click_alt(self, butt_parent):
        self.alt_on = True if self.alt_on is False else False
        color = '827f7f' if self.alt_on else '6e6b6b'
        butt_parent.setStyleSheet(f"""QPushButton {{border: 2px solid;background-color: #{color};color: white;
                                                    border-color: black;border-radius: 6px}}""")
    def click_shift(self):
        print('shift')
        if self.shift_on is False:
            upper = eng_upper
            self.shift_on = True
        else: 
            upper = eng_lower
            self.shift_on = False

        for i in reversed(range(self.layout.count())): 
                self.layout.itemAt(i).widget().setParent(None)
        positions = [(i,j) for i in range(5) for j in range(14)]
        for position, name in zip(positions, upper):
            if name == '': continue
            button = QPushButton(name)
            color_press = '827f7f' if  (position == (3,0) and self.shift_on) or (position == (4,2) and self.alt_on) else '6e6b6b'
            self.add_setstyle(button, position, color_press)
    def click_capsLock(self):
        if (self.capsL_on is False) and (self.shift_on is False):
            upper = eng_upper
            self.capsL_on = True
        elif (self.capsL_on is False) and (self.shift_on is True):
            upper = eng_lower
            self.capsL_on = True
        else: 
            upper = eng_lower
            self.capsL_on = False

        for i in reversed(range(self.layout.count())): 
                self.layout.itemAt(i).widget().setParent(None)
        positions = [(i,j) for i in range(5) for j in range(14)]
        for position, name in zip(positions, upper):
            if name == '': continue
            button = QPushButton(name)
            color_press = '827f7f' if  (position == (2,0) and self.capsL_on) or (position == (3,0)  and self.shift_on) else '6e6b6b'
            self.add_setstyle(button, position, color_press)
    
    def butt_3some(self):
        pass












if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = Window()
    myWin.show()
    sys.exit(app.exec())
