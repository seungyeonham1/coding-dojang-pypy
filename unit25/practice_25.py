
# 딕셔너리 키-값 쌍 추가
# setdefault: 키-값 쌍 추가
# update: 키의 값 수정, 키가 없으면 키-값 쌍 추가

# # setdefault
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x.setdefault('e')
# print(x)

# y = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# y.setdefault('f', 100)
# print(y)

# # update
# # update(키=값)

# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x.update(a=90) #a의 값을 90으로 최신화한다.
# print(x) # a는 10대신 90으로 최신화되어 출력된다

# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x.update(e=500) # e값이 없을땐, 딕셔너리에 추가된다
# print(x)

# # update 키-값 쌍 여러 개를 콤마로 구분해서 넣을때
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x.update(a=900, f=60) # a의 값을 900으로 최신화하고, f의 값은 기존 딕셔너리에 존재하지 않기 때문에 새롭게 추가한다.
# print(x)

# # update(키=값) 키가 문자열일 때만 사용할 수 있음
# y = {1: 'one', 2: 'two'}
# y.update({1: 'ONE', 3: 'THREE'})
# print(y)
# # update(키=값) 리스트와 튜플을 이용하는 방법
# y.update([[2,'Li'], [4, 'Si']]) # 리스트는 [[키1, 값1], [키2, 값2]] 형식으로 리스트를 만들고, 이 리스트를 다시 리스트 안에 넣어서 키-값 쌍을 나열해줌
# print(y)
# # update(반복가능한객체) 키-값 쌍으로 된 반복 가능한 객체로 값을 수정. 키 리스트와 값 리스트를 묶은 zip 객체로 값을 수정할 수 있음.
# y.update(zip([1, 2], ['one', 'two']))
# print(y)

# # setdefault <> update 차이
# # setdefault: 키-값 쌍 추가만 할 수 있고, 이미 들어있는 키의 값은 수정불가
# # update: 키-값 쌍 추가와 값 수정 모두 가능

# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x.setdefault('a', 90)
# print(x) # setdefault 특성상 이미 들어가있는 키의 값은 수정이 불가능하기 때문에 키 값이 변경되지 않음

# # 딕셔너리에서 키-값 쌍 삭제하기
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x.pop('a')
# print(x)

# # pop(키, 기본값) 처럼 기본값을 지정하면 딕셔너리에 키가 있을 때, 해당 키-값 쌍을 삭제한 뒤 삭제한 값을 반환
# # 키가 없을 땐, 기본값만 반환
# x.pop('z', 0)
# print(x)

# # pop대신 del로 특정 키-값을 삭제할 수 있음. []에 키를 지정하여 del을 사용해야함.
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# del x['a']
# print(x)

# # 딕셔너리에서 임의의 키-값 쌍 삭제하기
# # popitem(), 딕셔너리에서 키-값 쌍을 삭제 한뒤, 삭제한 키-값 쌍을 튜플로 반환함
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x.popitem() # 파이썬 3.6은 마지막 키-값을 삭제하지만 3.5에선 임의의 키-값을 삭제함
# print(x)

# # 딕셔너리의 모든 키-값 쌍을 삭제하기
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x.clear()
# print(x)

# # 딕셔너리에서 키의 값을 가져오기
# # get()
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# b = x.get('a')
# c = x.get('z')
# print(b)
# print(c)

# # 딕셔너리에서 키-값 쌍을 모두 가져오기
# # items: 키-값 쌍을 모두 가져옴
# # keys: 키를 모두 가져옴
# # values: 값을 모두 가져옴
# # 이 메서드들은 보통 for 반복문과 조합해서 사용함

# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# a = x.items()
# b = x.keys()
# c = x.values()
# print(a)
# print(b)
# print(c)

# # 리스트와 튜플로 딕셔너리 만들기
# # dict.fromkeys(키리스트): 키 리스트로 딕셔너리를 생성하며 값은 모두 none으로 저장
# keys = ['a', 'b', 'c', 'd']
# x = dict.fromkeys(keys)
# print(x)

# # 키리스트에 값을 지정한 경우
# y = dict.fromkeys(keys, 100)
# print(y) # 모든 키 값이 100으로 지정된다.


# # defaultdict를 사용해서 딕셔너리에 없는 키에 접근하기
# # defaultdict(기본값생성함수)

# from collections import defaultdict # 콜렉션 모듈에서 defaultdict를 가져오기
# y = defaultdict(int)
# x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
# #print(x['z'])
# print(y['z']) # int는 실수나 문자열을 정수로 변환하되, 다음과 같이 int에 아무것도 넣지 않고 호출하면 0을 반환함

# y1 = defaultdict(lambda: 'python')
# print(y1['a'])
# print(y1[0])

# 반복문으로 딕셔너리의 키-값 쌍을 모두 출력하기

# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# for i in x:
#     print(i, end = ' ') # 키만 출력됨

# 키와 값을 모두 출력하고 싶다면
# for 키, 값 in 딕셔너리.items():
#    반복할 코드

# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# for key, value in x.items(): # 딕셔너리 x에서 키와 값을 꺼내 key, value에 저장하고 꺼낼 때마다 코드를 반복함.
#     print(key, value)

# 딕셔너리를 직접 지정하고 싶은 경우
# for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items():
#     print(key, value)

# 딕셔너리의 키만 출력하기

# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# for key in x.keys():
#     print(key, end= ' ')

# 딕셔너리의 값만 출력하기

# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# for value in x.values():
#     print(value, end=' ')

# 딕셔너리 표현식 사용하기
# 딕셔너리도 리스트와 마찬가지로 if 조건문과 for 반복문을 사용하여 딕셔너리를 생성할 수 있음
# {키: 값 for 키, 값 in 딕셔너리}
# dict({키: 값 for 키, 값 in 딕셔너리})

# keys = ['a', 'b', 'c', 'd']
# x = {key: values for key, values in dict.fromkeys(keys).items()}
# # 1. items()로 딕셔너리 키-값 쌍을 구함
# # 2. 키와 값을 하나씩 꺼낸 뒤, key와 values로 딕셔너리 생성함
# print(x)

# key로 키만 가져온 뒤 특정 값을 넣거나, values로 값을 가져온 뒤 값을 키로 사용할 수 있음
x = {key: 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()} # 키만 가져옴
print(x)
y = {value: 0 for value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.values()} # 값을 키로 사용함
print(y)

# 키와 값의 자리를 바꾸는 등 여러가지로 응용이 가능
z = {value: key for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items()} # 키-값 자리를 바꿈
print(z)

# 딕셔너리 표현식에서 if 조건문 사용하기
# 딕셔너리 표현식은 딕셔너리에서 특정 값을 찾아서 삭제할 때, 유용함.

# for 반복문으로 반복하면서 del로 삭제
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# for key, value in x.items():
#     if value == 20:
#         del x[key]
# print(x) # 반복 중에 딕셔너리 크기가 바뀌었다는 에러가 발생하게 됨 
# 즉, 딕셔너리는 for 반복문으로 반복하면서 키-값 쌍을 삭제하면 안됨

# 딕셔너리 표현식에서 if 조건문을 사용하여 삭제할 값을 제외하면 됨.
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key: value for key, value in x.items() if value != 20}
# 1. 값이 20인 것을 제외한 키, 값들을 반복해서 하나씩 꺼낸다.
# 2. key, value로 딕셔너리를 생성한다
print(x)

#  {키: 값 for 키, 값 in 딕셔너리 if 조건식}
# dict({키: 값 for 키, 값 in 딕셔너리 if 조건식})

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key: value for key, value in x.items() if value != 20}
print(x)

# 딕셔너리 안에서 딕셔너리 사용하기
# 딕셔너리 = {키1: {키A, 값A}, 키2: {키B, 값B}}
# 중첩 딕셔너리는 계층형 데이터를 저장할 때 유용함

# 딕셔너리[키][키]
# 딕셔너리[키][키] = 값

terrestrial_planet = { # 딕셔너리는 terrestrial_planet, key는 머큐리, 베누스, 어쓰, 마스가 있다.
    'Mercury': { # 머큐리는 radius, mass, period 값 부분에 딕셔너리를 가지고 있음.
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}
 
print(terrestrial_planet['Venus']['mean_radius'])

# 딕셔너리의 할당과 복사

x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x # 딕셔너리가 2개일 것 같지만, 실제로는 딕셔너리가 1개다. 
y['a'] = 99
print(x)
print(x is y) # 변수 이름만 다를 뿐, 딕셔너리 x와 y는 같은 객체다. 그렇기 때문에, y값을 변경하면 x값도 같이 반영된다.

# 딕셔너리를 완전하게 2개로 만들려면 copy 메소드로 모든 키-값 쌍을 복사해야함
x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x.copy()
# y['a'] = 99

print(x)
print(y)
print(x is y) # 키-값 쌍이 다른 객체이기때문에 False
print(x == y) # 키-값 쌍은 같기때문에 True

# 중첩 딕셔너리의 할당과 복사 

x = {'a': {'python': '3.6'}, 'b': {'python': '2.7'}}
y = x.copy()
y['a']['python'] = '3.6.15'

print(x)
print(y)

# 중첩 딕셔너리를 완전히 복사하기 위해선 copy 모듈의 deepcopy 함수를 사용

x = {'a': {'python': '3.6'}, 'b': {'python': '2.7'}}
import copy
y = copy.deepcopy(x) # x의 모든 딕셔너리를 깊은 복사한다.
y['a']['python'] = '3.6.15'
print(x)
print(y)



#y3 = {'a': 10, 'b': 20, 'c': 30}

#for key in y3:
#    print(key)