
# 리스트 요소 추가
# append: 요소 하나를 추가
# extend: 리스트 연결을 하여 확장
# insert: 특정 인덱스에 요소 추가


# 리스트 추가하기
# a = [11, 22, 33]
# a.append(100)
# print(a)
# print(len(a))

# a = []
# a.append([11, 22, 33, 44])
# print (a)

# a = [11, 22, 33]
# a.append([44, 55, 66])
# print(a)
# print(len(a))

# 리스트 확장하기
# a = [11, 22, 33]
# a.extend([55, 66, 77, 88])
# print(a)
# print(len(a))


# 특정 인덱스에 요소 추가하기

# a = [11, 22, 33] #  0 = 11, 1 = 22, 2 = 33
# a.insert(2, 99) 
# print(a) # 11 22 99 33
# print(len(a))

# a = [11, 22, 33] #  0 = 11, 1 = 22, 2 = 33
# a.insert(len(a), 99)  # 마지막 인덱스보다 큰 값을 지정하면 리스트 끝에 요소를 추가시킴
# print(a) # 11 22 33 99
# print(len(a))

# a = [11, 22, 33] 
# a.insert(2, [99,100,101])
# print(a) 

# a = [11, 22, 33]
# a[1:1] = [99,100,101]
# print(a) 


# 리스트 요소 삭제
# pop : 마지막 요소 or 특정 인덱스 요소를 삭데
# remove : 특정 값을 찾아서 삭제


# 특정 인덱스 요소 삭제
# a = [11, 22, 33] 
# a.pop()
# print(a)

# a = [11, 22, 33] 
# a.pop(1)
# print(a)

# a = [11, 22, 33] 
# del a[0]
# print(a)

# 리스트 특정 값을 찾아서 삭제
# a = [11, 22, 33] 
# a.remove(22)
# print(a)

# 리스트에서 특정 값의 인덱스 구하기
# index 

# a = [11, 22, 33] 
# print(a.index(22))

# a = [11, 22, 33, 22, 22] 
# print(a.count(22))

# 리스트 순서를 뒤집기
# reverse

# a = [11, 22, 33]
# a.reverse()
# print(a)

# 리스트 요소 정렬하기
# sort / sort(reverse=False): 리스트의 값을 작은 순서대로 (오름차순)
# sort(reverse=True): 리스트의 값을 큰 순서대로 (내림차순)

# 내림차순
# a = [11, 22, 33, 99, 55]
# a.sort(reverse=True)
# print(a)

# 오름차순
# a = [11, 22, 33, 99, 55]
# a.sort(reverse=False) # a.sort()와 같음
# print(a)

# 리스트 모든 요소를 삭제하기
# clear() / del 변수명[:]

# a = [11, 22, 33, 99, 55]
# del a[:] #a.clear()와 같음
# print(a)

# 리스트를 슬라이스로 조작하기


# a = [11, 22, 33, 99, 55]
# a[len(a):] = [500] #리스트 끝에서부터 시작하겠다.  11 22 33 99 55 500
# print(a)

# 1개 추가  a[len(a):] = [500]  == a.append(500)
# # 여러개 추가 a[len(a):] = [500,600] == a.extend([500, 600])

# 리스트가 비어 있는지 확인
# if not len(seq): 리스트가 비어있으면 True
# in len(seq): 리스트에 요소가 있으면 True

# if not seq: 리스트가 비어 있으면 True
# if seq: 리스트에 내용이 있으면 True

# seq = [1, 2, 3, 4, 5]
# if seq: #리스트에가 요소가 있다면
#     print(seq[-2]) # 마지막 요소 다음 요소를 가져온다  5 4 3 2 1 => 4


# 리스트의 할당과 복사

# a = [0, 0, 0, 0] 
# b = a # b와 a의 리스트는 같으므로
# print(a is b) # a는 b가 맞기 때문에, true값이 나온다

# b[3] = 22
# print(a)


# 리스트를 완전히 2개로 만들기
# copy()

# a = [0, 0, 0, 0]
# b = a.copy() # b는 a리스트 요소를 복사하였으나 리스트는 서로 다른 객체
# print(a is b) # 리스트는 서로 다르기 때문에 false값이 나옴
# print(a == b) # 리스트 요소는 같기 때문에 True값이 나옴

# for 반복문으로 리스트의 요소를 모두 출력하기

# a = [38, 39, 40, 41 ,42]
# for i in a:
#     print(i)

# for index, value in enumerate(a): # 인덱스와 요소를 함께 출력
#     #print(index, value) # 인덱스 0부터 
#     print(index+1, value) #인덱스 1부터

# 인덱스 1부터 출력하기
# a = [38, 39, 40, 41 ,42]
# for index, value in enumerate(a, start = 1):
#     print(index, value)


# for문에서 인덱스 요소로 출력

# a = [1, 11, 22, 33, 44]
# for i in range(len(a)): # i에는 요소가 아닌 0부터 마지막 인덱스까지 인덱스가 들어감
#     print(a[i])


# while문에서 반복문으로 요소 출력하기
# a = [2, 4, 6, 8, 10]
# i = 0
# while i < len(a):  # i가 마지막 인덱스까지 작을 경우 
#     print(a[i]) # 0 1 2 3 4 출력
#     i+=1 #i는 1씩 증가함


# 가장 작은 수와 가장 큰 수
# smallest 변수 = 직접 선언
# largest 변수 = 직접 선언
# sort 메서드 = 오름차순 
# min, max 함수 사용

# 요소의 합계 
# sum 함수 사용


# 리스트 표현식 사용하기
# 식 for 변수 in 리스트
# list(식 for 변수 in 리스트)


# a = [i for i in range(10)] # 0부터 9까지 숫자를 생성하여 리스트 생성
# print(a)

# b = list(i for i in range(10)) # 0부터 9까지 숫자를 생성하여 리스트 생성
# print(b)

# c = [i + 5 for i in range(10)] # 0부터 9까지 숫자를 생성하여, 값에 5를 더한 리스트를 생성
# print(c)

# d = [i * 2 for i in range(10)]
# print(d)


# 리스트 표현식에서 if 조건문 사용
# 식 for 변수 in 리스트 if 조건식
# list(식 for 변수 in 리스트 if 조건식)

# a = [i for i in range(10) if i % 2 == 0]
# print(a)

# b = [i + 5 for i in range(10) if i % 2 == 1]
# print(b)



# for문과 if 조건문 여러 번 사용하기
# for 변수1 in 리스트1 if 조건식1
# for 변수2 in 리스트2 if 조건식2

# list(식 for 변수1 in 리스트1 if 조건식1)
#     (식 for 변수2 in 리스트2 if 조건식2)

# a = [i * j for j in range(2, 10) 
#            for i in range(1, 10)]
# print(a)


# 리스트에 map 사용하기
# list(map(함수, 리스트))
# tuple(map(함수, 튜플))

# a = [1.2, 2.5, 3.7, 4.6]

# for i in range(len(a)):
#     a[i] = int(a[i]) # 리스트를 하나하나 가져와서 int로 변환
#     print(a)

# a = list(map(int, a)) # map을 사용하여 코드 줄을 한 줄로 요약
# print(a)


# range를 사용하여 숫자를 만든 뒤, 숫자를 문자열로 변환
# a = list(map(str, range(10)))
# print(a)

# input().split()과 map

# a = input().split()

# a = map(int, input().split())
# print(list(a))

# map이 반환하는 객체는 '이터레이터'라서 변수 여러개에 저장하는 언패킹이 가능함

# a, b = map(int, input().split())를 풀어서 쓰면 
# x = input().split()  결과는 문자열 리스트
# m = map(int, x) 리스트의 요소를 int로 변환, 결과는 맵 객체
# a, b = m  # 맵 객체는 변수 여러 개에 저장할 수 있음












