# for i in range(5):      # 0 1 2 3 4
#     for j in range(5):  # 0 1 2 3 4
#         print('j:', j, sep='', end=' ')     # 안쪽 루프에서 도는 코드
#     print('i:', i, '\\n', sep='')           # 바깥쪽 루프에서 도는 코드 \n을 이스케이프 하기 위해 \ 넣어줌

# for i in range(5):
#     for j in range(5):
#         print('*', end='')  # 별 출력하기. end=''을 넣어서 각 *들이 개행처리 되지 않고 한줄로 출력되도록 한다.
#     print()                 # print()은 개행. 즉 for j in range(5)가 다 돌고 나면 개행처리를 하도록 넣는다. i에서 숫자를 뽑을때 마다 개행처리 할것임.

# for i in range(2):
#     for j in range(10):
#         print('*', end='')  # 별 출력하기. end=''을 넣어서 각 *들이 개행처리 되지 않고 한줄로 출력되도록 한다.
#     print()                 # print()은 개행. 즉 i에서 숫자를 뽑을때 마다 개행처리 할 것임.

for i in range(5):
    for j in range(5):
        if j <= i:      # i가 j 보다 크거나 같은 경우에만 별을 출력한다. i가 0인 경우 j도 0인 경우에만 *을 출력한다.
            print('*', end='')
    print()


for i in range(5):
    for j in range(5):
        if j == i:              # j가 i와 매치하는 경우에만 *을 출력한다. 즉 가로 세로 좌표가 일치하는 경우에만 별을 출력
            print('*', end='')
        else:                   # 문자열이 None인 경우에는 자동으로 좌측 정렬을 하기 때문에 가로 세로 좌표가 일치하지 않는 케이스에는 공백을 넣어서 문자열이 대각선으로 출력되도록 한다.
            print(' ', end='')
    print()

