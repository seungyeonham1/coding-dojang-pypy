

# 데코레이터
# 메서드를 만들 때 @staticmethod, @classmethod, @abstractmethod 등을 붙인 것들이 데코레이터임.
# 함수(메서드)를 장식한다는 뜻
# 함수를 수정하지 않은 상태에서 추가 기능을 구현할 때 사용함.

# class Calc
    # @staticmethod # 데코레이터
   # def add(a, b):
        # print(a + b)


# 함수의 시작과 끝을 출력하는 데코레이터

# def trace(func): # 호출할 함수를 매개변수로 받음 (데코레이터:trace)
#     def wrapper(): # 호출할 함수를 감싸는 함수
#         print(func.__name__, '함수 시작') # __name__으로 함수 이름 출력
#         func() # 매개변수로 받은 함수를 호출
#         print(func.__name__, '함수 끝') 
#     return wrapper # wrapper 함수 반환

# def hello():
#     print('hello')

# def world():
#     print('world')

# trace_hello = trace(hello) # 데코레이터에 호출할 함수를 넣음
# trace_hello() # 반환된 함수를 호출
# trace_world = trace(world) # 데코레이터에 호출할 함수를 넣음
# trace_world() # 반환된 함수를 호출



# @으로 데코레이터 사용하기
# @ 데코레이터
# def 함수이름():
        # 코드

def trace(func):
    def wrapper():
        print(func.__name__, '함수 시작')
        func() # 매개변수로 받은 함수를 호출 hello(), world()
        print(func.__name__, '함수 끝')
    return wrapper

@trace # 데코레이터
def hello(): # func()
    print('안녕하세요')

@trace # 데코레이터
def world(): # func()
    print('세계')

hello() # 함수를 그대로 호출
world() # 함수를 그대로 호출


# 데코레이터 여러 개 지정
# @데코레이터1
# @데코레이터2 # 데코레이터가 실행되는 순은 위에서 아래로 실행
# def 함수이름():
    # 코드

def decorator1(func):
    def wrapper():
        print('데코레이터')
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print('데코레이터2')
        func()
    return wrapper

@decorator1  
@decorator2 

# @를 사용하지 않을 때
# decorated_hello = decorator1(decorator2(hello))
# decorated_hello()

def hello():
    print('hello')

hello()


# 매개변수와 반환값을 처리하는 데코레이터 만들기

def trace(func): # 호출할 함수를 매개변수로 받음
    def wrapper(a, b):  # 호출할 함수 add(a, b)의 매개변수와 똑같이 지정
        r = func(a, b) # func에 매개변수 a, b를 넣어서 호출하고 반환값을 변수(r)에 저장
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r)) # 매개변수와 반환값 출력

        return r # func 반환값을 반환
    return wrapper # wrapper 함수 반환

@trace # 데코레이터
def add(a, b): # 매개변수 2개 
    return a + b # 매개변수 2개를 더한 값을 반환

print(add(10, 20))


# 가변 인수 함수 데코레이터
# 매개변수(인수)가 고정되지 않은 함수는 wrapper 함수로 가변 인수 함수로 만듦

def trace(func): # 호출할 함수를 매개변수로 받음
    def wrapper(*args, **kwargs): # 가변 인수 함수로 만듦
        r = func(*args, **kwargs) # funcs에 args, kwargs를 언패킹하여 넣어줌
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(func.__name__, args, kwargs, r)) #매개변수와 반환값 출력

        return r # func의 반환값을 반환
    return wrapper # wrapper 함수 반환

@trace
def get_max(*args): # 위치 인수를 사용하는 가변 인수 함수
    return max(args)

@trace
def get_min(**kwargs): # 키워드 인수를 사용하는 가변 인수 함수
    return min(kwargs.values())

print(get_max(10, 20))
print(get_min(x=10, y=20, z=30))



# 메서드에 데코레이터 사용
# 클래스를 만들면서 데코레이터 사용 시, self를 주의해야함
# 인스턴스 메서드는 항상 self를 받으므로 데코레이터를 만들 때도 wrapper 함수의 첫 번째 매개변수는 self로 지정해야 함.
# func를 호출할 때도 self와 매개변수를 그대로 넣어야함.

def trace(func):
    def wrapper(self, a, b): # 호출할 함수가 인스턴스 메서드이므로, 첫 번째 매개변수는 self로 지정

        r = func(self, a, b) # self와 매개변수를 그대로 넣어줌
        print('{0}(a ={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))

        return r # func의 반환값을 반환
    return wrapper

class Calc:
    @trace
    def add(self, a , b): # add는 인스턴스 메서드
        return a + b
    
c = Calc()
print(c.add(10, 20))


# 매개변수가 있는 데코레이터 만들기

def is_multiple(x): # 데코레이터가 사용할 매개변수를 지정
    def real_decorator(func): #호출할 함수를 매개변수로 받음
        def wrapper(a, b): # 호출할 함수의 매개변수와 똑같이 지정
            r = func(a, b) # func를 호출하고 반환값을 변수에 저장
            if r % x == 0: # func의 반환값이 x의 배수인지 확인
                print('{0}의 반환 값은 {1}의 배수 입니다.'.format(func.__name__, x))
            else:
                print('{0}의 반환 값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r # func의 반환값을 반환
        return wrapper # wrapper 함수 반환
    return real_decorator # real_decorator 함수 반환

# @is_multiplex(3) # 데코레이터 인수
# def add(a, b):
#     return a + b

# 데코레이터 사용
# @데코레이터(인수)
# def 함수이름():
        # 코드

# print(add(10, 20))
# print(add(2, 5))




# 매개변수가 있는 데코레이터 여러 개 지정하기

# @데코레이터1(인수)
# @데코레이터2(인수)
# def 함수이름():
        # 코드

@is_multiple(3) # 데코레이터 인수 
@is_multiple(7)

# @를 사용하지 않았을 때
# decorated_add = is_multiple(3)(is_multiple(7)(add))
# decorated_add(10, 20)

def add(a, b):
    return a + b

print(add(10, 20))





# 원래 함수 이름이 안 나오는 경우엔?
# 데코레이터를 여러 개 사용하면 데코레이터에서 반환된 wrapper 함수가 다른 데코레이터로 들어감.
# 함수의 원래 이름을 출력하고 싶다면 functools 모듈의 wraps 데코레이터를 사용해야 함.
# @funcstools.wraps는 원래 함수의 정보를 유지시킴. 따라서, 디버깅을 할 때 유용하므로 데코레이터를 만들 때 사용하는 게 좋음.


import functools

def is_multiple(x): # 데코레이터가 사용할 매개변수를 지정
    def real_decorator(func): #호출할 함수를 매개변수로 받음
        @functools.wraps(func) # funcstool.wraps에 funcs를 넣은 뒤 wrapper 함수 위에 지정
        def wrapper(a, b): # 호출할 함수의 매개변수와 똑같이 지정
            r = func(a, b) # func를 호출하고 반환값을 변수에 저장
            if r % x == 0: # func의 반환값이 x의 배수인지 확인
                print('{0}의 반환 값은 {1}의 배수 입니다.'.format(func.__name__, x))
            else:
                print('{0}의 반환 값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r # func의 반환값을 반환
        return wrapper # wrapper 함수 반환
    return real_decorator # real_decorator 함수 반환

@is_multiple(3) # 데코레이터 인수 
@is_multiple(7)

def add(a, b):
    return a + b

print(add(10, 20))



# 클래스로 데코레이터 만들기
# 인스턴스를 함수처럼 호출하게 해주는 __call__메서드를 구현해야함

class Trace:
    def __init__(self, func): # 호출할 함수를 초깃값으로 지정
        self.func = func # 호출할 함수를 속성 funcs에 저장

    def __call__(self):
        print(self.func.__name__, '함수 시작')
        self.func()
        print(self.func.__name__, '함수 종료')

@Trace
def hello():
    print('hello')

hello()

# 클래스로 만든 데코레이터는 @를 지정하지 않고 데코레이터의 반환값을 호출하는 방식으로도 사용 가능함.
# def hello():
    # print('hello')

# trace_hello = Trace(hello) # 데코레이터에 호출할 함술르 넣어서 인스턴스 생성
# trace_hello() #인스턴스를 호출. __call__메서드가 호출됨



# 클래스로 매개변수와 반환값을 처리하는 데코레이터 만들기

class Trace:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):  # 호출할 함수의 매개변수를 처리
    # 가변 인수를 사용하지 않고, 고정된 매개변수를 사용할 때 def __call__(self, a, b):  처럼 만들어도 됨.
        r = self.func(*args, **kwargs)

        print('{0}(args={1}, kwargs={2}) -> {3}'.format(self.func.__name__, args, kwargs, r))

        return r
    
@Trace
def add(a, b):
    return a + b 

print(add(10, 20))
print(add(a=10, b=20))



# 클래스로 매개변수가 있는 데코레이터 만들기

class IsMultiple:
    def __init__(self, x): # 데코레이터가 사용할 매개변수를 초깃값으로 받음
        self.x = x
    
    def __call__(self, func): # 호출할 함수를 매개변수로 받음
        def wrapper(a, b): # 호출할 함수의 매개변수와 똑같이 지정 
                           # (가변 인수로 작성해도 됨)
            r = func(a, b)
            if r % self.x == 0: # func의 반환값이 self.x의 배수인지 확인
                print('{0}의 반환값은 {1}의 배수 입니다.'.format(func.__name__, self.x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, self.x))
            return r
        return wrapper
    

@IsMultiple(3) # 데코레이터(인수)
def add(a, b):
    return a + b

print(add(10, 20))
print(add(2, 5))