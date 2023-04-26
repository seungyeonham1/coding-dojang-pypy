

# 표준 입력으로 양의 정수 2개가 입력됨

a1, b1 = map(int,input().split())

# 공약수를 세트 형태로 구하도록 만드세요. 단, 최종 결과는 공약수의 합으로 판단됨


# 입력값 범위 설정 + a 나머지가 0인 경우
# 입력값 범위 설정 + b 나머지가 0인 경우

a = {i for i in range(1, a1+1) if a1 % i == 0} # 첫 번째 입력값 a1의 약수 세트 
b = {i for i in range(1, b1+1) if b1 % i == 0} # 두 번째 입력값 b1의 약수 세트

#print(a) # 공약수 a 출력 
#print(b) # 공약수 b 출력

divisor = a & b  # a와 b의 공약수

result = 0

if type(divisor) == set: # 공약수 타입이 세트 형식이면
    result = sum(divisor) # 공약수의 합을 구한다

print(result) # 공약수의 합을 출력한다.