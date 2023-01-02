# 파이썬의 숫자 자료형에는 int, float, complex
# 정수는 10진수 이외에도 2, 8, 16진수로도 표현할 수 있음

# a = 10
# b = 1.5

# print(type(a))
# print(type(b))

print(1+1)
print(1-2)
print(3*3)
print(11/3) # 소수점을 버리지 않는 나눗셈. 결과 값은 float
print(11//3) # 소수점을 버리는 나눗셈. 결과 값은 무조건 int

print(15%6) # 나눗셈 이후, 나머지를 구하는 연산자
print(2**5) # 2의 5승, 거듭제곱 연산자
 

print(int(3.3))
print(int(5/2)) 


quotient, remainder = divmod(5, 2) # 5를 2로 나눴을 때 나오는 몫과 나머지를 의미한다
# divmod = 몫과 나머지를 구하는 함수
print(quotient, remainder) # 몫과 나머지를 출력한다 (결과는 몫2 나머지1이 출력될 것)


