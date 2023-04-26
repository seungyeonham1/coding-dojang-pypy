
# 람다 표현식
# 식 형태로 되어 있음
# 함수를 간편하게 작성할 수 있음
# 다른 함수의 인수로 넣을 때 주로 사용함
# 람다 표현식은 이름이 없는 함수를 만들기 때문에 '익명 함수'로 불리기도 함
# 람다 표현식 안에서는 변수를 만들 수 없음 (변수가 필요한 경우, def로 함수를 작성하는 게 좋음)
# 람다 표현식 안에서 조건부 표현식 if, else을 사용할 땐 콜론(:)을 붙이지 않음
# map, filter, reduce 사용



# 람다 표현식으로 함수 만들기
# plus_ten 함수를 람다 표현식으로 작성

# def plus_ten(x):
#     return x + 10

# plus_ten(1)

# 람다 표현식
# lambda 매개변수들: 식
# lambda x: x + 10

# lambda로 만든 익명 함수를 호출할려면 람다 표현식을 변수에 할당해주면 됨

# plus_ten = lambda x: x + 10
# plus_ten(1)


# 람다 표현식 자체를 호출하기 (변수에 할당하지 않고 람다 표현식 자체를 바로 호출)
# (lambda 매개변수들:식)(인수들)

# (lambda x: x + 10)(1)


# 람다 표현식 안에서는 변수를 만들 수 없음

# (lambda x: y = 10; x + y)(1)  => 문맥에러발생

# 람다 표현식 바깥에 있는 변수는 사용할 수 있음.
# y = 10
# (lambda x: x + y)(1)

# 람다 표현식을 인수로 사용하기
# 함수의 인수 부분에서 간단하게 함수를 만들기 위함
# 대표적인 예 : map

# def plus_ten(x):
#     return x + 10

# list(map(plus_ten, [1, 2, 3]))

# 람다 표현식 
# list(map(lambda x: x + 10, [1, 2, 3]))

# 람다 표현식으로 매개변수 없는 함수 만들기

# (lambda : 1)()

# x = 10
# (lambda : x)()

# 람다 표현식과 map, filter, reduce 함수 활용

# 람다 표현식의 조건부 표현식
# (lambda 매개변수들: 식1 if 조건식 else 식2)

# map을 활용한 리스트 a에서의 3의 배수를 문자열로 변환한 예
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x % 3 == 0 else x, a))

# 람다 표현식 안에서 조건부 표현식 if, else을 사용할 땐 콜론(:)을 붙이지 않음
# 람다 표현식 안에서는 elif를 사용할 수 없음 (반드시 else를 사용해야함)
# 조건부 표현식: 식1 if 조건식1 else 식2 if 조건식2 else 식3
# labmda 매개변수들: 식1 if 조건식1 else 식2 if 조건식2 else 식3

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))

# def 함수로 가독성 높이기

def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10
    
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(f, a))

# map에 객체 여러 개 넣기
# map은 리스트 등 반복 가능한 객체를 여러개 넣을 수도 있음.

a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]

list(map(lambda x, y: x * y, a, b))

# filter 사용하기
# filter는 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져옴. 단, filter에서 지정한 함수 반환값이 True인 경우만 해당됨
# 함수 반환값이 False인 경우는 버림
# filter(함수, 반복가능한객체)

def f(x):
    return x > 5 and x < 10

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list(filter(f, a))

list(filter(lambda x: x > 5 and x < 10, a)) # 람다 표현식을 이용한 filter


# reduce 사용하기
# reduce는 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤, 이전 결과와 누적해서 반환하는 함수

# from functools import reduce
# reduce(함수, 반복가능한객체)

def f(x, y):
    return x + y

a = [1, 2, 3, 4, 5]
from functools import reduce
reduce(f, a)

reduce(lambda x, y: x + y, a) # 람다 표현식을 이용한 reduce



# map, filter, reduce 리스트 표현식
# 람다 표현식보다 리스트 표현식이 좀 더 알아보기 쉽고 속도가 빠름

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
[i for i in a if i > 5 and i < 10]



# reduce 람다 표현식을 for 반복문으로 표현
# reduce(lambda x, y: x + y, x a)

a = [1, 2, 3, 4, 5]
x = a[0]

for i in range(len(a) - 1):
    x = x +a[i + 1]