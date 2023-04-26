

# super()로 기반 클래스 초기화 하기

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'  # Person 클래스의 hello 속성

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__() # 기반 클래스의 __init__  메서드 호출
        self.school = '파이썬 코딩 도장' # Person 기반 클래스의 파생 클래스인 Student의 school 속성

james = Student()
print(james.school)
print(james.hello)