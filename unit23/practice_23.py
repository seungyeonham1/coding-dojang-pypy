
# 2차원 리스트 = 리스트 안에 또 다른 리스트가 있다
# 가로 좌표와 세로 좌표가 존재

# 2차원 리스트 요소에 접근
# 리스트[세로인덱스][가로인덱스]
# 리스트[세로인덱스][가로인덱스] = 값


# 톱니형 리스트 = 리스트 가로 크기가 불규칙한 리스트
# a = [[10, 20],
#     [500, 600, 700],
#      [9]
#      [30, 40]]


# for 반복문을 한 번만 사용

# a = [[10, 20], 
#      [30, 40], 
#      [50, 60]]


# for x, y in a: # 리스트 가로 한 줄에서 요소 2개를 꺼냄
#     print(x, y)


# for 반복문을 두 번 사용하기

# a = [[10, 20], 
#      [30, 40], 
#      [50, 60]]

# for i in a: # a에서 안쪽 리스트를 꺼냄
#     for j in i: # 안쪽 리스트에서 요소를 하나씩 꺼냄
#         print(j, end=' ')
#     print()



# for와 range 사용

# a = [[10, 20], 
#      [30, 40], 
#      [50, 60]]

# for i in range(len(a)): # 세로
#     for j in range(len(a[i])): # 가로
#         print(a[i][j], end = ' ')
#     print()


# while 반복문 사용


# a = [[10, 20], 
#      [30, 40], 
#      [50, 60]]

# i = 0
# while i < len(a): # 리스트 크기(세로)보다 작으면 반복
#     x, y = a[i] # 요소 2개를 가져간다
#     print(x, y) # 가져간 요소를 출력
#     i += 1 # i 값은 1만큼 증가 (카운트값)


# # while 반복문 두 번 사용하기

# a = [[10, 20], 
#      [30, 40], 
#      [50, 60]]

# i = 0
# while i < len(a): # 리스트 크기(세로)보다 작을 경우 반복
#     j = 0 
#     while j < len(a[i]):  # 리스트 크기(가로)보다 작을 경우 반복
#         print(a[i][j], end= ' ') # 내부 요소를 하나씩 출력
#         j += 1 # 가로 인덱스 값 증가
#     print()
#     i += 1 # 세로 인덱스 값 증가


# for 반복문으로 1차원 리스트 만들기

# a = []

# for i in range(10):
#     a.append(0)
# print(a)


# for 반복문으로 2차원 리스트 만들기

# a = []

# for i in range(3): # 0 ~2 반복
#     line = [] # 리스트로 만듬
#     for j in range(2):  # 0 ~ 1 반복
#         line.append(0) # 
#     a.append(line)
# print(a)


# 리스트 표현식으로 2차원 리스트 만들기

# a = [[0 for j in range(2)] for i in range(3)]
# print(a)

# a = [[0] * 2 for i in range(3)]
# print(a)


# 톱니형 리스트 만들기

# a = [3, 1, 3, 2, 5]
# b = []

# for i in a: # 가로 크기를 저장한 리스트를 반복 
#     line = [] 
#     for j in range(i): # 리스트 a에 저장된 가로 크기만큼 반복 
#         line.append(0)
#     b.append(line) # 리스트 b에 안쪽 리스트를 추가

# print(b)

# i = 5  =  [], [], [], [], [] = 리스트 5개

# 3 = 0  1 = 1 3 = 2 2 = 3 5 = 4


# j =  0 ,1 ,2
# j =  [0, 0, 0]



# a = [[0] * i for i in [3, 1, 3, 2, 5]]
# print(a)


# 람다 = 익명 함수 = define 하지 않음 = 일회용 = 소모성 함수 ?
# 람다 = 리턴 값만 보내고 사라짐 

# 반복 가능한 객체 = 이터레이블


# 2차원 리스트의 할당과 복사 알아보기

# a = [[10, 20], [30, 40]]
# b = a
# b[0][0] = 500
# print(a)


a = [[10, 20], [30, 40]]
b = a.copy()
b[0] = [1, 2]
print(a)
print(b)


# a = [[10, 20], [30, 40]]
# import copy
# b = copy.deepcopy(a)
# b[0][0] = 500
# print(a)
# print(b)







