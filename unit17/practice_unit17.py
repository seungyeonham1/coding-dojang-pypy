
# while 문 기본 문법
# while 조건식:
#   반복할 코드
#   변화식


# i = 0
# while i < 10:             # 조건식
#    print('Hello, python') # 반복할 코드
#    i += 1                 # 변화식



# 초깃값을 1부터 시작하기
#i = 1
#while i <= 10:          # 조건식
#    print('Hello, python', i) # 반복할 코드
#    i += 1             # 변화식


# 초깃값을 감소시키기

#i = 100
#while i > 0 :
#    print('hello, java', i)
#    i -= 1

# 입력한 횟수대로 반복하기

#count = int(input())

#i = 0
#while i < count:
#   print('python', i)
#   i += 1


#count = int(input())

#while count > 0:
#    print('python', count)
#    count -= 1



# import 모듈 = 함수를 호출
# import random = 랜덤 함수를 호출


#import random 

#i = 0
#while i != 6:
#    i = random.randint(1,6)
#    print(i)


# random.choice
# random.choice 함수는 시퀀스 객체에서 무작위로 요소를 선택함



#i = 0
#dice = [1, 2, 3, 4, 5, 6]

#while i != 6:
#    i = random.choice(dice)
#    print(i)



# while 반복문 무한 루프 

repeat_count = 0
while True:
    print('mint choko {0}'.format(repeat_count+1))
    repeat_count +=1


    if repeat_count == 50:
        break

