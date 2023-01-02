hello = 'hello world!'
print(hello) # 문자열을 변수에 저장하고, 변수를 호출하여 문자열 출력

hello2 = "java world!" # 문자열을 변수에 저장하고, 변수를 호출하여 문자열 출력, 큰 따옴표로 생성, 이 경우 작은 따옴표와 완전히 동일하게 작동
print(hello2)

hello3 = "'hello' 'world!'"
print(hello3)

hello4= '"hello" "world!"'
print(hello4)

#작은 따옴표, 큰 따옴표


#dock 스트링
hello_dock = \
'''hello world
pypypypypy
hello world'''

print(hello_dock)

single_quote = '''"안녕하세요."
'파이썬'입니다.'''

double_quote = """"Hello"
'Python'"""

double_quote2 = """Hello, 'Python'"""

print(single_quote)
print(double_quote)
print(double_quote2)


def add(value1, value2):
    '''\
이 함수는 매개변수 value1과 value2를 더한 값은 return하는 함수입니다.\
'''
    result = value1 + value2
    return result
help(add)

#문자열에 따옴표를 포함하는 다른 방법
#작은 따옴표 안에 작은 따옴표 넣기 = 작은 따옴표 앞에 역슬래시(\) 사용하기

s = 'Python isn\'t difficult' 
print(s)

#큰 따옴표도 사용 가능

s1 = "he said \"Python is easy\""
print(s1)

# 따옴표 세 개로 묶지 않고 여러 줄로 된 문자열 사용하기

print('Hello\nPython')
print('''Hello
Python''')