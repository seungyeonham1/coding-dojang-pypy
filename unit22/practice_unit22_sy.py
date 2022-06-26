# a = [10, 20, 30]
# a.append(500)   # a 리스트 맨 뒤 인덱스에 500이라는 요소를 추가한다.
# print(a)
# print(len(a))

# a1 = [10, 20, 30]
# a1.append([100,200,300])    # a 리스트 맨 뒤 인덱스에 리스트를 추가한다. 리스트 안에 리스트를 추가하기 때문에 2차원 리스트가 된다.
# print(a1)

# a2 = [10, 20, 30]
# a2.extend('abc')    # extend는 리스트 맨 뒤 인덱스에 반복 가능한 객체의 요소를 연결해서 리스트 길이를 연장한다. 반복 가능한 객체라면 뭐든지 넣을 수 있음.
# print(a2)

# a3 = [10, 20, 30]
# a3.insert(1, ['a','b','c'])     # insert는 리스트 내의 원하는 인덱스에 새 요소를 추가할 수 있다. extend처럼 리스트를 연장하지는 않기 때문에 리스트를 연장하고 싶다면 리스트 슬라이스를 사용하자.
# print(a3)

# a4 = [10, 20, 30]
# a4[1:1] = ['a','b','c']
# print(a4)

# a5 = [10, 20, 30]
# print(a5.pop())     # pop()은 리스트의 마지막 인덱스 요소를 반환하고 해당 요소를 리스트에서 제거한다. pop(2) 같이 제거하고 싶은 인덱스 위치를 지정할 수도 있다.
# print(a5)

# a6 = [10, 20, 30]
# del a6[1]     # del은 pop과 거의 비슷하지만 제거하는 요소를 반환하지 않는 정도의 차이만 있다.
# print(a5)

# a7 = [10, 20, 30, 'a']
# a7.remove('a')      # remove는 특정 값을 기준으로 요소를 찾아서 제거한다. 인덱스와 관련없이 값이 일치하는 요소만 찾아서 제거한다.
# print(a7)

# a8 = [10, 'a', 20, 30, 'a']
# a8.remove('a')      # 단, remove는 한번에 하나의 요소만 찾아서 제거할 수 있다. 이 경우, 가장 먼저 찾은 요소를 제거하기 때문에, 인덱스가 더 빠른 요소가 우선시 된다.
# print(a7)

# b = [10, 20, 30, 40, 50]
# print(b.index(20)) # 리스트 내 특정 값의 인덱스 찾기

# b1 = [10, 20, 30, 40, 50, 20]
# print(b1.count(20)) # 리스트 내 특정 값의 개수 세기

# b2 = [10,15,20,30,60,70]
# print(list(reversed(b2)))
# b2.reverse()        # reverse는 리스트의 순서를 뒤집는다. reversed의 경우 비 파괴적이지만 reverse는 파괴적이다.
# print(b2)

# b3 = [10,15,20,30,60,70,23,19]
# b3.sort()       # sort()는 리스트 내의 요소를 작은 순서대로 정렬한다. 문자열이라면 a,b,c,d 순으로 정렬함.
# print(b3)
# b3.sort(reverse=True) # sort()안에 reverse=True를 넣으면 리스트 내의 요소를 큰 순서대로 정렬한다.
# print(b3)

# b4 = [1,2,3,4,5,6,7,8]
# b4.clear()      # clear() 메서드는 리스트 내의 요소를 모두 삭제한다. 이 경우 리스트는 빈 리스트가 된다. del b4[:] 도 같은 동작을 한다.
# print(b4)

# b5 = [1,2,3,4,5,6,7,8]
# b5[len(b5):] = [500,600,700]        # 리스트의 마지막에 해당 요소를 이어서 붙인다. extend와 같은 동작.
# print(b5)

# seq = ['daytime1','daytime2']
# if seq :                # seq 리스트가 비어있지 않다면 True를 반환하기 때문에 seq에 요소가 하나라도 있다면 가장 마지막 요소를 출력한다.
#                         # 주로 게임에서 가장 최근 매칭 정보나 가장 최근에 구매한 아이템 등을 표시할때 사용한다.
#     print(seq[-1])




# a = [0,0,0,0]
# b = a           # 어차피 같은 리스트 객체를 사용하여 변수에 저장만 하고 있는 거라 같은 객체 취급이다.
# print(a is b)

# # b[2] = 100      # 따라서 b에서 리스트에 뭔가 요소를 변경하면 a가 들고있는 리스트에도 적용된다.
# # print(a)

# b = a.copy()      # copy 메서드를 사용하여 리스트를 복사하여 할당하면 다른 객체로 취급된다.
# print(a is b)
# b[2] = 150
# print(a)

# a = [38, 21, 53, 10, 11]

# for i in a:     # list는 반복가능한 객체기 때문에 for 문에서도 사용할 수 있다.
#     print(i)

# for index, value in enumerate(a): # enumerate에 리스트를 넣으면 for 반복문에서 리스트의 요소와 인덱스를 같이 꺼내올 수 있다.
#     print(index, value)

# for index, value in enumerate(a, start=1): # enumerate에 start=1을 하면 모든 인덱스 값에 1을 더한다.
#     print(index, value)


# i = 0
# while i < len(a):       # i가 len(a) 보다 작을 때. 즉 리스트의 길이만큼 반복한다. 파이썬은 제로 인덱싱이며, len은 요소의 개수를 반환한다. 따라서 요소가 5개라면 인덱스는 4가 끝이다.
#     print(a[i])
#     i += 1

# smallest = a[0]
# for i in a:
#     if i < smallest:
#         smallest = i

# print(smallest)


# largest = a[0]
# for i in a:
#     if i > largest:
#         largest = i

# print(largest)

# a1 = [38, 21, 53, 10, 11]
# a1.sort()
# print(a1[0])

# a1.sort(reverse=True)
# print(a1[0])

# print(max(a))
# print(min(a))

# b = [5,5,5,5,5]
# # x = 0
# # for i in b:
# #     x += i

# print(sum(b))

# a = [i for i in range(10)]      # 리스트 컴프리헨션. 리스트 안에서 반복문을 돌려서 리스트를 생성하는 파이썬식 줄임 코드다.
# print(a)
# b = list(i for i in range(10))
# print(b)

# c = [i + 5 for i in range(10)] # 0부터 9까지 숫자를 뽑아서 i에 저장하는데 i에 5를 더해가면서 리스트를 생성
# d = [i * 2 for i in range(10)] # 0부터 9까지 숫자를 뽑아서 i에 저장하는데 i에 2를 곱해가면서 리스트를 생성
# print(c)
# print(d)

# a1 = [i for i in range(10) if i % 2 == 0] # 0부터 9까지 숫자를 뽑아서 i에 저장하는데 i가 2의 배수인 경우에만 리스트로 만듬
# print(a1)

# a2 = [i * j for j in range(2, 10)
#             for i in range(1, 10)] # 구구단을 리스트 컴프리헨션으로 표현하기
# print(a2)

# a = [1.2, 2.5, 3.5, 5.0]
# for i in range(len(a)):     # 리스트의 인덱스를 가져오고, 요소 하나하나를 int로 변환하기
#     a[i] = int(a[i])

# print(a)

# # 사실 이러면 꽤 귀찮다.

# b = [1.2, 2.5, 3.5, 5.0]
# b = list(map(int, b))       # map을 사용하면 각 요소를 지정된 함수로 처리할 수 있다. 여기서는 int.
# print(b)

# # map은 모든 반복가능한 객체를 넣을 수 있다. range 또한 반복가능한 객체기 때문에 넣을 수 있음

# c = list(map(str, range(10)))   # range로 생성되는 숫자를 전부 str로 받는다.
# print(c)

# d = map(int, input().split())   # input.split으로 입력받는 경우 스트링으로 구성된 리스트를 생성하기 때문에 마찬가지로 map에 넣을 수 있다.
# print(list(d))

# e1, e2, e3 = map(int, input().split())   # map 또한 이터레이터기 때문에 언패킹을 사용할 수 있다.
# print(e1)
# print(e2)
# print(e3)

# a,b,c,d = list(range(4))
# print(a)
# print(b)
# print(c)
# print(d)

from math import *
from decimal import *

a,b,c = [1.1, 2.2, 3.5]



print(Decimal(str(a)) + Decimal(str(b)) + Decimal(str(c)))