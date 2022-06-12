hello = 'hello world!'
print(hello) # 문자열을 변수에 저장하고, 변수를 호출해서 문자열을 출력하기.

hello1 = "hello world!"
print(hello1) # 문자열을 변수에 저장하고, 변수를 호출해서 문자열을 출력하기. 큰따옴표로 생성. 이 경우 작은따옴표와 완전히 동일하게 동작한다.

hello2 = "'hello' 'world!'"
print(hello2) # 문자열을 변수에 저장하고, 변수를 호출해서 문자열을 출력하기. 작은 따옴표를 스트링으로 사용하고 싶은 경우, 큰따옴표 안에 작은따옴표를 넣어서 출력하면 원하는 대로 출력할 수 있다.

hello3 = '"hello" "world!"'
print(hello3) # 문자열을 변수에 저장하고, 변수를 호출해서 문자열을 출력하기. 큰 따옴표를 스트링으로 사용하고 싶은 경우, 작은따옴표 안에 큰따옴표를 넣어서 출력하면 원하는 대로 출력할 수 있다.

# 아래부터는 독스트링. 사실 좀 중요함
hello_dock = \
'''\
hello world
pypypypypy
hello world
sdfsdfdsf
sdfsdfdsfds
sdfsdfsdfs
sdfsdfsdfs\
'''

print(hello_dock)

def add(value1, value2):
    '''\
이 함수는 매개변수 value1과 value2를 더한 값을 return하는 함수입니다.\
'''
    result = value1 + value2
    return result

help(add)


s1 = "'Python' "
s2 = '''is a "programming language"
that lets you work quickly
and
integrate systems more effectively.'''

s = s1 + s2
print(s)