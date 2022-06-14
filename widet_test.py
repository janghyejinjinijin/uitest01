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

        checkBox = QCheckBox('체크박스', self)
        checkBox.toggle() # 체크된 상태로 출력
        checkBox.stateChanged.connect(self.changeText)

        self.setGeometry(100, 100, 300, 300)
        self.show()

    def changeText(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('체크박스 체크 성공!')
        else:
            self.setWindowTitle('체크박스 체크 실패!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())