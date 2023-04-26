

class Person:
    def __init__(self): # Person __init__ 메서드가 호출되지 않기 때문에 에러 발생.
        print('Person __init__')
        self.hello = '안녕하세요.'  # Person 클래스의 hello 속성

class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = '파이썬 코딩 도장' # Person 기반 클래스의 파생 클래스인 Student의 school 속성

james = Student()
print(james.school)
print(james.hello)