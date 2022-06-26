# i = 1
# while True:
#     print('반복:',i)
#     i += 1
#     if i == 51:     # i가 51 이면 코드를 중단함. i는 1이기 때문에 총 50회까지 반복한다.
#         break

# for i in range(1, 1001):
#     print('반복:',i)
#     if i == 10:     # i == 10인 경우 코드 실행을 중단함.
#         break


# for i in range(20):
#     if i % 2 == 0:      # i가 짝수이면 아래 코드를 실행하지 않고 다음 반복으로 건너뜀
#         continue
#     print('반복 홀수_for:', i)


# i = 0
# while i < 20:
#     i += 1
#     if i % 2 == 0:      # i가 짝수이면 아래 코드를 실행하지 않고 다음 반복으로 건너 뜀
#         continue
#     print('반복 홀수_while:',i)

# count = int(input())

# i = 1
# while True:
#     print('반복 수:',i)
#     i += 1
#     if i == count + 1:  # count 받은 숫자만큼만 반복함. 조건을 만족하면 코드를 중단시킨다.
#         break

count = int(input())

for i in range(count + 1):
    if i % 2 == 0:              # 입력한 숫자만큼 반복하는데 홀수만 출력한다.
        continue
    print('반복 홀수:', i)


