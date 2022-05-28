hello = 'hello world!'
print(hello) # 문자열을 변수에 저장하고, 변수를 호출하여 문자열 출력

hello2 = "java world!" #문자열을 변수에 저장하고, 변수를 호출하여 문자열 출력, 큰 따옴표로 생성, 이 경우 작은 따옴표와 완전히 동일하게 작동
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


def add(value1, value2):
    '''\
이 함수는 매개변수 value1과 value2를 더한 값은 return하는 함수입니다.\
'''
    result = value1 + value2
    return result
help(add)