
# 클로저 사용하기

# 변수의 사용 범위 

# x = 10

# def foo(): # 전역 변수
#     print(x) # 전역 변수 출력

# foo() 
# print(x) # 전역 변수 출력


# def foo():
#     x = 10 # foo의 지역변수
#     print(x) # foo의 지역 변수 출력

# foo() 
# print(x) # foo의 지역변수는 출력할 수 없음

# # 지역 변수는 변수를 만든 함수안에서만 접근할 수 있고, 함수 바깥에서는 접근할 수 없음



# 함수 안에서 전역 변수 변경하기
# global 키워드 사용  >> global 전역변수

# x = 10
# def foo():
#     global x # 전역 변수 x를 사용하겠다고 설정
#     x = 20
#     print(x) # foo의 지역 변수 출력 = 20

# foo()
# print(x) # 전역 변수 출력 = 10  ==> foo 함수 내 global 키워드로 전역 변수를 설정한 경우에는 20으로 출력


# 네임스페이스
# 파이썬에서 변수는 네임스페이스에 저장됨

# 함수 내에서 locals 사용

# def fooo():
#     x = 10
#     print(locals()) # 지역 범위 내에서 네임스페이스 출력하기 때문에, 지역 네임스페이스를 가져옴

# fooo()


# 함수 안에서 함수 만들기

# def 함수이름1():
#     코드
#     def 함수이름2():
#         코드


# def print_hello():
#     hello = 'Hello, java!' # 전역 변수
#     def print_message():
#         print(hello)
#     print_message()
    
# print_hello()


# 지역 변수의 범위
# 바깥쪽 함수의 지역 변수는 그 안에 속한 모든 함수에서 접근할 수 있음



# 지역 변수 변경
# 지역 변수의 값을 변경 
# nonlocal 지역변수

# def A():
#     x = 10 # A의 지역 변수 x
#     def B():
#         x = 20 # B의 지역 변수 x를 새로 만듦

#     B()
#     print(x) # A의 지역 변수 x 출력

# A()

# def A():
#     x = 10 # A의 지역 변수 x
#     def B():
#         nonlocal x # 현재 함수의 바깥쪽에 있는 지역 변수 사용
#         x = 20 # A의 지역 변수 x에 20을 할당

#     B()
#     print(x) # A의 지역 변수 x 출력

# A()

# nonlocal이 변수를 찾는 순서
# 현재 함수의 바깥쪽에 있는 지역 변수를 찾을 때, 가장 가까운 함수부터 먼저 찾음
# 지역 변수가 없다면, 계속 바깥쪽으로 나가서 찾음

def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()
A()



# global로 전역 변수 사용하기
# 함수에서 값을 주고받을 때는 매개변수와 반환값을 사용하는 게 좋음

x = 1
def A():
    x = 10
    def B():
        x = 20
        def C():
            global x # 전역 변수 x를 사용하겠다 선언 x = 1
            x = x + 30
            print(x)
        C()
    B()
A()


# 클로저 사용하기
# 클로저란? 함수를 둘러싼 환경(지역 변수, 코드)을 계속 유지하다가, 함수를 호출할 때 다시 꺼내서 사용하는 함수
# 클로저를 사용하면 프로그램의 흐름을 변수에 저장할 수 있음
# 클로저는 지역 변수와 코드를 묶어서 사용하고 싶을 때 활용
# 클로저에 속한 지역 변수는 바깥에서 직접 접근할 수 없으므로 데이터를 숨기고 싶을 때 활용

def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    return mul_add 

c = calc() # c에 저장된 함수가 클로저
print(c(1), c(2), c(3), c(4))



# lambda로 클로저 만들기

def calc():
    a = 3
    b = 5
    return lambda x: a * x + b

c = calc()
print(c(1), c(2), c(3), c(4), c(5))


# 클로저의 지역 변수 변경하기
# 클로저의 지역 변수를 변경하고 싶다면 nonlocal 사용

def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add
c = calc()
c(1)
c(2)
c(3)



# 일급 객체란 ? 
# 변수나 데이터 구조에 넣을 수 있어야 함
# 매개변수에 전달할 수 있어야 함
# 반환값으로 사용할 수 있어야 함
# 위 3가지 조건을 만족하는 객체를 일급 객체라 부른다.

# 파이썬 함수는 일급 함수임
# def 안에서 def로 함수를 만들거나,  lambda를 사용해 실행 중에 함수를 생성할 수 있기 때문임


# 파이썬에선 switch 문을 사용할 수 없으나, 람다 표현식과 딕셔너리를 사용하면 switch 처럼 사용 가능함

switch = {
    '+': lambda x, y : x + y,
    '*': lambda x, y: x * y}

x = '+'
try:
    print(switch[x](10, 20)) # 딕셔너리에 키를 지정하는 방식
except KeyError:
    print ('default') # 딕셔너리에 키가 없을 때는 기본값