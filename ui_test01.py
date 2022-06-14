# sys data 불러오기
import sys

# PyQt5 불러오기 // 큐티 위젯 불러오기
from PyQt5.QtWidgets import *

# 큐티 중에 큐어플리케이션을 설정 / 인수로 sys.argv저장함
app = QApplication(sys.argv)

# 파워포인트의 글상자같은거임 QLabel
label1 = QLabel("HelloWorld")
label1.show()
#label 이런것들이 객체다 gui 프로그램 원리가 판데기 안에 클래스를 만들어서 show를 통해 판떼기에 붙여줌


# 버튼 하나 만들 수 있음 input type='button' 이랑 같은거임
button01 = QPushButton("버튼")
button01.show()

#창이 원래 꺼지는게 정상인데 app.exec를 쓰면 무한루프로 켜짐
app.exec_()

