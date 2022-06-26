

# break : 제어 흐름 중단
# continue : 제어 흐름 유지, 코드 실행만 건너 뜀 (아무것도 하지x)

# while에서 break 반복문 끝내기

#i = 0
#while True:
#    print(i)
#    i += 1
#    if i == 100: # i가 100이면 
#        break # 멈춘다.


# for에서 break로 반복문 끝내기

#for i in range(10000): # 0에서 9999까지 반복
#    print(i)
#    if i == 100: # i가 100이면
#        break # 멈춘다

# for에서 continue로 코드 실행 건너 뛰기

#for i in range(100): # 0에서 99까지 반복
#    if i % 2 == 0: # 2로 나눌때 나머지가 0이면
#        continue # 그냥 건너 뛰고
#    print(i) # 홀수만 출력

# while 반복문에서 continue로 코드 실행 건너 뛰기

#i = 0
#while i < 100:  # 100보다 작을 때까지 반복
#    i += 1 # i 는 1만큼 증가시킴
#    if i % 2 == 0: # 2로 나눴을 때 나머지가 0이라면
#        continue # 짝수를 건너뛰고
#    print(i) # 홀수를 출력함

# continue와 pass는 동작은 똑같지만 용도가 다르다
# continue: 아무것도 안하고 다음 단계로 건너 뜀 
# pass

# 입력한 횟수대로 반복하기

#count = int(input('반복할 횟수를 입력하셈: '))

#i = 0
#while True: # 무한 루프
#    print(i)
#    i += 1 # i를 1씩 증가시킴
#    if i == count:  # i가 입력받은 카운트 값이면
#        break # 실행을 멈춘다


# 입력한 숫자까지 홀수 출력하기

#count = int(input('반복할 횟수를 입력하셈: '))

#for i in range(count+1): # range(count)는 0부터 시작, count의 값은 반복에 포함되지 않으므로 count+1을 해줌

#    if i % 2 == 0: #  i를 2로 나눴을 때 0이라면
#        continue # 아래 코드를 실행하지 않고 건너뜀
#    print(i)



