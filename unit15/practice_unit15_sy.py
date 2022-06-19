x = 30

if x == 10:
    print('10임')
elif x == 20:
    print('20임')
else:
    print('10도 20도 아님')

# elif와 else는 if에 종속된다. 따라서 단독으로는 사용이 불가능하다.
# 또한 else는 연속된 조건문의 가장 마지막에 위치해야 한다. elif보다 위에 있거나 if보다 위에 있을 수 없음.

button = int(input())

coke = [0,0,0,0,0,0,1,0,0,0,0,0,0]
cyder = [1,1,1,1,1,0,0,0,0]

def drink_count_check(drink_list):
    drink_count = 0
    for i in drink_list:
        if i:
            drink_count += 1
        else :
            continue
    
    return drink_count


if button == 1 :
    if drink_count_check(coke) :
        print('콜라')
    else :
        print('음료 다 떨어짐')
elif button == 2:
    if drink_count_check(cyder) :
        print('사이다')
    else :
        print('음료 다 떨어짐')

else :
    print('이상한 버튼 누름')