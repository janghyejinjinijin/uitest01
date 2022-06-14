class TestClass:
    def sum(self, a, b):
        return a+b
    def __init__(self):
        self.age = age
        self.name = name
# 무조건 인자갑 넣어줘야됨 함수에서는

    def showName(self):
        print("이름")


# 상속
class Parent:
    def work(self):
        print("일을 하신다")

worker1 = Parent()
worker1.work()
# 일을하신다가 출력

class Child(Parent):
    def play(self):
        print("놀기")
#차일드 안에 패런츠를 넣어서 패런츠 상속

child1 = Child()
child1.play()
child1.work()
#상속을 받아서 work도 되는 것임



#초기화자

stu1 = TestClass(10, "홍길동")

stu1.name
# 홍길동

stu1.age
#10

stu1.showName()
#label1 show랑 같음