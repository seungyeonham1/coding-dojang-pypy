x = 10 # x는 10이라는 int값을 가지고 있는 변수가 되었다. 변수 이름은 특별히 제약은 없으나, 영문 문자와 숫자를 사용하는 것이 일반적이다.
x = 'abc' # x는 2번 라인부터는 10이라는 int값을 가지고 있는 변수가 아니라, 'abc' 라는 string값을 가지고 있는 변수가 되었다.

# 변수 이름은 일반적으로 아무거나 사용할 수 있지만, 파이썬에서 기본적으로 사용한다고 선언된 키워드들은 사용할 수 없다.
# 예시를 들자면, print, if, for, while, True, False, or, is, and.........
# 특수문자도 사용할 수 없지만, 예외적으로 언더바는 사용할 수 있다. a_result = a+10

print(x) # 변수에 접근하는 방법은 그냥 변수를 그대로 매개변수로 사용하면 된다.
print(type(x))

# a, b, c, d = 10, 20, 'aa', 40
# print(a,b,c,d)

# a_none = None
# print(a_none) # 빈 변수 만들기. None은 C++에서의 NULL과 같다. 값 자체가 없음을 지칭


# print(a + b) # 변수로 계산하기. 사칙연산을 지원하고, 파이썬의 기본적인 연산자를 전부 사용할 수 있다.

# a = 10
# a += 20 # 산술 연산 후 할당 연상자 사용하기. 여기서는 a에 20을 더하고 다시 그 결과를 a에 저장한다. 결론적으로, a는 30이 된다.
# print(a)

# input_wait = '문자열을 입력하세요> '
# input_a = input(input_wait) # input 함수는 유저의 표준 입력을 받는 함수다. 매번 유저의 입력에 따라서 값이 바뀌기 때문에 닉네임이나 나이, 성별 정보 같은걸 유저에게 받을때 종종 사용한다.
# print('입력결과:', input_a)
# # input 함수의 매개변수에는 str을 넣을 수 있다. input 대기중에 안내 str을 표시하는 기능을 제공한다. 여기에는 변수도 넣을 수 있음.

# input_number1 = input()
# input_number2 = input()

# print(input_number1+input_number2)
# # print('10'+'20')
# # 왜냐면, input 함수의 결과값은 항상 str타입의 값만을 반환하기 때문에 이렇게 동작한다. str끼리 + 연산자를 사용하는 경우 두 스트링을 그대로 이어서 출력한다.

# print(int(input_number1)+int(input_number2))
# # print(10+20)
# # input 함수의 결과값을 int로 바꿔서 연산함. 물론, 이 방법도 유효하지만, int(input())과 같은 형태로 input 자체를 int로 받는 방법도 유효하다.

# a,b = input().split(',')
# # split 메서드를 사용하면, 변수 여러개에 여러 값을 동시에 할당할 수 있다. split 메서드 내의 매게변수에는 해당 스트링 기준으로 input 값을 쪼개는 것을 선언한다.
# # 예시를 들자면, ',' 인 경우, 30, 40, 50, 60을 콤마를 기준으로 4개의 값으로 쪼갠다.

# a = int(a)
# b = int(b)

# print(a+b)
# print(type(a))

a,b = map(int, input().split())
print(a+b)