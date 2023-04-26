
# 클래스 상속 = 물려받은 기능을 유지한 채로 다른 기능을 추가할 때 사용하는 기능
# 기반 클래스 = 기능을 물려주는 클래스 = 부모 클래스, 슈퍼 클래스
# 파생 클래스 = 상속을 받아 새롭게 만드는 클래스 = 자식 클래스, 서브 클래스
 
# 클래스 상속은 클래스를 만들 때 ()를 붙이고 안에 기반 클래스 이름을 넣음
# class 기반클래스이름:
        # 코드
# class 파생클래스이름(기반클래스이름):
        # 코드

class Person():
    def greeting(self):
        print('안녕하세요.')

class Student(Person):  # Student는 기반 클래스 Person에서 파생된 클래스
    def study(self):
        print('공부하기')

james = Student()
james.greeting() # 안녕하세요: 기반 클래스 Person의 메서드 호출
james.study() # 공부하기: 파생 클래스 Student에 추가한 study 메서드


# Student 클래스에 greeting 메서드가 없지만, Person 클래스를 상속받았기 때문에 greeting 메서드를 호출할 수 있음

# 상속 관계 확인하는 방법 = issubclass 함수를 사용
# 기반 클래스의 파생 클래스가 맞으면 True, 아니면 False 반환
# 상속 관계 = is-a 관계


# super() = 상속 관계에서 부모 클래스를 호출하는 함수
# super().메서드()
# 파생 클래스에서 __init__ 메서드를 생략한 경우엔 super()를 사용하지 않아도 됨

# super(파생클래스, self).메서드
# 현재 클래스가 어떤 클래스인지 명확하게 표시하는 방법

# class Student(Person):
    # def __init__(self):
        # print('Student __init__')
        # super(Student, self).__init__() # super(파생클래스, self)로 기반 클래스의 메소드 호출
        # self.school = '파이썬 코딩 도장'


# 메서드 오버라이딩 사용하기
# 파생 클래스에서 기반 클래스의 메서드를 새로 정의하는 것 = 메서드 오버라이딩
# 오버라이딩 = 무시하다, 우선하다. 즉, 기반 클래스의 메서드를 무시하고 새로운 메서드를 만든다
# 프로그램에서 어떤 기능이 같은 메서드 이름으로 계속 사용되어야 할 때, 메서드 오버라이딩을 사용함
# 오버라이딩은 원래 기능을 유지하면서 새로운 기능을 덧붙일 때 사용함

 
# 오버라이딩 사용 예시
# class Person():
#     def greeting(self):
#         print('안녕하세요.')

# class Student(Person):
#     def greeting(self):
#         print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')

# james = Student()
# james.greeting()


# super()로 기반 클래스 호출하는 예시
# class Person():
#     def greeting(self):
#         print('안녕하세요.')

# class Student(Person):
#     def greeting(self):
#         super().greeting() # 기반 클래스의 메서드를 호출하여 중복을 줄임
#         print('저는 파이썬 코딩 도장 학생입니다.')

# james = Student()
# james.greeting()



# 다중 상속 
# 다중 상속은 여러 기반 클래스로부터 상속받아 파생 클래스를 만드는 방법

# class 기반클래스이름1:
    # 코드
# class 기반클래스이름2:
    #코드
# class 파생클래스이름(기반클래스이름1, 기반클래스이름2):


# 다이아몬드 상속

# class A:
#     def greeting(self):
#         print('안녕하세요. A입니다.')

# class B(A):
#     def greeting(self):
#         print('안녕하세요. B입니다.')

# class C(A):
#     def greeting(self):
#         print('안녕하세요. C입니다.')

# class D(B,C):
#     pass

# x = D()
# x.greeting()

# 매서드 탐색 순서 확인 => 다이아몬드 상속에 대한 해결책을 제시
# 클래스.mro()


# 추상 클래스
# 메서드의 목록만 가진 클래스, 상속받는 클래스에서 메서드 구현을 강제로 하기 위해 사용함
# from abc import *
# class 추상 클래스이름(metaclass=ABCMeta):
        # @abstractmethod
        # def 메서드이름(self):
        # 코드

# 추상 클래스는 파생 클래스가 반드시 구현해야하는 메서드를 정해줄 수 있음
# 추상 클래스의 추상 메서드를 모두 구현했는지 확인하는 시점 = 파생 클래스가 인스턴스를 만들 때.

# 추상 메서드를 빈 메서드로 만드는 이유
# 추상 클래스는 인스턴스를 만들 수 없으니 추상 메서드도 호출할 일이 없음 = 그렇기 때문에 추상 메서드를 만들 때 pass만 넣어서 빈 메서드로 만듦.
# 추상 클래스는 오로지 상속에서만 사용함, 파생 클래스에서 반드시 구현해야할 메서드를 정해줄 때 사용함.