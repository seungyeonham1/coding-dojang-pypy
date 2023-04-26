
# 2차원 리스트 = 리스트 안에 또 다른 리스트가 있다 
# [[ , ], [ , ], [ , ]]

# 가로 좌표와 세로 좌표가 존재

# 2차원 리스트 요소에 접근
# 리스트[세로인덱스][가로인덱스]
# 리스트[세로인덱스][가로인덱스] = 값


# 톱니형 리스트 = 리스트 가로 크기가 불규칙한 리스트
# a = [[10, 20],
#     [500, 600, 700],
#      [9]
#      [30, 40]]


# 2차원 리스트를 사각형 구조로 유지하도록 출력하는 함수 = pprint
# from pprint import pprint
# pprint(변수, indent=들여쓰기 칸 수, width=가로 폭 수치)


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

# for i in a: # a에서 안쪽 리스트를 꺼냄 # 첫번째 요소 [10, 20]
#     for j in i: # 안쪽 리스트에서 요소를 하나씩 꺼냄  # [10, 20] -> 10 20
#         print(j, end=' ') 
#     print()



# for와 range 사용

#a = [[10, 20], 
#    [30, 40], 
#    [50, 60]]

#for i in range(len(a)): # 세로
#     for j in range(len(a[i])): # 가로
#         print(a[i][j], end = ' ')
#     print()


# while 반복문 사용


# a = [[10, 20], 
#      [30, 40], 
#      [50, 60]]

# i = 0
# while i < len(a): # 리스트 크기(세로)보다 작으면 반복  # len(a) = 3 ... 즉 0, 1, 2행
#     x, y = a[i] # 요소 2개를 가져간다  10 20 / 30 40 / 50 60
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

# for i in a: # 가로 크기를 저장한 리스트를 반복   a 는 3
#     line = [] 
#     for j in range(i): # 리스트 a에 저장된 가로 크기만큼 반복  # i = 3  j = 0 , 1 , 2
#         line.append(0) # 라인에 0을 추가한다.
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


# 2차원 리스트 정렬하고 싶다 = sorted 함수를 사용함
# sorted(반복가능한객체, key=정렬함수, reverse=True 또는 False)

#students = [ 
#    ['민트', 'C', 19],
#    ['피스타치오', 'A', 25],
#    ['초콜렛', 'B', 7]
#]

# 정렬 함수를 람다 표현식으로 작성
#print(sorted(students, key=lambda student: student[1])) # 인덱스 1의 기준으로 정렬한다 (피스타치오>초콜렛>민트)
#print(sorted(students, key=lambda student: student[2])) # 인덱스 2의 기준으로 정렬한다 (초콜렛>민트>피스타치오)




# 2차원 리스트의 할당과 복사 알아보기

# a = [[10, 20], [30, 40]]
# b = a
# b[0][0] = 500
# print(a)


#a = [[10, 20], [30, 40]]
#b = a.copy()
#b[0] = [1, 2]
#print(a)
#print(b)

# 2차원 이상의 다차원 리스트는 리스트를 완전히 복사하기 위해선 copy 모듈의 deepcopy 함수를 사용해야함

# a = [[10, 20], [30, 40]]
# import copy # copy 모듈을 가져온다
# b = copy.deepcopy(a) # deepcopy 함수를 사용하여 완전히 복사한다
# b[0][0] = 500
# print(a)
# print(b)




#지뢰 갯수를 출력하는 프로그램


# 입력값  
col, row = map(int, input().split())


# 지뢰판 크기 및 지뢰 유무 입력
matrix = []
for i in range(row):
    matrix.append(list(input()))


# 지뢰 판독기

for i in range(row): # 입력받은 row 값을 i에 할당
    for j in range(col): # 입력받은 col 값을 j에 할당
        if matrix[i][j] == '.': # matrix 요소가 '.' 이라면
            matrix[i][j] = 0 # '.'인 요소를 전부 0으로 바꿔준다.
            
#print(matrix)

# 지뢰 갯수 확인 기능
# 0행부터 0열에서 2열까지 반복
# 0행이 끝났으면 1행부터 0열에서 2열까지 반복 ..... 
# 할당할 값을 정한다. y = row  x = col


            for y in range(i-1, i+2): 
                for x in range(j-1, j+2): 


        #리스트 요소가 음수인 값 해결하기 위한 조건문 작성
                    if y < 0 or x < 0 or y >= row or x >= col:
                        continue # 리스트 요소가 음수라면 다음 조건문을 실행하지 않고 넘어갈것
                    elif matrix[y][x] == '*': # 리스트 요소가 지뢰 라면 
                        matrix[i][j] = matrix[i][j] + 1 # 리스트 요소 값에 1을 더한다.

for i in range(row):
    for j in range(col):
        print(matrix[i][j], end = '')
    print()

    #조건식



