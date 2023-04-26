
# 기반 클래스를 초기화하지 않아도 되는 경우
# => 파생 클래스에서 __init__ 메서드를 생략한 경우

class Person():
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'

class Student(Person):
    pass

james = Student()
print(james.hello)