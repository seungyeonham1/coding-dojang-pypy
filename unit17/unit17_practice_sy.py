# i = 0
# while i < 5:
#     print('반복 회수: {0} / 출력 : Hello, world!'.format(i+1))
#     i += 1

# i = 10
# while i > 0:
#     print('Hello, world!', i)
#     i -= 1

# count = int(input())
# i = 0
# while i < count:        # i가 count보다 작은 동안 동작한다. 따라서 이 while 문은 input 받는 count의 값 만큼 아래의 코드를 반복한다.
#     print('Hello world!', i)
#     i += 1

from random import *


dice_range = list(range(1,13))  # 1~12
i = 0
# while i != 6:
#     i = randint(1, 6)
#     print(i)
#     if i == 6:
#         print('6 뽑아서 멈춤')

while i != 12:
    i = choice(dice_range)
    print(i)
    if i == 12:
        print('12 뽑아서 멈춤')


repeat_count = 0
while not False:
    print('Hello World! {0}'.format(repeat_count+1))
    repeat_count += 1

    if repeat_count == 100:
        break

