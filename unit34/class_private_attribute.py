

class Person():
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet


    def pay(self, amount):
        self.__wallet -= amount 
        print('이제 {0}원 남았네요.'.format(self.__wallet))


    # def pay(self, amount):
    #     if amount > self.__wallet:
    #         print('돈이 부족하당')
    #         return
    #     self.__wallet -= amount
              
maria = Person('마리아', 20, '서울시 반포동', 20000)
maria.pay(5000)