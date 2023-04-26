
# 세트는 중괄호 {} 안에 값을 저장하며, 값은 콤마(,)로 구분해준다.

# 세트 = {값1, 값2, 값3}

# 세트는 요소의 순서가 정해져 있지 않음. 또한, 요소는 중복될 수 없으며 똑같은 요소를 넣어도 1개만 출력됨

# 세트는 리스트, 딕셔너리와 달리 세트안에 세트를 넣을 수 없음

fruits = {'orange', 'orange', 'banana', 'apple'}
print(fruits)

# 세트는 리스트, 튜플, 딕셔너리와 달리 대괄호([])로 특정 요소만 출력할 수 없음

# 세트에 특정값 확인하기
# in 연산자 활용

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
a = 'orange' in fruits
b = 'peach' in fruits
print(a) # 오렌지가 세트에 있으니 True
print(b) # 복숭아가 세트에 없으니 False

# 세트에 특정갑 없는지 확인
# not in 연산자 활용
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
a = 'orange' not in fruits
b = 'peach' not in fruits
print(a) # 오렌지가 세트에 있으니 False
print(b) # 복숭아가 세트에 없으니 True

# set를 사용하여 세트 만들기
# set(반복가능한객체)  # set에 반복가능한 이터레이블(객체)를 넣는다.

# 영문 문자열 세트
a = set('apple')
print(a)

# 숫자 세트
b = set(range(5))
print(b)

# 빈 세트
c = set()
print(c)

# 세트가 중괄호({ })를 사용한다고 해서 만드는 경우
d = {}
print(d)
print(type(d)) # 자료형의 종류는 딕셔너리임을 알 수 있음

# 프로즌 세트
# 프로즌 세트 = frozenset(반복가능한객체)
# 즉, 얼어있는 세트.
# 프로즌 세트는 뒤에서 설명할 집합 연산과 메서드에서 요소를 추가하거나 삭제하는 연산 메서드를 사용할 수 없음
# 프로즌세트는 세트 안에 세트를 넣고 싶을 때 사용함.
# 프로즌세트는 프로즌세트를 중첩해서 넣을 수 있음. 단, frozenset만 넣을 수 있고, 일반 set는 넣을 수 없음
# ex) frozenset({frozenset({1, 2}), frozenset({3, 4})}) 





# 집합 연산
# 집합 연산은 파이썬의 산술 연산자와 논리 연산자를 활용함


# | 연산자는 Union(합집합)을 구하며, OR 연산자 '|' 를 사용함. set.union 메서드와 동작이 같음
# 세트1 | 세트2
# set.union(세트1, 세트2)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = set.union(a, b)
print(a|b)
print(c)


# & d연산자는 intersection(교집합)을 구하며, AND 연산자 '&' 를 사용함. set.intersection 메서드와 동작이 같음
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = set.intersection(a, b)
print(a & b)
print(c)


# - 연산자는 difference(차집합)을 구하며, 뺄셈 연산자 -를 사용함. set.difference 메서드와 동작이 같음
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = set.difference(a, b)
print (a - b)
print(c)

# ^ 연산자는 symmetric_difference(대칭차집합)을 구하며, XOR 연산자 ^을 사용합니다. set.symmetric_difference 메서드와 동작이 같음
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = set.symmetric_difference(a, b)
print(a ^ b)
print(c)

# 집합 연산 후 할당 연산자 사용하기

# 세트1 |= 세트2는 세트1.update(세트2)와 같다.

a = {1, 2, 3, 4}
a|= {5} # 현재 세트에 5를 업데이트 한다.
# a.update({5})
print(a)

# 세트1 &= 세트2는 세트1.intersection_update(세트2)와 같다.

a = {1, 2, 3, 4}
#a &= {0, 1, 2, 3, 4}
a.intersection_update({0, 1, 2, 3, 4})
print(a)

# 세트1 -= 세트2는 세트1.difference_update(세트2)와 같다.

a = {1, 2, 3, 4}
#a -= {3}
a.difference_update({3})
print(a)

# 세트1 ^= 세트2는 세트1.symmetrice_difference_update(세트2)와 같다

a = {1, 2, 3, 4}
#a^= {3, 4, 5, 6}
a.symmetric_difference_update({3, 4, 5, 6})
print(a)


# 부분 집합과 상위집합 확인하기
# 세트는 부분, 상위, 진상위집합과 같이 속하는 관계를 표현할 수 있음
# 현재 세트가 다른 세트의 (진)부분 집합 또는 (진)상위집합인지 확인할 때, 세트 자료형에 부등호와 등호를 사용함


# <= 현재 세트가 다른 세트의 부분집합인지 확인, issubset 메서드와 같음
# 현재세트 <= 다른세트
# 현재세트.issubset(다른세트)

a = {1, 2, 3, 4}
print(a <= {1, 2, 3, 4})
a1 = a.issubset({1, 2, 3, 4, 5})
print(a1)

# <는 현재 세트가 다른 세트의 진부분집합인지 확인하며, 메서드는 없음
# 현재세트 < 다른세트
a = {1, 2, 3, 4}
print(a<{1, 2, 3, 4, 5})

# >=는 현재 세트가 다른 세트의 상위집합인지 확인, issuperset 메서드와 같다
a = {1, 2, 3, 4}
print(a>={1, 2, 3, 4})
print(a>={1, 2, 3, 4, 5})
a1 = a.issuperset({1, 2, 3, 4})
print(a1)

# >는 현재 세트가 다른 세트의 진상위집합인지 확인하며, 메서드는 없음
# 현재세트 > 다른세트
a = {1, 2, 3, 4}
print(a>{1, 2, 3})

# == 연산자는 세트가 같은지 다른지 확인
a = {1, 2, 3, 4}
print(a=={1, 2, 3, 4})
print(a=={4, 2, 3, 1}) # 세트는 요소의 순서가 정해져 있지 않아, 각 요소만 같으면 참이다

# != 연산자는 세트가 다른지 확인
a = {1, 2, 3, 4}
print(a!={1, 3, 2})

# disjoint는 현재 세트가 다른 세트와 겹치지 않았는지 확인
# 겹치는 요소가 없으면 True, 있으면 False
# 현재세트.isdisjoint(다른세트)

a = {1, 2, 3, 4}
a1 =a.isdisjoint({5, 6, 7, 8})
a2 = a.isdisjoint({4, 3, 6, 5})
print(a1)
print(a2)




# 세트 조작하기

# 세트에 요소 추가하기 
# add(요소)

# 세트에 특정 요소를 삭제하기
# remove(요소) >> 세트에서 특정 요소를 삭제하고 요소가 없으면 에러를 발생시킴
# discard(요소) >> 세트에서 특정 요소를 삭제하고 요소가 없으면 그냥 넘어감

# 임의의 요소를 삭제하기
# pop() >> 임의의 요소를 삭제하고 해당 요소를 반환함. 요소가 없으면 에러를 발생시킴

# 모든 요소를 삭제하기
# clear()

# 세트의 요소 개수 구하기
# len(세트) >> 세트의 요소 개수(길이)를 구함


# 세트의 할당과 복사
a = {1, 2, 3, 4}
#b = a # 세트가 2개일 것 같지만 세트가 1개임.
# print(a is b) # 객체가 같기 때문에, True
# b.add(5) # b에 5를 추가하면, a에도 추가가 될 것
#print(a) # a를 출력하면 b에서 추가된 5가 들어가 있는 것을 알 수 있다.

b = a.copy() # 세트a와 세트b를 완전히 2개로 만들기 위해 copy 메서드를 사용함
b.add(5)
print(a) # a와 b가 다른 객체이기 때문에, b에서 추가된 5가 보이지 않음
print(b) # b에선 추가된 5가 들어가있는 것을 볼 수 있음

print(a is b) # 두 객체가 다르기 때문에 False가 나옴. 같은 경우에는 True
print(a == b) # 요소가 다르기 때문에 False가 나옴. 같은 경우에는 True(객체는 달라도 요소가 같으면 True)

# 반복문으로 세트의 요소를 모두 출력하기

a = {1, 2, 3, 4}
for i in a:
    print(i)

# 세트 표현식 사용
# {식 for 변수 in 반복가능한객체}
# set(식 for 변수 in 반복가능한객체)

a = {i for i in 'apple'}
print(a)

# 세트 표현식에 if 조건문 사용
# {식 for 변수 in 세트 if 조건식}
# set(식 for 변수 in 세트 if 조건식)

a = {i for i in 'pineapple' if i not in 'apl'}
print(a)
