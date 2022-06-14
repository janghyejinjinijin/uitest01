# 위젯 툴바 만들기
import sys

from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

class myWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 상태표시줄에 날짜찍기
        self.date = QDate.currentDate()
        self.initWindow()

    def initWindow(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))#그냥찍으면 에러뜸

        menu1 = QAction(QIcon('1.png'), 'EXIT', self )
        menu1.setShortcut('CTRL+P')
      #  menu1.setStatusTip('프로그램 출력')
        menu1.triggered.connect(qApp.quit) #프로그램이 꺼짐

        menu2 = QAction(QIcon('2.png'), 'print', self )
        menu2.setShortcut('CTRL+Q')
      #  menu2.setStatusTip('프로그램 종료')
        menu2.triggered.connect(qApp.quit) #프로그램이 꺼짐

        menu3 = QAction(QIcon('3.png'), 'save', self )
        menu3.setShortcut('CTRL+S')
    #    menu3.setStatusTip('프로그램 저장')
        menu3.triggered.connect(qApp.quit) #프로그램이 꺼짐

        menu4 = QAction(QIcon('4.png'), 'EDIT', self )
        menu4.setShortcut('CTRL+E')
  #      menu4.setStatusTip('프로그램 수정')
        menu4.triggered.connect(qApp.quit) #프로그램이 꺼짐

        toolbar = self.addToolBar('toolbar') #여기다가 메뉴1을 붙이겠다 대신 이 툴바이름을 넣어줘야함
        toolbar.addAction(menu1)
        toolbar.addAction(menu2)
        toolbar.addAction(menu3)
        toolbar.addAction(menu4)






        self.setGeometry(100,100,300,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myWindow()
    sys.exit(app.exec_())
#무한루프