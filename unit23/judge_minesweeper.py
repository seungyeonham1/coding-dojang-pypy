
#col = 열 ,가로
#row = 행, 세로


#지뢰판 크기 입력

col, row = map(int,input().split()) # 가로 , 세로 값을 입력받는다. (지뢰판 크기)

# 3, 3 입력

# 지뢰 넣기

matrix = []  # 빈 리스트 생성
for i in range(row): # 입력받을 때 까지 반복함
    matrix.append(list(input()))


# 입력한 3x3판에 지뢰를 입력함

# .**  
# *..  
# .*.  


# 지뢰 판독

for i in range(row): # 세로 반복
    for j in range(col): # 가로 반복
        if matrix[i][j] == '*': # 지뢰가 맞으면  col:3 row:3  인덱스 (0,0)부터 시작 
            continue # 아래 코드 실행 x
        else:
            matrix[i][j] = 0 # 지뢰가 아닐 시, 0 값으로 전부 줌.

# 0**
# *00
# 0*0

# 위 아래 탐색 기능

            for y in range(i-1, i+2): # 위 아래 반복 
                for x in range(j-1, j+2): # 왼쪽부터 오른쪽 반복
                    if x < 0 or y < 0 or x >= col or y >= row: 
                        continue
                    elif matrix[y][x] == '*':
                        matrix[i][j] = matrix[i][j] + 1 

# (0,0) 값이므로 y는 -1 x는 -1부터 시작


for i in range(row):
    for j in range(col):
        print(matrix[i][j], end = '')
    print()