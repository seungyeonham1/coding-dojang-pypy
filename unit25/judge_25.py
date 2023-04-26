
# 표준 입력으로 문자열 여러 개와 숫자 여러 개가 두줄로 입력

# 첫번째 줄은 키, 두번째 줄은 값으로 하여 딕셔너리를 생성

# 딕셔너리에서 키가 'delta'인 키-값 쌍과 값이 30인 키-값 쌍을 삭제하도록 만드세요

# 키-값 쌍 삭제 = pop 함수 or del 함수

key = input().split() # 여러 문자열을 입력
value = map(int,input().split()) # 여러 정수(숫자)를 입력

x = dict(zip(key, value)) # 키와 값을 묶은 딕셔너리를 생성
x.pop('delta') # 딕셔너리에 'delta' 키를 삭제
# del 함수를 쓰는 경우에는 del x['delta']
x = {key: value for key, value in x.items() if value != 30}
print(x)


# alpha bravo charlie delta echo foxtrot
# 10 20 30 40 50 60

