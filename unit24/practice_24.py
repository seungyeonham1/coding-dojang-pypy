
# # 리스트 = 요소 여러개가 이어져 있는 것 
# # 문자열 = 문자 여러개가 이어져 있는 것 = 시퀀스 자료형

# # 문자열 바꾸기  = replace('바꿀문자열', '새문자열')

# # a = 'Hello, world!'.replace('world', 'Python') # 'world'를 'Python'으로 바꾼다
# # print(a)

# # # 문자 바꾸기
# # # str.maketrans('바꿀문자','새문자') 변환 테이블을 만든 뒤, translate(테이블)을 사용

# # table = str.maketrans('aeiou', '12345') # a는 1, e는 2, i는 3, o는 4, u는 5
# # print('apple'.translate(table))

# # # 문자열 분리하기
# # # split()는 공백을 기준으로 문자열을 분리하여 리스트로 만듬

# # a = 'apple pear grape pineapple orange'.split() # 공백을 기준으로 문자열을 분리함  
# # print(a)


# # b = 'apple, pear, grape, pineapple, orange'.split(', ') # split('기준문자열')과 같이 기준 문자열을 지정하면 기준 문자열로 문자열을 분리
# # print(b) 

# # 구분자 문자열과 문자열 리스트 연결하기
# # join(리스트) 구분자 문자열과 문자열 리스트의 요소를 연결하여 문자열로 만듬

# #c = ' '.join(['apple', 'pear', 'grape', 'orange', 'pineapple'])
# #print(c)

# #d = '+'.join(['apple', 'pear', 'grape', 'orange', 'pineapple'])
# #print(d)

# # 소문자를 대문자로 바꾸기
# # upper()

# #a = 'python'.upper()
# #print(a)

# # 대문자를 소문자로 바꾸기
# # lower()

# #b = 'PYTHON'.lower()
# #print(b)

# # 왼쪽 공백 삭제하기
# # lstrip()

# # 오른쪽 공백 삭제하기
# # rstrip()

# # 양쪽 공백 삭제하기
# # strip()

# #a = '      Python       '
# #print(a.lstrip())
# #print(a.rstrip())
# #print(a.strip())

# # 왼쪽의 특정 문자 삭제하기
# # lstrip('삭제할문자들')

# # a = ', python.'.lstrip(',.')
# # print(a)
# # b = ', python.'.rstrip(',.')
# # print(b)
# # c = ', python.'.strip(',.')
# # print(c)

# # # 구두점을 간단하게 삭제하기
# # # strip 메서드에 string.punctuation 넣기

# # import string
# # a = ', python.'.strip(string.punctuation)
# # b = ', python.'.strip(string.punctuation + ' ') # 공백까지 삭제하고 싶다면 공백 ' ' 연결
# # c = ', python.'.strip(string.punctuation).strip() # 메서드 체이닝 활용
# # print(a)
# # print(b)
# # print(c)

# # 문자열 왼쪽 정렬
# # ljust(길이)

# # a = 'python'.ljust(10) # 문자열을 10의 길이에 맞춘다. (python (6) + 공백 4칸 = 10)
# # print(a)

# # 문자열 오른쪽 정렬
# # rjust(길이)

# # a = 'python'.rjust(10)
# # print(a)

# # 문자열 가운데 정렬
# # a = 'python'.center(11) # 왼쪽 공백 3칸  python 6칸 오른쪽 공백 2칸
# # print(a)

# # 메서드 체이닝
# # 문자열 메서드는 처리한 결과를 반환하도록 만들어져 있지만, 메서드 체이닝을 통해 메서드를 계속 연결하여 호출할 수 있음
# # 메서드를 줄줄이 연결한다는 뜻
# # 문자열 입력받을 때 사용하던 input().split() 또한 메서드 체이닝이다.

# # a = 'python'.rjust(10).upper() #오른쪽 정렬 메서드와 소문자를 대문자로 바꿔주는 메서드가 연결됨
# # print(a)

# # # 문자열 왼쪽에 0 채우기
# # # zfill(길이)  zero fill을 의미하며 왼쪽에 0을 채운다

# # a = '만두'.zfill(4)
# # print(a)

# # b = 'pYthon'.zfill(10).lower()
# # print(b)

# # # 문자열 위치 찾기
# # # find('찾을문자열') 
# # # 특정 문자열을 찾아서 인덱스를 반환하고, 문자열이 없다면 -1을 반환한다.
# # # 같은 문자열이 여러 개일 경우, 처음 찾은 문자열 인덱스를 반환한다.

# # a = 'apple pineapple'.find('pl')
# # print(a)
# # b = 'apple pineapple'.find('xy')
# # print(b)


# # # 오른쪽부터 문자열 위치 찾기
# # # rfind('찾을문자열')

# # a = 'apple pineapple'.rfind('pl')
# # print(a)
# # b = '위아더원위아더원'.rfind('위아')
# # print(b)

# # 문자열 찾기
# # index, rindex로 문자열의 위치를 찾을 수 있음 
# # index('찾을문자열') => 왼쪽에서부터 특정 문자열을 찾아서 인덱스를 반환함

# a = 'apple pineapple'.index('pl')
# print(a)

# # 오른쪽 문자열 찾기

# a = 'apple pineapple'.rindex('pl')
# print(a)

# 문자열 개수 세기
# # count('문자열')
# a = 'apple pineapple'.count('pl')
# print(a)

# 문자열 서식 지정자와 포매팅 사용하기
# 문자열 안에서 특정 부분을 원하는 값으로 바꿀 때, 서식 지정자 또는 문자열 포매팅을 사용함
# ex ) 제임스 평균 점수는 ~~ 입니다.  마리아의 평균 점수는 ~~입니다. 이 때, '의 평균 점수는' 과 '점입니다.'은 같고 점수만 다를때

# 서식 지정자로 문자열 넣기
# '%s' % 문자열
# '%s' 는 문자열 이라는 뜻이며, s는 String의 앞자리 s를 의미
# a = 'I am %s. ' % 'james'
# print(a)

# name = 'Maria'
# b = 'I am %s. ' %name
# print(b)

# # 서식 지정자로 숫자 넣기
# # '%d' % 숫자
# # '%d'는 Decimal integer의 앞자리 d를 의미
# c = 'I am %d years old. ' % 20 
# print(c)

# # 서식 지정자로 소수점 표현
# # '%f' % 숫자
# d = '%f' % 2.3 
# print(d)

# # 소수점 이하 자릿수를 지정하기 위해선
# #%.자릿수f' % 숫자
# e = '%.2f' % 2.3
# f = '%.3f' % 2.3 
# print(e)
# print(f)

# 서식 지정자로 문자열 정렬하기
# %길이s

# a = '%10s' % ' python'
# print(a)  # 문자열 10 길이의 지정되며, 남는 공간은 공백으로 채움

# 자릿수가 다른 숫자 출력
# %길이d
# %길이'.자릿수f

# a = '%10d' % 150 
# b = '%10d' % 15000

# print(a)
# print(b)

# c = '%10.2f' % 2.3
# d = '%10.2f' % 2000.3
# print(c)
# print(d)

# # 문자열 왼쪽 정렬
# # '-길이s'

# e = '%-10s' % 'python'
# print(e)

# # 서식 지정자로 문자열 안에 값 여러개 넣기
# # '%d %s' % (숫자, "문자열")

# a = 'Today is %d %s. ' % (3, 'April')
# print(a)


# # format 메서드 사용
# # 문자열 포매팅 =  '{인덱스}'.format(값)

# a = 'Hello, {0}'.format('world!')
# b = 'Hello, {0}'.format(100)

# print(a)
# print(b)

# # format 메서드로 값 여러개 넣기
# a = 'Hello, {0} {2} {1}'.format('Python', 'Script', 3.6)
# print(a)

# # format 메서드로 같은 값을 여러개 넣기
# a = '{0} {0} {1} {1}'.format('Python', 'Script')
# print(a)

# format 메서드에서 인덱스 생략하기
# 인덱스를 생략하면 format에 지정한 순서대로 값이 들어가짐
# a = 'Hello, {} {} {}'.format('apple', 'banana', 'orange')
# print(a)

# # format 메서드에서 인덱스 대신 이름 지정하기
# a = 'Hello, {language} {version}'.format(language='Python', version=3.6)
# print(a)

# # 문자열 포매팅에 변수를 그대로 넣기
# language = 'C#'
# version = 3.6
# f'Hello, {language} {version}'

# print(f'Hello, {language} {version}')


# 중괄호 출력
#{} 중괄호 자체를 출력할 때는 {{, }} 처럼 중괄호를 2번 사용
a = '{{ {0} }}'.format('Python')
print(a)
# format 메소드로 문자열 정렬하기
# '{인덱스:<길이}'.format(값) # 왼쪽 정렬
# '{인덱스:>길이}'.format(값) # 오른쪽 정렬
# '{:>길이}'.format(값) # 인덱스를 사용하지 않는다면 콜론(:)과 정렬 방법으로만 지정해도 됨
a = '{0:<10}'.format('python')
print(a) # 왼쪽로 정렬한 길이 10 출력 (나머지 4칸은 공백)

# 숫자 개수 맞추기
# '%0개수d' % 숫자
# %d는 %와 d 사이에 0과 숫자 개술르 넣어주면 자릿수에 맞춰서 앞에 0이 들어감
# '{인덱스:0개수d'}.format(숫자)

a = '%03d' % 1
print(a)

a = '{0:03d}'.format(35)
print(a)

# '%0개수.자릿수F' % 숫자
# '{인덱스:0개수.자릿수f'}.format(숫자)


# 실수 숫자갯수 맞추기 
# 실수는 숫자 개수에 정수, 소수점, 소수점 이하 자릿수가 모두 포함됨
a = '%08.2f' % 3.6
print(a)

a = '{0:08.2f}'.format(150.37)
print(a)

# 채우기와 정렬을 조합해서 사용
# '{인덱스:[[채우기]정렬][길이][.자릿수][자료형]}'

a = '{0:0<10}'.format(15)
print(a) # 길이가 10으로 만든뒤, 왼쪽으로 정렬하고 남는 공간을 0으로 채운다

a = '{0:0>10}'.format(15)
print(a)

# 실수형
a = '{0:0>10.2f}'.format(15)
print(a) # 길이를 10으로 만든뒤, 오른쪽으로 정렬하고 소수점 자릿수는 2자리다

a = '{0: >10}'.format(15) # 남는 공간을 공백으로 채움
b = '{0:>10}'.format(15) # 채우기 부분을 생략하면 공백이 들어감
c = '{0:x>10}'.format(15) #남는 공간을 문자 x로 채움

print(a)
print(b)
print(c)

# 금액에서 천단위로 콤마 찍기
# format(숫자, ',')
# format(1493500, ',')


a = 'Hello, ' '%s 3.6' % 'Python'
print(a)