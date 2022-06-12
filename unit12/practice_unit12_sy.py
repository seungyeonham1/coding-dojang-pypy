from random import randint


def no_mans(dice_1, dice_2):
    no_mans_fail_count = 0
    while True :
        dice_1 = randint(1,6)
        dice_2 = randint(1,6)

        if dice_1 != dice_2 :
            no_mans_fail_count += 1
            print('\n무인도 탈출 못함 {0}회'.format(no_mans_fail_count))
            print('뽑은거 :', dice_1, dice_2)
            continue
        
        elif dice_1 == dice_2 :
            print('\n무인도 탈출')
            print('뽑은거 :', dice_1, dice_2, '\n')
            return [dice_1, dice_2]

field = 0
dice_roll = 0
dice_roll_count = 0
no_mans_count = 0

while field < 40 :
    dice_roll = randint(1,6)
    field += dice_roll
    dice_roll_count += 1
    print('현재 위치 : {0} / 던진 횟수 : {1}'.format(field, dice_roll_count))

    if field == 10 or field == 20 or field == 30:
        no_mans_count += 1
        print('\n무인도 걸림 {0}회'.format(no_mans_count))
        dice_check1 = 0
        dice_check2 = 0
        no_mans(dice_check1, dice_check2)
    else :
        continue

print('\nfield 40 넘어서 게임 끝남')