

class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')

class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')

class D(B,C): # 왼쪽에서 오른쪽 순서로 메서드를 찾으며, 같은 메서드가 있는 경우 왼쪽(B)가 우선임.
    pass

x = D()
x.greeting()


