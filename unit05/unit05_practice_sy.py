# 파이썬의 숫자 자료형에는 int, float, complex가 있는데, complex의 경우에는 QA에서 사용하는 수준에서는 거의 사용되지 않는다. 사용되는 경우엔 보통 NUMPY를 같이 사용한다.

# a = 10
# b = 1.5
# print(type(a))
# print(type(b))

print(1+1)
print(1-2)
print(3*3)
print(4/4) # 소수점을 버리지 않는 나눗셈. 딱 맞아떨어지더라도 결과값은 무조건 float가 된다. 1.0, 2.0, 3.0...

print(5//4) # 소수점을 버리는 나눗셈. 결과값은 무조건 int가 된다.

print(5 % 2) # 나눗셈 후 몫이 아닌 나머지만을 구하는 연산자.
print(2 ** 10) # 거듭제곱.

print(int(3.3)) # int로 만들기.
print(int(5/2)) # 수식도 int로 만들수 있다.
print(int('102')) # 문자열도 int로 만들수 있는데, 숫자 형태의 문자열이 아닌 경우엔 ValueError를 뱉는다.

print(type(1))
print(type('1'))
print(type(1/1)) # type은 해당 객체의 자료형을 알수 있다.

a = (3 + 5) * 2 # 중등 수학과 동일하다. 괄호 안의 수식을 더 먼저 계산하며, 괄호 밖에서는 *나 /를 더 먼저 계산하고 +-를 더 나중에 계산한다.
