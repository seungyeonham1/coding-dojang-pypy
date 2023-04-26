
# 동물 클래스 Animal
# 날개 클래스 Wing
# 두 클래스를 상속받은 새 클래스 Bird
# '먹다', '파닥거리다', '날다', True, True 출력


class Animal():
    def eat(self):
        print('먹다')



class Wing():
    def flap(self):
        print('파닥거리다')


class Bird(Animal, Wing):
    def fly(self):
        print('날다')


b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal)) # 상속관계 확인하기 = issubclass
print(issubclass(Bird, Wing))