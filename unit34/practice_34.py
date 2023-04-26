
# 클래스 ? 객체를 표현하기 위한 문법
# '객체'는 특정한 개념이나 모양으로 존재하는 것을 의미함
# 객체를 만들때 사용하는 것이 '클래스'



# 게임의 캐릭터를 표현하기 

# '기사' 캐릭터는 체력, 마나, 물리공격력, 주문력이 필요함
# '기사' 캐릭터는 칼로 베기, 찌르기 등의 '스킬'이 필요함

# 체력, 마나, 물리 공격력, 주문력 = 클래스의 속성
# 베기, 찌르기 같은 스킬 기능 = 메서드


# 객체지향 프로그래밍 ?
# 복잡한 문제를 잘게 나누어 객체로 만들고, 객체를 조합해서 문제를 해결함



# 클래스와 메서드 만들기
# 클래스는 class에 이름을 지정하고 콜론(:)을 붙인 뒤, 다음 줄부터 def로 메서드를 작성함
# 클래스 이름은 대문자로 시작함
# 메서드의 첫 번째 매개변수는 반드시 self 지정할 것

# ex) class 클래스이름:
#          def 메서드(self):
#               코드


# 인스턴스 = 클래스()



# 메서드 호출하기
# 메서드는 클래스가 아닌 인스턴스를 통해 호출함.
# 인스턴스.메서드()

# 파이썬에서 흔히 볼 수 있는 클래스
# int, list, dict 등도 사실 클래스
# 파이썬에서는 자료형도 클래스 > type


# 인스턴스와 객체는 같은 것을 뜻함
# 보통 객체만 지칭할 때는 '객체'라 부르지만 클래스와 연관 지어서 말할 땐, '인스턴스'로 부름
# a = list(range(10)) # a는 list 클래스의 인스턴스, a는 객체
# b = list(range(10)) # b는 list 클래스의 인스턴스, b는 객체

# 빈 클래스를 만들 때는 코드 부분에 pass를 넣어줌

# 메서드 안에서 메서드 호출하기

class Person:
    def greeting(self):
        print('Hello')

    def hello(self):
        self.greeting()  # self.메서드() 형식으로 클래스 안의 메서드를 호출

james = Person()
james.hello()


# 특정 클래스의 인스턴스인지 확인
# isinstance 함수를 사용하여, 현재 인스턴스가 특정 클래스의 인스턴스인지 확인함. 맞으면 True, 틀리면 False를 반환
# isinstance는 주로 객체의 자료형을 판단할 때 사용함. ex) 팩토리얼 함수가 숫자가 실수, 음의 정수면 계산을 하지 않고 정수 일때만 계산하도록 만드는 예
# isinstance(인스턴스, 클래스)


# 속성 사용하기

# class 클래스 이르미
#       def __init__(self): # 속성을 만들 때, __init__ 메서드 안에서 self.속성에 값을 할당함
#           self.속성 = 값



# self = 인스턴스 자기 자신



# 인스턴스를 만들 때 값 받기
# class 클래스이름:
#       def __init__(self, 매개변수1, 매개변수2):
#             self.속성1 = 매개변수1
#             self.속성2 = 매개변수2

# 클래스 안에서 속성에 접근할 때는 'self.속성' 형식이지만 클래스 바깥에서 속성에 접근할 때는 '인스턴스.속성' 형식으로 접근


# 클래스의 위치 인수, 키워드 인수
# 클래스로 인스턴스를 만들 때 위치 인수와 키워드 인수를 사용할 수 있음
# 규칙은 위치 인수와 리스트 언패킹을 사용하려면 *args 사용해야함. 매개변수에서 값을 가져올려면 args[0]처럼 사용함

class Person():
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

maria = Person(*['마리아', 20, '서울시 반포동'])

# 키워드 인수와 딕셔너리 언패킹을 사용하려면 **kwargs 사용해야함. 매개변수에서 값을 가져올려면 kwargs['name']처럼 사용

class Person():
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']

maria1 = Person(name = '마리아', age = 20, address='서울시 반포동')
maria2 = Person(**{'name': '마리아', 'age': 20, 'address': '서울시 반포동'})


# 인스턴스를 생성한 뒤에 속성 추가하기, 특정 속성만 허용하기
# 클래스로 인스턴스를 만든 뒤에도 인스턴스.속성 = 값 형식으로 속성을 계속 추가할 수 있음

class Person:
    pass

maria = Person()
maria.name = '마리아'
print(maria.name)


# 특정 속성만 허용되고, 다른 속성은 제한하고 싶을 때
# __slots__ = ['속성이름1', '속성이름2']


class Person():
    __slots__ = ['name', 'age']

maria = Person()
maria.name = '마리아'
maria.age = 20
# maria.address = '서울시 반포동' # 허용되지 않은 속성은 추가할 때 에러가 발생함



# 비공개 속성 사용하기
# __속성과 같이 이름이 __로 시작해야함.
# 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
# 비공개 속성은 중요한 값인데 바깥에서 함부로 꺼내면 안될 때 주로 사용함
# 공개 속성 : 클래스 바깥에서 접근할 수 있는 속성을 공개 속성이라 부름
# class 클래스 이름:
#       def __init__(self, 매개변수)
#           self.__속성 = 값

class Person():
    def __init__(self, name, age, address, wallet):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
maria = Person('마리아', 20, '서울시 반포동', 20000)
# maria.__wallet -= 20000 # 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함