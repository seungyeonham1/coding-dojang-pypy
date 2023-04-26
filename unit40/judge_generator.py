
# 표준 입력으로 정수 2개가 입력됨 (첫 번째 입력 값의 범위 10~1000, 두 번째 입력 값의 범위는 100~1000, 첫 번째 입력 값은 항상 두 번째 입력 값보다 작음)
# 첫 번째 정수부터 두 번째 정수 사이의 소수(prime number)를 생성하는 제너레이터를 만드세요.
# 소수는 1과 자기 자신으로 나누어 떨어지는 1보다 큰 양의 정수입니다.


def prime_number_generator(start, stop):

    for n in range(start, stop):
        check = True # 소수 확인용 변수 생성
        for i in range(2, n): # 입력한 start ~ stop 범위까지 소수 판별 
            if n % i == 0: # 소수가 아닌 경우
                check = False  # 소수 여부 False 처리
        if check: # 소수 판별한 것들 중에
            yield n  # 소수로 판별된 값만 바깥으로 전달


start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))

for i in g:
    print(i, end=' ')