# 자동차로 예를 들면
# 색상, 현재 속도, 모델 등...
car1_color = 'Red'
car1_speed = 100
car1_model = '테슬라'

car2_color = 'Blue'
car2_speed = 70
car2_model = 'BMW'


# 리스트나 딕셔너리에 담아서 하나의 변수로 표현할 수도 있지만
# '자동차' 만을 위한 정보 단위는 아니다.

# 속성(Attributes) : color, speed, model 등 객체를 표현하기 위한 값들
# 구조체(Struct) : 새로운 정보단위를 생성하고 속성만 나열한 것
# 클래스(Class) : 속성 + 메소드(함수)
#               메소드가 하는 주요 역할은 속성값을 변경하는 것
class Car:
    color = 'Blue'
    speed = 100
    model = 'BMW'

    def speedUp(self):
        self.speed += 10


# mycar는 클래스 Car형의 데이터
# => mycar는 Car 클래스의 인스턴스(Instance)다.
mycar = Car()
print(f'mycar : {mycar.color}, {mycar.speed}, {mycar.model}')

mycar2 = Car()
mycar2.color = 'Red'
mycar2.speed = 200
mycar2.model = '아우디'
print(f'mycar2 : {mycar2.color}, {mycar2.speed}, {mycar2.model}')


# self : 클래스 자기자신
#        메소드에는 self가 반드시 첫번째 파라미터로 포함되어야 합니다.
#        메소드를 호출할 때에는 self를 (여러분들이) 신경쓰지 않습니다.
#        왜냐면, 자동으로 전달되기 때문

# 클래스가 가져야 할 특징
# 은닉성 : 외부에서 클래스의 속성을 마음대로 편집하게 하면 안된다.

class Car2:
    # 생성자(Constructor) : 인스턴스가 만들어질 때 반드시 실행되는 함수
    def __init__(self, color, speed, model):
        self.color = color
        self.__speed = speed
        self.model = model

    def __del__(self):
        print(f'{self.model}가 폐차되었습니다.')

    def __add__(self, other):
        print(f'{self.model}과 {other.model}이 충돌했습니다.')
        return '망함'

    def speedUp(self):
        self.__speed += 10

    def setSpeed(self, new_speed):  # setter : 외부에서 속성을 변경할 수 있게 해주는 함수
        self.__speed = new_speed

    def getSpeed(self): # getter : 외부에서 속성 값을 확인할 수 있게 해주는 함수
        return self.__speed


mycar3 = Car2('Blue',200,'포르쉐')
mycar3.speedUp()
mycar4 = Car2('Yellow',900,'모닝')

# mycar4.__speed += 50
mycar4.setSpeed(950)

# print(f'mycar3 : {mycar3.color}, {mycar3.speed}, {mycar3.model}')
# print(f'mycar4 : {mycar4.color}, {mycar4.speed}, {mycar4.model}')
print(f'mycar3 : {mycar3.color}, {mycar3.getSpeed()}, {mycar3.model}')
print(f'mycar4 : {mycar4.color}, {mycar4.getSpeed()}, {mycar4.model}')

result = mycar3 + mycar4
print(result)

del(mycar3)
del(mycar4)


