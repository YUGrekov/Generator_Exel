from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt, QThread, QSize

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Виртуальная клавиатура')
        self.resize(900, 120)
        self.setStyleSheet("background-color: #636060;")

        self.initkey_b()

    def initkey_b(self):
        keypad = ['`','1','2','3','4','5','6','7','8','9','0','-','=','⟵',
                  'TAB', '','q','w','e','r','t','y','u','i','o','p','[',']',
                  'Caps Lock','','a','s','d','f','g','h','j','k','l',';','Enter','',
                  'Shift', '','z','x','c','v','b','n','m',',','.','/','Shift', '',
                  'Ctrl','Win','Alt',' ','','','','','','','','','','']

        layout = QGridLayout()

        positions = [(i,j) for i in range(5) for j in range(14)]
        for position, name in zip(positions, keypad):
            if name == '': continue
            button = QPushButton(name)
            
            button.setStyleSheet("QPushButton {border :2px solid;background-color: #6e6b6b;color: white;"
                                "border-color: black;border-radius: 10px;}"
                                 "QPushButton::hover{background-color: #827f7f;}"
                                 "QPushButton::pressed{background-color: #827f7f;font: bold 30px;}")

            button.setFont(QFont('Times', 16))
            button.clicked.connect(self.click_key)
            button.setMinimumHeight(60)
            button.setMaximumHeight(120)

            if position == (1,0) or position == (2,0) or position == (2,12) or position == (3,0) or position == (3,12): 
                button.setMinimumWidth(120)
                layout.addWidget(button, *position, 1, 2) 
            elif position == (4,3): 
                button.setMinimumWidth(120)
                layout.addWidget(button, *position, 1, 11) 
            else:
                button.setMinimumWidth(60)
                layout.addWidget(button, *position, 1, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def click_key(self):
        text = self.sender().text()
        if text == 'Shift':
            self.click_shift(self.sender())
    
    def click_shift(self, butt_parent): 
        
        butt_parent.setStyleSheet("QPushButton {border :2px solid;background-color: #827f7f;"
                                    "color: white;border-color: black;border-radius: 10px;}")
        








if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = Window()
    myWin.show()
    sys.exit(app.exec())
