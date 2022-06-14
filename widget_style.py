import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        # 부모클래스 초기화자를 불러옴(반드시 필수사항임)
        self.initWindow()
        # 함수호출

    def initWindow(self):

        label_red = QLabel('빨강')
        label_blue = QLabel('파랑')

        label_red.setStyleSheet(
            # 여기다가 css넣기 / json형식으로 넣어야함

            "color:red;"
            "border-style:solid;"
            "border-width:2px;"
            "border-color:red;"
            "background-color:pink"


        )
        label_blue.setStyleSheet(
            # 여기다가 css넣기 / json형식으로 넣어야함

            "color:blue;"
            "border-style:solid;"
            "border-width:2px;"
            "border-color:blue;"
            "background-color:skyblue"

        )
        styleBox = QVBoxLayout()
        styleBox.addWidget(label_red)
        styleBox.addWidget(label_blue)
        self.setLayout(styleBox)

        self.setGeometry(100,100,300,300)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())

# 이벤트 루프를 만들어 주는 것임