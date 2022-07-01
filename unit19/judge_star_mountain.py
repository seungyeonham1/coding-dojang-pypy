
# 표준 입력으로 삼각형의 높이가 입력됨
# 입력된 높이 만큼 산 모양으로 별을 출력하는 프로그램을 만드세요.


height = int(input())

#오른쪽

for i in range(height):
    for j in reversed(range(height)):  
        if i < j:
            print(' ', end= '') 
        else:
            print('*', end= '')

#왼쪽
    for j in range(height):
        if i > j:
            print('*', end = '')
    print()



#왼쪽 입력값이 3일때

# i = 0  j = 2 1 0     *' '' '
# i = 1  j = 2 1 0     **' '
# i = 2  j = 2 1 0     ***


#오른쪽 입력값이 3일때
 
# i = 0 j = 2 1 0 ' '' '' '
# i = 1 j = 2 1 0  ' '' '*
# i = 2 j = 2 1 0    ' '**