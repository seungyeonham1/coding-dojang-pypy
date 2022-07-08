
# 표준 입력 정수 2개
# 첫 번째 입력값 범위 1~200
# 두 번째 입력값 범위 10~200
# 첫 번째 값은 두 번째 값보다 항상 작다
# 첫 번째 정수와 두 번째 정수 사이의 숫자 중 3으로 끝나지 않는 숫자가 출력되게만드세요.


start, stop = map(int, input().split())

i = start

while True:
    if not 1 <= start <= 200:
        print('start값 범위가 올바르지 않음, 입력값:{0}'.format(start))
        break
    elif not 10 <= stop <= 200:
        print('stop값 범위가 올바르지 않음, 입력값:{0}'.format(stop))
        break
    elif i % 10 == 3: # i값을 10으로 나눈 나머지가 3이라면
        i += 1 # i 값이 1만큼 증가하며
    elif i > stop: # i가 stop 값보다 크게되면
        break # 멈춘다
    print(i, end= ' ')
    i += 1