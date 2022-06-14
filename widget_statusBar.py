# 상태바 만들기(상태표시줄)

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

class myWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.statusBar().showMessage('하이하이')
        #메뉴바만들기
        exitWindow = QAction(QIcon('mywin.ui'), 'EXIT', self )
        exitWindow.setShortcut('CTRL+Q')
        exitWindow.setStatusTip('프로그램 종료')
        exitWindow.triggered.connect(qApp.quit) #프로그램이 꺼짐
        #q액션뒤에 아이콘을 넣음 그 뒤에 표시될 말을 씀
        #setShortcut 표시되는 단어
        #setStatusTip 툴팁하나 넣어주기
        #실제 실행되는 단어 trigger연결되는 함수 쓰기 상태바에 어떤 얘기인지 뜸

         #이걸 붙여줄 메뉴바 만들기
        menubar = self.menuBar()
        filemenu = menubar.addMenu('&파일') #&를 꼭써야됨
        filemenu.addAction(exitWindow)


        self.setGeometry(100,100,300,300)
        self.show()
    # 상태바는 메인윈도우에만 들언가겠죠?
    #상태표시줄임 statusBar
    #상태표시줄에는 버전이나 만든이이런거 쓰면 좋음.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myWindow()
    sys.exit(app.exec_())
#무한루프