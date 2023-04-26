
# 위치 인수와 리스트 언패킹 사용하기

# 위치 인수란 ? 함수에 인수를 순서대로 넣는 방식을 말함
# ex) print(10, 20, 30) => 출력하면 10, 20, 30 순서대로 출력됨

# 위치 인수를 사용하는 함수를 만들고 호출하기

#def print_numbers(a, b, c):
#    print(a)
#    print(b)
#    print(c)

def print_numbers(a, b, c):
   print(a)
   print(b)
   print(c)
   
print_numbers(10, 20, 30)

# 언패킹 사용하기
# 인수를 순서대로 넣을 때 리스트나 튜플을 사용할 수 있음.
# 함수의 매개변수 개수와 리스트의 요소 개수는 같아야함

# 함수(*리스트)
# 함수(*튜플)


x = [10, 20, 30]
# 리스트(튜플) 앞에 *를 붙이면 언패킹이 됨 = 리스트의 포장을 푼다라는 뜻
print_numbers(*x)


# 가변 인수 함수 만들기
# 위치 인수와 리스트 언패킹은 가변 인수에 사용함.

# def 함수이름(*매개변수):
#     코드


def print_numbers(*args):
    for arg in args:
        print(arg)

# 숫자를 넣은 개수만큼 출력됨
print_numbers(10) # 1개 넣으면 1개
print_numbers(10, 20, 30, 40) # 4개 넣으면 4개가 출력됨

# 리스트(튜플) 언패킹으로 여러 숫자 출력
x = [50]
print_numbers(*x)

y = [50, 60, 70, 80]
print_numbers(*y)

# 고정 인수와 가변 인수를 함께 사용하기

# *args가 고정 매개변수보다 앞쪽에 오면 안됨. 반드시 매개변수 순서에서 가장 뒤쪽에 와야 함
def print_numbers(a,*args):
    print(a)
    print(args)

print_numbers(1)
print_numbers(1, 10, 20)
print_numbers(*[10, 20, 30])


# 키워드 인수 사용하기

def personal_info(name, age, address):
    print('이름: ',name)
    print('나이: ',age)
    print('주소: ',address)

# 아래와 같이 값만 사용하려면 인수의 순서를 기억해야함.
personal_info('가나다', 30, '경기도 판교')

# 인수의 순서가 달라지면 잘못된 결과가 출력되니, 순서와 용도를 매번 기억하지 않도록 키워드 인수라는 기능을 제공함.
# 함수(키워드=값)
# 아래와 같이 키워드 = 값을 사용하면 인수 순서에 관계없이 올바른 값이 출력됨
personal_info(name = '가나다', age = '30', address = '경기도 판교')
personal_info(age = '30', name = '가나다', address = '경기도 판교')
# print 함수에 사용했던 sep, end도 키워드 인수임.




# 키워드 인수와 딕셔너리 언패킹 사용하기
# 함수(**딕셔너리)

def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

# 딕셔너리 키워드(키)는 반드시 문자열 형태여야만 함
# 딕셔너리 언패킹을 사용할 때는 함수의 매개변수 이름과 딕셔너리의 키 이름이 같아야함
x = {'name': '홍길동', 'age': 30, 'address': '경기도 수원시'}
personal_info(**x)
# 딕셔너리 변수 대신 딕셔너리 앞에 바로 **를 붙여도 똑같이 동작함
personal_info(**{'name': '홍길동', 'age': 30, 'address': '경기도 수원시'})

# 딕셔너리에 **를 2번 사용하는 이유? 딕셔너리는 키-값 쌍 형태로 값이 저장되어 있음. 두 번 언패킹하면 값을 사용하도록 만듦

x = {'name': '홍범도', 'age': 31, 'address': '경기도 화성시'}
personal_info(*x) # 한 번만 넣으면 x의 키가 출력되는데, 이는 키를 사용한다라는 뜻이 됨
personal_info(**x) # 두 번 언패킹하여 값을 사용하도록 만듬



# 키워드 인수를 사용하는 가변 인수 함수 만들기
# def 함수이름 (**매개변수):
#     코드

def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')


# 인수를 직접 넣음
personal_info(name = '홍길동')
personal_info(name = '홍길동', age = 30, address = '경기도 수원시 원천동')

# 딕셔너리 언패킹 
x = {'name': '홍길동'}
personal_info(**x)

y = {'name': '나데시코', 'age': 17, 'address': '경기도 분당시'}
personal_info(**y)


# 함수를 만들 때, 매개변수에 **를 붙여주면 키워드 인수를 사용하는 가변 인수 함수를 만들 수 있음.
# **kwargs를 사용한 가변 인수 함수는 함수 안에서 특정 키가 있는지 확인한 뒤 해당 기능을 만듬

def personal_info(**kwargs):
    if 'name' in kwargs: # in으로 딕셔너리 안에 특정 키가 있는지 확인
        print('이름 : ', kwargs['name'])
    if 'age' in kwargs:
        print('나이 : ', kwargs['age'])
    if 'address' in kwargs:
        print('주소 : ', kwargs['address'])


# 고정 인수와 가변 인수(키워드 인수)를 함께 사용하기
# 고정 매개변수를 먼저 지정하고, 그다음 매개변수에 **를 붙여주면 됨

def personal_info(name, **kwargs):
    print(name)
    print(kwargs)

personal_info('페이커')
personal_info('페이커', age = 25, address = '서울특별시 강남구')
personal_info(**{'name': '페이커', 'age': 25, 'address': '서울특별시 강남구'})


# 위치 인수와 키워드 인수를 함께 사용하기
# 함수에서 위치 인수를 받는 *args, 키워드 인수를 받는 **kwargs를 함께 사용할 수 있음
# 대표적인 함수가 print


def custom_print(*args, **kwargs):
    print(*args, **kwargs)

custom_print(1, 2, 3, sep = ':', end='')


# 매개변수에 초깃값 정하기
# def 함수이름(매개변수 = 값):
#     코드

def personal_info(name, age, address = '비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

# 주소 값을 넣지 않으면 초기 값을 설정해둔 '비공개' 값이 출력됨
personal_info('이만기', 35)
# 주소 값을 설정했기 때문에 입력된 주소값이 출력됨
personal_info('이만기', 35, '인천광역시 남구')


# 초깃값이 지정된 매개변수의 위치
# def personal_info(name, address = '비공개', age): # 문법 에러 발생


# 초깃값이 지정된 매개변수는 뒤쪽에 몰아줄 것
def personal_info(name, age, address = '비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

def personal_info(name, age = 0, address = '비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

def personal_info(name = '비공개', age = 0, address = '비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
 
