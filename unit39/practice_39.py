
# 이터레이터 = 값을 차례대로 꺼낼 수 있는 객체, '반복자'로 불림

# for i in range(100) >> 사실 0~99까지 값을 차례대로 꺼낼 수 있는 이터레이터를 하나만 만들어냄
# 숫자가 많을 때는 메모리를 많이 사용하게 됨
# 그렇기 때문에, 파이썬에서는 이터레이터만 생성하고 값이 필요한 시점이 되었을 때 값을 만드는 방식을 사용.
# 즉, 데이터 생성을 뒤로 미루는 것 = '지연 평가' 방식

# 반복 가능한 객체(이터레이블) = 문자열, 리스트, 딕셔너리, 세트 = 요소가 여러 개 들어있고, 한 번에 하나씩 꺼낼 수 있는 객체
# 반복 가능한 객체 알아 보는 방법: 객체에 __iter__ 메서드가 있는지 확인, 'dir' 함수를 사용하면 객체의 메서드를 확인할 수 있음

# print(dir([1, 2, 3]))

# a = [1, 2, 3].__iter__()
# print(a)

# # __next__ 메서드를 호출하면 요소를 차례대로 꺼낼 수 있음.

# it = [1, 2, 3].__iter__()
# print(it.__next__()) # 1
# print(it.__next__()) # 2
# print(it.__next__()) # 3
# # print(it.__next__()) # 이터레이터는 __next__요소로 계속 꺼내다가, 꺼낼 요소가 없으면 StopIteration 예외를 발생시켜 반복을 끝냄.


# print('Hello, world'.__iter__())
# print({'a' : 1, 'b': 2}.__iter__())
# print({1, 2, 3}.__iter__())

# it1 = range(3).__iter__()
# print(it1.__next__()) # 0 
# print(it1.__next__()) # 1
# print(it1.__next__()) # 2
# print(it1.__next__()) # 동일하게 꺼낼 요소가 없기 때문에, StopIteration 예외를 발생시켜 반복을 멈춤

# 반복 가능한 객체 과정
# 1. 반복 가능한 객체는 __iter__() 메서드를 통해 이터레이터를 얻는다.
# 2. 이터레이터의 __next__메서드로 요소를 꺼내는 것을 반복한다. (클래스에 __iter__와 __next__  메서드를 모두 구현하면 이터레이터를 만들 수 있음)
# __iter__, __next__ 메서드를 가진 객체를 이터레이터 프로토콜을 지원한다라고 말함.
# 3. 꺼낼 요소가 더이상 없으면 StopIteration 예외를 발생시켜 반복을 끝낸다.

# 이터레이블 =  요소를 한 번에 하나씩 가져올 수 있는 객체
# 이터레이터 = __next__ 메서드를 사용하여 차례대로 값을 꺼낼 수 있는 객체


# 리스트, 튜플, 문자열, range = 반복 가능한 객체이면서 시퀀스 객체
# 세트, 딕셔너리 = 반복 가능한 객체이지만, 시퀀스 객체는 아님

# 반복 가능한 객체 = 요소의 순서와 상관없이 요소를 한 번에 하나씩 꺼낼 수 있음.
# 시퀀스 객체란? 요소의 순서가 정해져 있고 연속적으로 이어져있어야함. <-> 세트, 딕셔너리는 요소(키)의 순서가 정해져 있지 않기 때문에 시퀀스 객체가 아님
# 시퀀스 객체가 반복 가능한 객체보다 좁은 개념


# 이터레이터 만들기
# class 이터레이터이름:
        # def __iter__(self):
                # 코드
        # def __next__(self):
                # 코드


# 이터레이터 언패킹
# 자주 사용하는 map도 이터레이터 => a, b, c = map(int,input().split())처럼 언패킹으로 변 수 여러 개에 값을 할당할 수 있음

# 반환값을 _에 저장하는 이유
# _, b = range(2) = a, b = range(2)와 같음.
# 반환값을 언패킹했을 때 _에 할당하는 것은 특정 순서의 반환값 사용하지 않고 무시하겠다라는 관례적 표현.

# a, _, c, d = range(4)  # 즉, 이 코드는 언패킹했을 때 두 번째 변수는 사용하지 않겠다라는 뜻.
# a, c, d


# 인덱스로 접근할 수 있는 이터레이터
# __getitem__ 메서드로 인덱스로 접근할 수 있는 이터레이터를 만듦.
# class 이터레이터이름:
        # def __getitem__(self, 인덱스):
                # 코드

# class Counter:
#     def __init__(self, stop):
#         self.stop = stop # 반복을 끝낼 숫자

# # 클래스에서 __getitem__만 구현해도 이터레이터가 됨 (__iter__, __next__ 생략 가능)
#     def __getitem__(self, index): # 인덱스를 받음
#         if index < self.stop: # 인덱스가 반복을 끝낼 숫자보다 작은 경우
#             return index # 인덱스를 반환
#         else: # 인덱스가 반복을 끝낼 숫자보다 크거나 같은 경우
#             raise IndexError # 예외를 발생하여 반복을 끝냄
        
# print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

# for i in Counter(3):
#     print(i, end=' ')


# iter, next 함수 활용

# iter: 반복을 끝낼 값을 지정하면, 특정 값이 나올 때 반복을 끝냄
# iter는 반복 가능한 객체 대신 호출 가능한 객체(callable)을 넣어줌.
# 반복을 끝낼 값은 sentinel (감시병)이라 부름 == 반복을 감시하다가 특정 값이 나오면 반복을 끝냄.
# iter(호출가능한 객체, 반복을 끝낼 값)
# iter 함수를 활용하면 if 조건문을 통해 매번 검사하지 않아도 되며, 코드가 간단해짐.




# import random

# it = iter(lambda : random.randint(0,5), 2)
# print(next(it)) # 숫자 2가 나오면 StopIteration이 발생하며 반복이 끝남
# print(next(it) )# 숫자 2가 나오면 StopIteration이 발생하며 반복이 끝남
# print(next(it)) # 숫자 2가 나오면 StopIteration이 발생하며 반복이 끝남
# print(next(it)) # 숫자 2가 나오면 StopIteration이 발생하며 반복이 끝남

# import random

# for i in iter(lambda : random.randint(0, 5), 2):
#     print (i, end = ' ')

# import random

# while True:
#     i = random.randint(0, 5)
#     if i == 2:
#         break
#     print(i, end = ' ')


# next는 기본값을 지정할 수 있음.
# 기본값을 지정하면 반복이 끝나더라도 StopIteration이 발생하지 않고, 기본값을 출력함.
# 반복할 수 있을 땐 해당 값을 출력하고, 반복이 끝났을 땐 기본값을 출력함.
# next(반복가능한객체, 기본값)

it = iter(range(3))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))