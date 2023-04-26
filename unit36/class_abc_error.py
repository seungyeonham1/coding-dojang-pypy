

from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기')

james = Student() # 추상 메서드 go_to_school을 구현하지 않아 Student 인스턴스를 만들 수 없음
james.study()