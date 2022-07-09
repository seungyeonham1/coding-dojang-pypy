
col, row = map(int,input().split())

matrix = []  # 빈 리스트 생성
for i in range(row): # 입력받을 때 까지 반복함
    matrix.append(list(input())) # 2 x 2 배열 + 지뢰 입력 설정

for i in range(row): # i는 2까지 반복
    for j in range(col): # j는 2까지 반복 
        count = 0
        if matrix[i][j] == '.': # 인덱스 값이 지뢰가 아닌 경우 

#row:2 col:2

# 2 x 2 2
# 00(0) 01(1)  .*  0*
# 10(0) 11(1)  *.  *0

#초기 i = 0 j = 0


            if i != 0 and j != 0: 
                if matrix[i-1][j-1] == '*':  
                    count = count + 1 

                
            if i != row - 1 and j != col-1: 
                if matrix[i+1][j+1] == '*':
                    count = count + 1  


            if i != 0:
                if matrix[i-1][j] == '*':  
                    count = count + 1      



            if i != 0 and j != col-1:
                if matrix[i-1][j+1] == '*':
                    count = count + 1



            if j != 0:
                if matrix[i][j-1] == '*':
                    count = count + 1


            if i != row -1 and j != 0:
                if matrix[i+1][j-1] == '*':
                    count = count + 1

            if j != col -1:
                if matrix[i][j+1] == '*':
                    count = count +1
            
            if i != row -1:
                if matrix[i+1][j] == '*':
                    count = count + 1

            matrix[i][j] = count
            print(matrix[i][j], end='')
        else:
            print(matrix[i][j], end='')
    print()


