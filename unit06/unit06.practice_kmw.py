# x = 10  # 10이 들어있는 변수 x
# 변수 이름은 영문과 숫자를 주로 사용함
# 변수는 숫자뿐만 아니라 문자열도 넣을 수 있음
# y = 'Hello, world!' # Hello, world! 라는 문자열을 변수 y에 할당

# print(y)

# type로 변수의 자료형 확인하기
# x = 10, y = 'Hello, world!'
# type(x) = x에는 10이라는 정수가 들어있으므로 int
# type(y) = y에는 Hello, world! 라는 문자열이 들어있으므로 str
# print(x)
# print(type(x))
# print(type(y))

# 변수는 여러 개를 선언할 수 있는데, 선언한 갯수와 값이 동일해야한다.
# x, y, z = 10, 20, 30

# 변수 삭제는 del을 사용한다
# x = 10
# del x  #  변수 x를 삭제한다

# 빈 변수 만들기
# 빈 변수를 만들 때는 None을 할당해준다.
# None은 값 자체가 없음을 의미한다. C나 C++의 Null과 같음

# 산술 연산, 할당 연산자 사용
# a = 10  # a에 10을 할당한다
# b = 20  # b에 20을 할당한다
# a += 20 # a는 a에 20을 더한 값을 할당한다.
# print(a+b) # a + b를 더한 값을 출력한다.


# a = input('첫 번째 숫자를 입력하세요: ') 
# b = input('두 번째 숫자를 입력하세요: ') # a 값을 10, b 값을 20 넣었을 경우 30이 나오게 해야한다

# print(a + b) # 하지만 실제 결과값은 1020으로 나오게된다. 그 이유는 input type가 Str, 즉 문자열이기 때문에 두 스트링을 이어서 출력한다.
# print(type(a + b))


# input 함수
# input은 사용자가 입력한 값을 가져오는 함수

# input_number1 = int(input())
# input_number2 = int(input())

# print(input_number1+input_number2)



# map을 사용하여 정수로 변환하기
# a, b = map(int, input().split())
# print(a+b)


# a = float(input('첫 번째 숫자 입력: '))
# b = float(input('두 번째 숫자 입력: '))

# print(a + b)

# 입력 값을 변수 두 개에 저장하기 = split()
# ex) a, b = input().split()

a, b = input('문자열 두 개를 입력하세요: ').split()

print(a) # a에 입력된 값을 출력
print(b) # b에 입력된 값을 출력


