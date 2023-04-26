

#a, b = map(int, input().split())

#for i in range(a, b+1):
#    if i % 5 == 0 and i % 7 == 0:
#        print('FizzBuzz')
#    elif i % 5 == 0:
#        print('Fizz')
#    elif i % 7 == 0:
#        print('Buzz')
#    else:
#        print(i)







a, b = map(int, input().split())

while True: # 먼저 조건을 충족하는지 확인한다
    if not 1 <= a < 1001: # a 입력값 조건이 만족하지 않을 시
        break # 종료 아니면 다음 루프로 넘어감
    elif not 10 <= b < 1001: # b 입력값 조건이 만족하지 않을 시
        break # 종료 아니면 다음 루프로 넘어감
    elif a > b or a == b: # 마찬가지로 해당 조건이 만족하지 않을 시
        break # 종료 아니면 다음 루프로 넘어감

    for i in range(a, b+1): # 입력 받은 값을 반복한다
        if i % 35 == 0: # 5와 7의 공배수가 맞으면
            print('FizzBuzz')   # 피즈버즈 출력
        elif i % 5 == 0: # 5의 배수이면
            print('Fizz') # 피즈 출력
        elif i % 7 == 0: # 7의 배수이면
            print('Buzz') # 버즈 출력
        else: # 그 외 값들
            print(i) # 출력
    if i == b: # 모든 반복을 마치면 
        print('모든 값을 출력함') # 해당 문자를 출력하고
        break # 프로그램을 종료

