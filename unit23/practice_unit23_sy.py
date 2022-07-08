# a = [1,
#      2,
#      3,
#      4,
#      5,
#      6]

# a_2dim = [[1,2],
#           [3,4],
#           [5,6]]


# print(a[2])
# print(a_2dim[2])
# print(a_2dim[2][0])

# a_2dim[2][0] = 50
# print(a_2dim)


# a_2dim_jag = [[1,2],
#               ['a','b','c'],
#               [10,20,30,40],
#               ['g']]

# b = []
# b.append([])
# b[0].append(10)
# b[0].append(20)
# b.append([])
# b[1].append('a')
# b[1].append('b')
# b[1].append('c')

# print(b)

# a = [[10,20],
#      [30,40],
#      [50,60]]

# # for x, y in a:      # 2차원 리스트에서 각 요소 출력하기. for문과 같지만 반복 인자 변수를 두개를 지정해야한다. 3차원 리스트라면 3개가 필요할 것.
# #     print(x, y)

# # print()

# # for i in a:         # for문 두번 써서 출력하기. a에서 안쪽 리스트를 전부 뽑아온다. i는 리스트를 가짐
# #     for j in i:     # 이제 i에 할당되어 있는 리스트 안에 있는 요소를 전부 뽑아온다.    
# #         print(j, end=' ')
# #     print()         # 세로 방향의 리스트 개수만큼 개행한다.

# # print()

# # for i in range(len(a)):             # 세로 방향 만큼 반복한다. len(a) = 3, i = 1
# #     for j in range(len(a[i])):      # 가로 방향 만큼 반복한다. len(a[1]) = 2 , j = 0
# #         print(a[i][j], end=' ')     # a[i][j] 와 같은 형태로 2차원 리스트의 요소에 접근하고, 출력.  a[1][0], a[1][1]
# #     print()                         # 세로 방향 만큼 개행한다.

# # print()


# # i = 0
# # while i < 3:       # 세로 길이만큼 반복함.
# #     x, y = a[i]         # 내부 리스트를 가져오고, 언패킹 x, y = [10,20]
# #     print(x, y)         # 그대로 출력한다.
# #     i += 1              # 반복 카운트를 1 증가 시켜서 다음 내부 리스트를 가져오도록 함

# # i = 0
# # while i < len(a):                   # 가로 길이 만큼 반복시킨다.
# #     j = 0                           
# #     while j < len(a[i]):            # 세로 길이 만큼 반복시킨다.
# #         print(a[i][j], end=' ')     # a[i][j] 로 내부 요소 하나씩 출력
# #         j += 1                      # 가로 인덱스 1 증가시키기
# #     print()
# #     i += 1                          # 세로 인덱스 1 증가시키기

# a = []

# for i in range(10):
#     a.append(10)

# print(a)

# a = []

# for i in range(10):         # 10회 반복.
#     line = []               # 내부 리스트로 추가할 line 이라는 빈 리스트를 먼저 선언하고, 매 반복마다 빈 리스트로 초기화한다.
#     for j in range(2):      # 2회 반복.
#         line.append(10)     # line 리스트에 10이라는 요소를 두번 추가
#     a.append(line)          # line을 a에 추가한다.

# print(a)

# a = [[0 for j in range(2)] for i in range(3)]
# print(a)

# a = [[0] * 2 for i in range(3)]
# print(a)

# a = [[0] * i for i in [3,1,3,2,5]]
# print(a)

# # [[0,0,0],[0],[0,0,0],[0,0],[0,0,0,0,0]]

# a =  [[10, 20],
#       [30, 40]]

# b = a
# b[0][0] = 560

# print(a)
# print(b)

# b = a.copy()
# b[0] = [50, 500]

# print(a)
# print(b)

# from copy import *

# a =  [[10, 20],
#       [30, 40]]
# b = deepcopy(a)
# # deepcopy 함수를 사용하여 깊은 복사. 왜 deepcopy를 해야하는지는 선언 찾아봐도 잘 모르겠음.
# # 읽어보면 copy로는 리스트는 복사할 수 있지만 리스트 내의 리스트를 복사할 수 없으니 대신 deepcopy를 쓰라고 설명되어 있음. 그냥 문법인듯?

# b[0][1] = 500

# print(a)
# print(b)

col = 5
row = 5


matrix = []
for i in range(row):
    matrix.append(list(input()))


for i in range(row):
    for j in range(col):
        if matrix[i][j] == '.' :
            matrix[i][j] = 0

print(matrix)

# [0][0] [0][1] [0][2]
# [1][0] [1][1] [1][2]
# [2][0] [2][1] [2][2]