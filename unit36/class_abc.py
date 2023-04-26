

from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self): # 추상 메서드는 호출할 일이 없으므로 빈 메서드로 만듦
        pass 

    @abstractmethod
    def go_to_school(self): # 추상 메서드는 호출할 일이 없으므로 빈 메서드로 만듦
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기')

    def go_to_school(self):
        print('학교가기')

james = Student() # 추상 클래스의 추상 메서드를 모두 구현했는지 확인하는 시점 = 파생 클래스가 인스턴스를 만들 때
james.study()
james.go_to_school()