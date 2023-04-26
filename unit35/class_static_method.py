

class Calc():
    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)

Calc.add(10, 20) # 클래스에서 바로 add 메서드 호출
Calc.mul(10, 20) # 클래스에서 바로 mul 메서드 호출
