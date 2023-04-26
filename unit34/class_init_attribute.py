
class Person:
    def __init__(self, name, age, address): # __init__ 메서드는 인스턴스를 만들 때 호출되는 특별한 메서드를 의미함
                        # __ 메서드는 파이썬이 자동으로 호출해주는 메서드,  스페셜 메서드 혹은 매직 메서드로 부름
                        # __init__의 매개변수 self 들어가는 값은 Person()
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address


    def greeting(self): # greeting 메서드의 self값은 jame.greeting()을 의미함
        print('{0} 저는 {1} 입니다.'.format(self.hello, self.name))

htsl = Person('함도서관', 32, '경기도 화성시')
htsl.greeting()

print('이름:', htsl.name)
print('나이:', htsl.age)
print('주소:', htsl.address)