
def add(a, b): # add 함수는 서브 루틴
    c = a + b
    print(c)
    print('add 함수')

def calc(): # calc 함수는 메인 루틴
    add(1, 2)
    print('calc 함수')

calc()

# 위 코드의 메인 루틴과 서브 루틴의 관계는 이렇다.
# 메인 루틴에서 서브 루틴을 호출 > 서브 루틴의 코드를 실행 > 메인 루틴으로 돌아옴
# 서브 루틴이 끝나면 서브 루틴의 내용은 모두 사라짐.
# 서브 루틴은 메인 루틴의 종속된 관계임.



# 코루틴 coroutine = 서로 협력하는 루틴
# 메인 루틴과 서브 루틴이 서로 대등한 관계이며 특정한 시점에 상대방의 코드를 실행함.
# 코루틴은 함수가 종료되지 않은 상태에서 메인 루트의 코드를 실행한 뒤, 코루틴의 코드를 실행함.
# 코루틴은 종료되지 않기 때문에 코루틴의 내용도 유지가 됨.
# 코루틴은 여러 번 실행할 수 있음 (코루틴은 진입점이 여러 개인 함수임)
# 진입점 = entry point, 함수의 코드를 실행하는 지점

# 코루틴에 값 보내기
# 코루틴은 yield 값을 받아올 수 있음 <> 제너레이터는 yielㅇ 값을 발생시킴.

# 코루틴객체.send(값)  # 코루틴에 값을 보내면서 코드를 실행할 때 send 메서드를 사용함.
# 변수 = (yeild) # send가 보낸 값을 받아오려면 (yield) 형식으로 변수에 저장함.
# next(코루틴객체) # 코루틴 안의 코드를 최초로 실행하여, yield 실행까지 코드를 실행함.


def number_coroutine():
    while True: # 코루틴을 계속 유지하기 위한 무한 루프 사용
        x = (yield) # 코루틴 바깥에서 값을 받아옴.
        print(x)

co = number_coroutine()

# next 함수로 코루틴의 코드를 최초로 실행
next(co) # 코루틴 안의 yield까지 코드 실행(최초 실행)

# send 메서드로 코루틴에 값을 보냄
co.send(1) # 코루틴에 숫자 1을 보냄
co.send(2) # 코루틴에 숫자 2를 보냄
co.send(3) # 코루틴에 숫자 3을 보냄


# send로 코루틴의 코드를 최초로 실행하기
# 코루틴객체.send(None) 


# 코루틴 바깥으로 값 전달하기
# 변수 = (yield)
# 변수 = next(코루틴객체)
# 변수 = 코루틴객체.send(값)

def sum_coroutine():
    total = 0
    while True:
        x = (yield total) # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        total += x

co = sum_coroutine()
print(next(co))  # 0 : 코루틴 안의 yield까지 코드를 실행하고 코루틴에서 나온 값 출력

print(co.send(1))
print(co.send(2))
print(co.send(3))

# next는 코루틴의 코드를 실행하지만 값을 보내지 않음
# send는 값을 보내면서 코루틴의 고드를 실행할 때 사용함.

# 즉, 제너레이터는 next 함수를 반복 호출하여 값을 얻어내는 방식
# 코루틴은 netx 함수를 한 번만 호출한 뒤, send로 값을 주고받는 방식

# 값을 보내지 않고 코루틴의 코드 실행 >> next 함수(__next__ 메서드)만 사용하면 됨.


# 코루틴을 종료하고 예외 처리하기
# 코루틴객체.close() # 코루틴을 강제로 종료하기

def number_coroutine():
    while True:
        x = (yield)
        print(x, end=' ')

co = number_coroutine()
next(co)

for i in range(20):
    co.send(i)

co.close()


# GeneratorExit 예외 처리하기
# 코루틴에서 close 메서드를 호출하면 코루틴이 종료할 떄, GeneratorExit 예외가 발생함

def number_coroutine():
    try:
        while True:
            x = (yield)
            print(x, end= ' ')
    except GeneratorExit: # 코루틴이 종료될 때 예외 발생함.
        print()
        print('코루틴 종료')

co = number_coroutine()
next(co)

for i in range(20):
    co.send(i)

co.close()



# 코루틴 안에 예외 발생시키기
# throw 메서드를 사용하는 데, throw 메서드에 지정한 에러메시지는 except as의 변수에 들어감
# 코루틴객체.throw(예외이름, 에러메시지)

def sum_coroutine():
    try:
        total = 0
        while True:
            x = (yield)
            total += x

    except RuntimeError as e:
        print(e)
        yield total # 코루틴 바깥으로 값 전달

co = sum_coroutine()
next(co)

for i in range(20):
    co.send(i)

print(co.throw(RuntimeError, '예외로 코루틴 끝내기'))


# 하위 코루틴의 반환값 가져오기
# 제너레이터: yield from을 사용하면 값을 바깥으로 여러 번 전달
# 코루틴: yield from에 코루틴을 지정하면 해당 코루틴에서 return으로 반환값을 가져옴
# 변수 = yield from 코루틴()

def accumlate():
    total = 0
    while True:
        x = (yield) # 코루틴 바깥에서 값을 받아옴
        if x is None: # 받아온 값이 None인 경우,
            return total  # 합계 total을 반환
        total += x


def sum_coroutine():
    while True:
        total = yield from accumlate()  # accumlate의 반환값을 가져옴
        print(total)

co = sum_coroutine()
next(co)


for i in range(1, 11):
    co.send(i) # 코루틴 accumlate에 숫자를 보냄 
co.send(None) # 코루틴 accumlate에 None을 보내서 숫자 누적을 끝냄

for i in range(1, 101):
    co.send(i)
co.send(None)


# StopIteration 예외 발생시키기
# 코루틴도 제너레이터이므로 return을 사용하면 StopIteration이 발생함. return 값은 raise StopIteration(값) 처럼 사용할 수도 있음.
# raise StopIteration(값) # vkdlTjs 3.7부터는 return 값을 사용

def accumlate():
    total = 0
    while True:
        x = (yield)
        if x is None:
            return total
        total += x

def sum_coroutine():
    while True:
        total = yield from accumlate()
        print(total)

co = sum_coroutine()
next(co)

for i in range(1, 11):
    co.send(i)
co.send(None)

for i in range(1, 101):
    co.send(i)
co.send(None)



# 코루틴의 yield from으로 값을 발생시키기
# x = (yield) >> # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
# 코루틴에서 yield에 값을 지정해서 전달했다면 yield from은 해당 값을 다시 바깥으로 전달함.

def number_coroutine():
    x = None
    while True:
        x = (yield x)
        if x == 3:
            return x


def print_coroutine():
    while True:
        x = yield from number_coroutine()
        print('print_coroutine:', x)


co = print_coroutine()
next(co)

x = co.send(1)
print(x)
x = co.send(2)
print(x)
co.send(3)