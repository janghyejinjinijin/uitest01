import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):

    def __init__(self):
        super().__init__() # 부모클래스의 초기화자 호출
        self.initWindow()

    def initWindow(self):

        radio1 = QRadioButton('첫번째버튼', self)
        radio1.move(50,50)
        radio1.setChecked(True)
       
        radio2 = QRadioButton(self)
        radio2.move(50,80)
        radio1.setChecked(True)
        radio2.setText('두번째버튼')
        

        self.setGeometry(100, 100, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())