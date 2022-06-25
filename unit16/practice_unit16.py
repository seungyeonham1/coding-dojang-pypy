
# for문
# for 변수(for문에서만 사용할 변수) in range(횟수)
# range는 숫자 개수 만큼 순서대로 나열, 인덱스 기준

# for i in range(5) # range(5)는 0,1,2,3,4를 생성하는 이터레이터, 이터레이터는 반복 가능한 개체
#    print(i)


# for문 시작하는 숫자와 끝나는 숫자 지정
# for 변수 in range(시작,끝)

# for문 증가폭 사용하기
# for 변수 in range(시작, 끝, 증가폭)

# for문 감소폭 사용하기
# for 변수 in range(시작, 끝, 감소폭)

# 감소폭 reversed 사용
# for 변수 in reversed(range(횟수))
# for 변수 in reversed(시작, 끝)
# for 변수 in reversed(시작, 끝, 증가폭)

#for i in range(5, 12):
#    print('Hello, wolrd', i)

#for i in range(0, 10, 2):
#    print('Hello, world', i)

#for i in range(10, 0 , -2):
#    print('Hello, world', i)

#for i in reversed(range(0, 10, 2)):
#    print('Hello, java', i)


# 시퀀스 객체로 반복하기
# for 문에 리스트, 튜플, 문자열 등 시퀀스 객체로 반복할 수 있음


# 리스트 요소를 꺼내면서 반복하는 출력

#a = [10, 20, 30, 40 ,50]
#for i in a:
#    print(i)

# 튜플의 요소를 꺼내면서 반복하는 출력

#a = ('장준', '장준1', '장준2', '장준3')
#for i in a:
#    print(i)


# 문자열을 꺼내면서 반복하는 출력

#for letter in 'Valheim':
#    print(letter, end=' ')


# reversed를 사용한 문자열을 뒤집어서 출력 

#for letter in reversed('썬이파 의준장'):
#    print(letter, end=' ')



for i in range(20, 10):
    print(i)