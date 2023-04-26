
# 제너레이터 = 이터레이터를 생성해주는 함수, '발생자'라 부름
# 함수 안에서 yield 라는 키워드만 사용하면 됨.
# yield 값

def number_generator():
    yield 0
    yield 1
    yield 2

for i in number_generator():
    print(i)



# 제너레이터는 이터레이터와 동작이 같음
# 제너레이터의 객체 메서드를 살펴보면 

g = number_generator()
print(dir(g)) # __iter__, __next__ 메서드가 들어 있음 

# 제너레이터는 yield에 지정한 값이 __next__ 메서드(next 함수)의 반환값으로 나옴. <> 이터레이터는 __next__ 메서드 안에서 직접 return으로 값을 반환
# 제너레이터는 함수의 끝까지 도달하면 StopIteration 예외가 자동으로 발생 <> 이터레이터는 raise로 직접 StopIteration을 발생시킴
# return도 함수를 끝내므로 return을 사용해서 중간에 빠져나오면 StopIteration 예외가 발생함.
# 제너레이터 안에서 return에 반환값을 지정하면 StopIteration 예외의 에러 메세지로 들어감.


# for와 제너레이터
# for문 반복 > __next__ 호출 > yield에서 발생시킨 값을 가져옴 > StopIteration 발생하면 반복을 끝냄

# yield 생산하다, 양보하다 >> yield를 사용하면 값을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보함.
# 즉, yield는 현재 함수를 잠시 중단하고 함수 바깥의 코드가 실행되도록 만듦.

# yield 동작 과정
# 변수 = next(제너레이터객체)

# return은 반환 즉시 함수가 끝나지만, yield는 잠시 함수 바깥의 코드가 실행되도록 양보하여 값을 가져가게 한 뒤, 다시 제너레이터 안의 코드를 계속 실행하는 방식
 


# 제너레이터 만들기 
# range(횟수)처럼 동작하는 제너레이터

def number_generator(stop):
    n = 0 # 숫자 0부터 시작
    while n < stop:
        yield n # 현재 숫자를 바깥으로 전달
        n += 1

for i in number_generator(3):
    print(i)


# yield 에서 함수 호출

def upper_generator(x):
    for i in x:
        yield i.upper() # 함수의 반환값을 바깥으로 전달

fruits = ['apple', 'pear', 'orange', 'grape', 'pineapple']

for i in upper_generator(fruits):
    print(i)


# yield from으로 값을 여러 번 바깥으로 전달하기
# 여러 번 바깥으로 전달할 때는 for, while 반복문으로 반복하면서 yield를 사용함

def number_generator():
    x = [1, 2, 3]
    for i in x:
        yield i

for i in number_generator():
    print(i)

# yield from 반복가능한객체
# yield from 이터레이터
# yield from 제너레이터객체

def number_generator():
    x = [1, 2, 3]
    yield from x # 리스트에 있는 요소를 한 개씩 바깥으로 전달 

for i in number_generator():
    print(i)



# yield form에 제너레이터 객체 지정하기

def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1

def three_generator():
    yield from number_generator(3) # 숫자를 세 번 바깥으로 전달

for i in three_generator(): # 숫자 세 번을 출력
    print(i)


# 제너레이터 표현식
# 리스트 표현식을 괄호()로 묶으면 제너레이터 표현식이 됨
# (식 for 변수 in 반복가능한객체)

print([i for i in range(10) if i % 2 == 0]) # 리스트 표현식
print((i for i in range(10) if i % 2 == 0)) # 제너레이터 표현식

# 리스트 표현식은 처음부터 리스트 요소를 만들어내지만, 제너레이터는 필요할 때 요소를 만들어내므로 메모리 절약이 가능함.