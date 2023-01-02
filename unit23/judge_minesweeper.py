
#col = 열 ,가로
#row = 행, 세로


#지뢰판 크기 입력

col, row = map(int,input().split()) # 지뢰판 크기의 행과 열을

# 3, 3 입력

# 지뢰 넣기

matrix = []  # 빈 리스트 생성
for i in range(row): # 행을 반복한다
    matrix.append(list(input())) # 지뢰 판에 넣을 지뢰를 입력한다.

# .**  
# *..  
# .*.  


# 지뢰 판독

for i in range(row): # 열 반복이 끝나면 행을 반복한다.
    for j in range(col): # 열을 반복하는 문으로, 리스트가 지뢰인 경우 아래 반복문을 진행하지 않고 통과한다. 0이 맞다면 아래 for문으로 이동한다.
        if matrix[i][j] == '*': 
            continue 
        else:
            matrix[i][j] = 0

# 0**    00 01 02  0 1 2
# *00    10 11 12  0 1 2
# 0*0    20 21 22  0 1 2

# 위 아래 탐색 기능

            for y in range(i-1, i+2): # x좌표(가로) 반복이 끝나면 y좌표(세로)를 반복한다.
                for x in range(j-1, j+2): # x좌표 (가로)를 반복한다.
                    if x < 0 or y < 0 or x >= col or y >= row:
                                 # 
                                 # 리스트는 음수의 값을 저장하지 못함. 결국 x, y좌표의 범위가 맞는지 판별하기 위함
                        continue # 
                    elif matrix[y][x] == '*': # 만약 전부 False이면서 커서의 위치가 지뢰인 경우에는
                        matrix[i][j] = matrix[i][j] + 1 # 커서 카운트 값이 1만큼 증가한다.

for i in range(row):
    for j in range(col):
        print(matrix[i][j], end = '')
    print()