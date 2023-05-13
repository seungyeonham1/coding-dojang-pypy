

# 정규표현식: 일정한 규칙(패턴)을 가진 문자열을 표현하는 방법
# 복잡한 문자열 속에서 특정한 규칙으로 된 문자열을 검색한 뒤 추출하거나 바꿀 때 사용함.
# 문자열이 정해진 규칙에 맞는지 판단할 때도 사용함
# re 모듈을 가져와서 사용함
# 특정 문자열이 맨 앞에 오는지 맨 뒤에 오는지 판단할 수 있음


# 문자열 판단하기
# re.match('패턴', '문자열')

import re
print(re.match('Hello', 'Hello, world!'))
print(re.match('Python', 'Hello, world!'))


# 문자열이 맨 앞에 오는지 맨 뒤에 오는지 판단
# 앞: ^문자열
# 뒤: 문자열$
# re.search('패턴', '문자열') # match 함수는 문자열 처음부터 매칭되는지 판단 <> search는 문자열 일부분이 매칭되는지 판단함

print(re.search('^Hello', 'Hello, world!'))
print(re.search('world!$', 'Hello, world!'))


# 지정된 문자열이 하나라도 포함되는지 판단
# 문자열|문자열 # '|'는 OR 연산자의 기본 개념과 같음
# 문자열|문자열|문자열|문자열

print(re.match('hello|world', 'hello'))


# 범위 판단하기
# 문자열이 숫자로 되어있는지 판단 
# [0-9]*  # *는 문자(숫자)가 '0개 이상' 있는지 판단
# [0-9]+  # +는 문자(숫자)가 '1개 이상' 있는지 판단

print(re.match('[0-9]*', '1234'))
print(re.match('[0-9]+', '1234'))
print(re.match('[0-9]+', 'abcd'))

print(re.match('a*b', 'b'))
print(re.match('a+b', 'b'))
print(re.match('a*b', 'aab'))
print(re.match('a+b', 'aab'))


# 문자가 한 개만 있는지 판단하기
# 문자?  # ?는 ? 앞의 문자(범위)가 0개 또는 1개인지 판단
# [0-9]? 
# . # .는 .이 있는 위치에 아무 문자(숫자)가 1개 있는지 판단

print(re.match('abc?d', 'abd'))
print(re.match('ab[0-9]?c', 'ab3c'))
print(re.match('ab.d', 'abxd'))


# 문자 개수 판단하기
# 문자{개수}
# (문자열){개수}
# [0-9]{개수}
# (문자){시작개수,끝개수}
# (문자열){시작개수,끝개수}
# [0-9]{시작개수,끝개수}

print(re.match('h{3}', 'hhhello'))
print(re.match('(hello){3}', 'hellohellohelloworld'))
print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1000-1000'))
print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1000-100'))
print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-100-1000'))
print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-10-1000'))


# 숫자와 영문 문자를 조합해서 판단
# a-z
# A-Z

print(re.match('[a-zA-Z0-9]+', 'Hello1234'))
print(re.match('[A-Z0-9]+', 'hello'))

# 한글 판단
# 가-힣
print(re.match('[가-힣]+', '홍길동'))


# 특정 문자 범위에 포함되지 않았는지 판단
# [^범위]*
# [^범위]+

print(re.match('[^A-Z]+', 'Hello'))  # 대문자를 제외한 모든 문자(숫자)가 1개 이상 있는지 판단
print(re.match('[^A-Z]+', 'hello'))


# 특정 문자 범위로 시작할 때
# ^[범위]*
# ^[범위]+

print(re.search('^[A-Z]+', 'Hello'))

# 특정 문자 범위로 끝나는지 확인 
# [범위]*$
# [범위]+$

print(re.search('[0-9]+$', 'Hello1234'))


# 특수 문자 판단하기
# \특수문자
# \d: [0-9]와 같음, 모든 숫자
# \D: [^0-9]와 같음, 숫자를 제외한 모든 문자
# \w: [a-zA-Z0-9_]와 같음, 영문 대소문자, 숫자, 밑줄 문자
# \W: [^a-zA-Z0-9_]와 같음, 영문 대소문자, 숫자, 밑줄 문자를 제외한 모든 문자


print(re.search('\*+', '1 ** 2'))
print(re.search('[$()a-zA-z0-9]+', '$(document)'))
print(re.match('\d+', '1234'))
print(re.match('\D+', 'Hello'))
print(re.match('\w+', 'Hello_1234'))
print(re.match('\W+', '(:)'))


# 공백 처리하기
# \s: [\t\n\r\f\v]와 같음. 공백(스페이스), \t(탭), \n(새 줄, 라인 피드), \r(캐리지 리턴), \f(폼피드), \v(수직 탭)
# \S: [^\t\n\r\f\v]와 같음. 공백을 제외하고 \t, \n, \r, \f, \v만 포함

print(re.match('[a-zA-Z0-9 ]+', 'Hello 1234'))
print(re.match('[a-zA-Z0-9\s]+', 'Hello 1234'))
print(re.match('[a-zA-Z0-9\S]+', 'Hello 1234'))


# 같은 정규표현식 패턴을 자주 사용할 때
# compile 함수를 사용하여 정규표현식 패턴을 객체로 만든 뒤 match 또는 search 메서드를 호출하면 됨
# 객체 = re.compile('패턴')
# 객체.match('문자열')
# 객체.search('문자열')

# p = re.compile('[0-9]+')
# p.match('1234'))
# p.search('hello'))


# 그룹 사용하기
# 그룹은 해당 그룹과 일치하는 문자열을 얻어올 때 사용함.
# (정규표현식)(정규표현식)
# 매치객체.group(그룹숫자)

# m = re.match('([0-9]+) ([0-9]+)', '10 295')
# m.group(1) # 첫 번째 그룹에 매칭된 문자열을 반환 '10'
# m.group(2) # 두 번째 그룹에 매칭된 문자열을 반환 '295'
# m.group() # 매칭된 문자열 한꺼번에 반환 '10 295'
# m.group(0) # 매칭된 문자열을 한꺼번에 반환 '10 295'


# 매치객체.groups() # 그룹 메서드는 각 그룹에 해당하는 문자열을 튜플로 반환함
# m.groups() # ('10', '295')


# 그룹 개수가 많아지면 숫자로 그룹을 구분하기 어려움. 그룹에 이름을 지으면 편해진다.
# (?P<이름>정규표현식)

# 매치객체.group('그룹이름')

m = re.match('(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)', 'print(1234)')
m.group('func') # 그룹 이름으로 매칭된 문자열 출력  'print'
m.group('arg') # 그룹 이름으로 매칭된 문자열 출력 '1234'



# 패턴에 매칭되는 모든 문자열 가져오기
# findall 함수를 사용하여 매칭된 문자열을 리스트로 변환
# re.findall('패턴', '문자열')

print(re.findall('[0-9]+', '1 2 Fizz 4 Buzz Fizz 7 8'))



# *, + 그룹 활용하기
# 정규표현식에서 +와 *를 조합하여 사용할 때는 그룹으로 묶어서 사용함.
# 규칙은 반드시 지켜야 하지만 있어도 되고 없어도 되는 상황에 사용
# ex) (.[a-z]+)* 는 점과 영문 소문자가 1개 이상 있는지 판단하고, 이것 자체가 0개 이상인지 판단

print(re.match('[a-z]+(.[a-z]+)*$', 'hello world'))
print(re.match('[a-z]+(.[a-z]+)*$', 'hello.1234'))
print(re.match('[a-z]+(.[a-z]+)*$', 'hello'))


# 문자열 바꾸기
# 정규표현식으로 특정 문자열을 찾은 뒤 다른 문자열로 바꾸는 방법
# 문자열을 바꿀 때는 'sub 함수'를 사용함
# re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)

print(re.sub('apple|orange', 'fruit', 'apple box orange tree')) # apple 또는 orange를 fruit로 바꿈
print(re.sub('[0-9]+', 'n', '1 2 Fizz 4 Buzz Fizz 7 8')) # 숫자만 찾아서 n으로 바꿈


# sub 함수는 바꿀 문자열 대신 교체 함수를 지정할 수도 있음
# 교체함수(매치객체)
# re.sub('패턴', 교체함수, '문자열', 바꿀횟수)

def multiple10(m): # 매개변수로 매치 개겣를 받음
    n = int(m.group()) # 매칭된 문자열을 가져와서 정수로 변환 
    return str(n * 10) # 숫자에 10을 곱한 뒤 문자열로 변환해서 반환

print(re.sub('[0-9]+', multiple10, '1 2 Fizz 4 Buzz Fizz 7 8'))

# 교체 함수 내용이 간단하면 람다 표현식으로 만들어서 넣어도 됨
# re.sub('[0-9]+', lambda m: str(int(m.group())* 10), '1 2 Fizz 4 Buzz Fizz 7 8')


# 찾은 문자열을 결과에 다시 사용하기
# \\숫자

print(re.sub('([a-z]+) ([0-9]+)', '\\2 \\1 \\2 \\1', 'hello 1234'))

print(re.sub('({\s*)"(\w+)":\s*"(\w+)"(\s*})', '<\\2>\\3</\\2>', '{ "name": "james" }'))
# ({\s*)은 {와 공백을 찾으므로 '{ '를 찾음. 마지막 (\s*})는 공백과 }를 찾으므로 ' }'를 찾음.
# "(\w+)":\s*"(\w+)"는 :을 기준으로 양 옆의 name과 jame를 찾음
# 바꿀 문자열은 '<\\2>와 같이 그룹 2 name과 그룹 3 james만 사용하고 그룹 1 '{ ', 그룹 4 '} '는 버림

# 그룹에 이름을 지은 경우
# \\g<이름>
# \\g<숫자>

print(re.sub('({\s*)"(?P<key>\w+)":\s*"(?P<value>\w+)"(\s*})', 
             '<\\g<key>>\\g<value></\\g<key>>', 
             '{ "name": "james" }'))



# raw 문자열 사용하기
# 정규표현식의 특수 문자를 판단하려면 '\'를 붙여야함
# 여기서 문자열 앞에 r을 붙여주면 원시 문자열이 되어 '\'를 붙이지 않아도 특수 문자를 그대로 판단할 수 있음
# r'\숫자 \g<이름> \g<숫자>'

print(re.sub('({\s*)"(\w+)":\s*"(\w+)"(\s*})', r'<\2>\3</\2>', '{ "name": "james"}'))