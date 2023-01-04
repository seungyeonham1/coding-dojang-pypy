# 딕셔너리 = {키1: 값1, 키2: 값2}

# 키 값 이름이 서로 중복인 경우 = 가장 뒤에 있는 값만 사용

# 키는 정수, 실수, 불, 자료형을 섞어서 사용이 가능함
# 키는 리스트와 딕셔너리를 사용할 수 없음
# ex)  x = {100: 'hundred', False: 0, [3.5, 3.5]}


# 빈 딕셔너리 = {} or dict()


# dict : 키와 값은 연결하거나, 리스트/튜플/딕셔너리로 딕셔너리를 만들 때 사용
# 키에 ' ' 나 " " 사용하지 않아야함

# 1. 키 = 값 형식

# lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
# print(lux1)

# 2. dict에 zip함수 사용
# zip 함수로 키 리스트와 값 리스트를 묶음
# 키와 값을 리스트가 아닌 튜플에 저장한 후, zip에 넣어도 됨

# lux2 = dict(zip(['heath, 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
# print(lux2)

# 3. 리스트 안에 (키, 값) 형식으로 튜플을 나열
 
# lux3= dict([('health', 490), ('mana, 334'), ('melee', 550), ('armor, 18.72)])
# print(lux3)

# 4. dict 안에 중괄호로 딕셔너리 생성하는 방법

# lux4 = dcit({'health': 490, 'mana': 334, 'melee': 500, 'armor': 18.72})
# print(lux4)


# 딕셔너리의 키에 접근하고 값 할당하기
# 딕셔너리[키]
# 딕셔너리[키] = 값
# 딕셔너리에 키를 지정하지 않으면 해당 딕셔너리 전체를 뜻함

lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health'] = 2037 # health 값을 2037로 변경
print(lux['health']) # 변경된 health 값으로 출력
print(lux)


# 딕셔너리 키가 있는지/없는지 확인하기
# 키 in 딕셔너리, 키 not in 딕셔너리
# 특정 키가 존재하는가 ? = in 연산자
# 특정 키가 존재하지 않는가? = not in 연산자

lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print('health' in lux) # 럭스 딕셔너리에 health 키가 존재하는가에 대한 결과 출력
print('health' not in lux) # 럭스 딕셔너리에 health 키가 존재하지 않는가에 대한 결과 출력
print('attack' in lux)

# 딕셔너리 키 개수 구하기
# len(딕셔너리)

lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(len(lux))
print(len({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}))






