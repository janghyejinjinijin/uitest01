import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

# 클래스 위에 먼저 불러와야함
form_class = uic.loadUiType("ui/mywin.ui")[0]

#uic는 고치기 힘듬(잘꼬이는 아이임)
#큐메인윈도우클래스를 상속을 받았음 // 그후 초기화자를 만들었음 //super 부모클래스의 생성자를 불러올 수 있도록 하는거임
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        #super().__init__() #부모클래스의 초기화자를 호출(안하면에러)
        p = super()
        p.__init__()
        self.setupUi(self)
  #      self.setGeometry(300, 500, 500, 600) 디자인 클래스가 있기때문
        self.setWindowTitle("Hello World")
        self.setWindowIcon(QIcon("hi.png"))

#큐푸시버튼클래스 안에 btn1객체를 만듬 /  그 후 붙일 곳을 정해야되는데 그게 self임
  #      btn1 = QPushButton("버튼1", self)
   #     btn1.move(30,50)
    #    btn2 = QPushButton("버튼2", self)
     #   btn2.move(200,50)

        self.btn1.clicked.connect(self.btn1Click)
        self.btn2.clicked.connect(self.btn2Click)

    def btn1Click(self):
        self.label1.setText("버튼1이 클릭됨")
        self.lineEdit1.setText("버튼1눌렀다니 반갑습니다")
#셋텍스트로 인해 레이블이 셋텍스트안에 글씨로 변환함
        print("버튼1이 클릭됨!!!")

    def btn2Click(self):
        self.label1.setText("버튼2이 클릭됨")
        print("버튼2이 클릭됨!!!")

# Q mainWindow는 판떼기라고 생각하고 그 위에 큐위젯을 올려 만드는것임
# 맴버변수는 항상 self가 붙음 자바의 this랑 비슷하다고 보면됨
# set세터임 // setGeometry 가로,세로 초기값, 그리고 높이와 길이값을 지정해줌
# setWindowTitle 타이틀 이름 바꿀 수 있음ㅋ
# setWindowicon 아이콘 지정해놓을 수 있음 //큐아이콘은 따로 임포트해야됨
# clicked 클릭을 했을때 일하게 해주는 메써드
# connect 버튼일이 클릭됨이라고 메써드가 발생함
# 위젯을 올려야됨 새로운 버튼1이 클릭됨을 콘솔창이 아닌 새로운창에 띄우기위해

app = QApplication(sys. argv)

myWin = MyWindow()

myWin.show()

app.exec_()



#초기화자는 init로 고정되어있음 반드시 __init__로 해야됨
# app = QApplication(sys. argv) 메인함수처럼 시작점
#  이사이에 내용을 넣어줌
# app.exec_() 메인함수처럼 끝점