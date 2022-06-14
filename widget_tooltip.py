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
        QToolTip.setFont(QFont("궁서",12))
# 툴팁 ! 마우스를 올리면 풍선도움말이 올라오는 거를 말함
# 툴팁구현하기~
# 큐폰트 안에 사이즈랑 글꼴을 넣어주면됨
        self.setToolTip("툴팁이 노출됩니다!")
# 툴팁안에 쓰고싶은말을 쓰면 된다.

        btn1 = QPushButton('버튼1', self)
        btn1.setToolTip("버튼을 클릭하면 ~합니다.") # initwindow 적용하기 버튼설명넣기

        self.setGeometry(100,100,300,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
    
# 이벤트 루프를 만들어 주는 것임