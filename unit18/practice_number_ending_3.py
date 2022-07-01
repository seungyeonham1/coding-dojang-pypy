

i = 0
while True:
    if i % 10 != 3: # 끝 자리수가 3인 경우가 아니라면
        i += 1 # i값이 1만큼 증가한다
        continue # 코드 실행을 건너 뛴다.
    if i > 73: #i 값이 73보다 크면
        break # 제어 흐름을 중지한다.
    print(i, end=' ')
    i += 1


# i = 0
# while i < 74:
#     i += 1
#     if i % 10 != 3:
#         continue
#     print(i, end = ' ')