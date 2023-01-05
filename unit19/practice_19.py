
# 중첩 루프 : 반복문 안에 반복문이 들어가는 형태


# i 는 세로 방향, j는 가로 방향
# for i in range(5): # 5번 반복, 바깥쪽
#    for j in range(5): # 5번 반복, 안쪽
#        print('j:', j, sep='', end=' ') # j값 출력

#    print('i:', i, '\\n', sep='') #i값 출력

    # j:0 j:1 j:2 j:3 j:4 i:0\n
    # j:0 j:1 j:2 j:3 j:4 i:1\n



#for i in range(5):
#    for j in range(5):
#        print('*', end='')
#    print() # j문의 5번 반복이 끝나면 i값을 출력  j가 5번일 때, i는 1번 

    #j: *****
    #j: *****
    #j: *****
    #j: *****
    #j: *****


#for i in range(3):
#    for j in range(7):
#        print('*', end='')
#    print()

#j: *******
#j: *******
#j: *******



# for i in range(5): # 0 1 2 3 4
#    for j in range(5): # 0 1 2 3 4
#        if j <= i: #i가 j보다 크거나 같으면
#            print('*', end='') # 별을 출력함
#    print()


# j: *
# j: **
# j: ***


#for i in range(5): # 0 1 2 3 4 
#    for j in range(5): # 0 1 2 3 4
#        if j == i: # j가 i값과 동일하다면
#            print('*', end='') # 별을 출력
#    print() # i값 출력

# *
# *
# *
# *
# *
# *


# for i in range(5):
#     for j in range(5):
#         if j == i:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# *
#  *
#   *


# 역삼각형

#for i in range(5):
#    for j in range(5):
#        if i <= j:
#            print('*', end = '')
#        else:
#            print(' ', end='')
#    print()


# 산 모양

# 좌 > 우 > 좌 방식으로 설계 
# 왼쪽 나무부터 출력하도록 설계함으로써, 순서를 뒤집는 reversed를 사용  

#a = int(input())

#for i in range(a):
#    for j in reversed (range(a)):
#        if i < j:
#            print('!', end = '')
#        else:
#            print('*', end = '')

#    for j in range(a):
#        if i > j:
#            print('*', end= '')
#        else:
#            print('!', end= '')
#    print()




# 리스트에서 알파벳 'O' 를 출력하는 방법

# a = ['Apple', 'Banana', 'Orange']

#print(type(a))
#print(type(str(a)))

#for i in str(a): # 문자열" ['Apple', 'Banana', 'Orange]를 for문으로 하나씩 뽑으면서
#    if i == 'O': # 'O'가 있으면
#        print(i) # 그것을 출력한다
#        #print(type(i))




#for i in a: # 'apple', 'banana', 'orange' 를 하나씩 뽑는다
#    for j in i: # 뽑은 것들 중에 
#        if j == 'O':
#            print(j)



#for i in ''.join(a):
#    if i == 'O':
#        print(i)

# print(a[2][0])  # 2차원 리스트를 이용해서 알파벳 O 출력


import random

dice = ['Apple', 'Banana', 'Orange']

COUNT = 0

#while i != 'O': # 뽑은 문자열이 O가 아닌 경우
#    COUNT += 1 # 카운트 횟수가 1 증가한다
#    i = random.choice(str(dice)) # dice의 문자열 중 랜덤으로 1개씩 뽑는다.
#    print(COUNT) # 횟수가 증가한 카운트를 출력한다

#    if i == 'O': # 뽑은 문자열이 O가 맞다면
#        print('O가 나왔습니다.') # O가 나왔습니다를 출력한다

#while True:
#    i = random.choice("".join(dice))
#    COUNT += 1

#    if i == 'O':
#        print('O가 나왔습니다', i)
#        print('주사위 횟수 : ', COUNT)
#        break

#while True:
#    i = random.choice(dice[2])
#    COUNT += 1 

#    if i == 'O':
#        print('O가 나왔습니다', i, '뽑는데 까지 걸린 횟수', COUNT)
#        break



#COUNT = 0 



while True: # True 값이 나올 때까지 무한루프 선언


# dice 리스트를 문자열로 변환하기 위해 join을 이용

    i = random.choice("".join(dice)) 
    print(' 주사위에서 나온 알파벳: ', i)
    COUNT += 1 # 카운트 횟수를 1 증가 한다

    if i == 'O': # 문자열이 O가 나왔다면
        print('O가 맞습니다: ', i + ' 뽑는데 까지 걸린 횟수: ', COUNT) # 결과값을 출력하고 최종 카운트 횟수를 출력한다
        break # 무한 루프를 멈춘다
    