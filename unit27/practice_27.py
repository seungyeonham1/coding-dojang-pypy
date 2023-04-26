
# 파일에 문자열 쓰기, 읽기
# 파일에 문자열을 쓸 때, 'open' 함수로 파일을 열어서 파일 객체(file object)를 얻은 뒤에 'write' 메서드를 사용합니다.

# 파일객체 = open(파일이름, 파일모드)
# 파일객체.write('문자열')
# 파일객체.close()

file = open('hello.txt', 'w') # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환(얻기)
file.write('Hello, world!') # 파일에 문자열 저장
file.close # 파일 객체 닫기

# 파일에 문자열 쓰는 과정
# 파일 열기 >> 파일 쓰기 >> 파일 닫기

# 파일에서 문자열 읽기
# 변수 = 파일객체.read()

file = open('hello.txt', 'r') # hello.txt 파일을 읽기 모드로 열기. 파일 객체 반환(얻기)
s = file.read() # 파일에서 문자열 읽기
print(s) # hello, world! 출력
file.close() # 파일 객체 닫기

# 파일에서 문자열 읽기 과정
# 파일 열기 >> 파일 읽기 >> 파일 닫기

# 자동으로 파일 객체 닫기
# 파이썬에서는 with as를 사용하면 파일을 사용한 뒤, 자동으로 객체를 닫아줌.
# with open(파이름이름, 파일모드) as 파일객체:
#    코드

# with open('hello.txt', 'r') as file: # hello.txt 파일을 읽기 모드(r)로 열기
#         s = file.read() # 파일에서 문자열 읽기
#         print(s) # hello, world!


# 문자열 여러 줄을 파일에 쓰기, 읽기

with open('hello.txt', 'w') as file:
    for i in range(3):
        file.write('Hello,world! {0}\n'.format(i)) # 문자열 끝에 개행 문자 \n를 지정해주어야 줄바꿈이 됨.

# 리스트에 들어있는 문자열을 파일에 쓰기
# 파일객체.writelines(문자열리스트)

lines = ['안녕하세요.\n', '감사해요.\n', '잘 있어요.\n', '다시 만나요.\n']

with open('hello.txt', 'w') as file: # hello.txt 파일을 쓰기 모드로 열기
    file.writelines(lines)


# 파일의 내용을 한 줄씩 리스트로 가져오기
# 변수 = 파일객체.readlines()

with open('hello.txt', 'r') as file:
    line = None # 변수 line을 None으로 초기화
    while line != '':
        line = file.readline()
        print(line.strip('\n')) # 파일에서 읽어온 문자열에서 \n 삭제하여 출력 


# for 반복문으로 파일의 내용을 줄 단위로 읽기

with open('hello.txt', 'r') as file:
    for line in file: # for에 파일 객체를 지정하여
        # 파일의 내용을 한 줄씩 읽어서 변수에 저장
        print(line.strip('\n')) # 파일에서 읽어온 문자열에서 \n을 삭제하여 출력


# 파일 객체는 이터레이터
# 변수 여러 개에 저장하는 언패킹도 가능함
# file = open('hello.txt', 'r')
# a, b, c = file
# a, b, c
# a, b, c = file과 같이 사용하기 위해선 hello.txt에 문자열 3줄이 들어있어야 함.
# 할당할 변수의 개수와 파일에 저장된 문자열의 줄 수가 일치해야 함.


# 파이썬 객체를 파일에 저장하기, 가져오기
# 파일에 저장하는 pickle 모듈, 파일에 저장하는 과정을 피클링(pickling)
# 파일에서 객체를 읽어오는 과정을 언피클링(unpickling)

# 파이썬 객체를 파일에 저장하기
# 피클링은 pickle 모듈의 dump 메서드를 사용함



# 파이썬 객체를 파일에 저장하기

import pickle

name = '미누킴'
age = 33
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'japanese' : 80, 'english': 85, 'chinese': 75}

with open('미누킴.p', 'wb') as file: #미누킴.p 파일을 바이너리 쓰기 모드(wb)로 열기  'b'는 바이너리의 약자
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

# 파일에서 파이썬 객체 읽기

import pickle

name = '미누킴'
age = 33
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'japanese' : 80, 'english': 85, 'chinese': 75}

with open('미누킴.p', 'rb') as file: #미누킴.p 파일을 바이너리 쓰기 모드(wb)로 열기  'b'는 바이너리의 약자
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)


# 파일 모드는 조합에 따라 여러 종류가 있음
# 읽기 'r'
# 쓰기 'w'
# 추가 'a': 이미 있는 파일에서 끝에 새로운 내용을 추가할 때 사용
# 배타적 생성 'x': 파일이 이미 있으면 에러(FileExistsError)를 발생시키고 없으면 파일을 만듬. 'x'는 exclusive creation의 x를 뜻함

# 파일 형식도 함께 지정할 수 있음
# 텍스트 모드 't'
# 바이너리 모드 'b'

# 'rt', 'wt': 읽기와 쓰기 모드를 조합한 텍스트 모드
# 'rb', 'wb': 바이너리 모드, 피클링을 사용하여 바이너리 데이터를 직접 저장할 때 사용함.

# '+': 파일을 읽기/쓰기 모드로 염. 
# 'r+t', 'w+t', 'w+', 'r+b', 'w+b' 등으로 조합할 수 있음