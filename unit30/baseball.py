# 1. 중복되지 않는 랜덤한 숫자 3개를 뽑아서 저장하는 함수를 만들기

# 2. 유저가 3개의 숫자를 넣어서 풀이를 시도했을 때, 그 숫자에 따라 SBO를 출력해주는 함수를 만들기. 
# 단 이때 유저가 입력하는 숫자에 중복이 있으면 그 입력 횟수를 무효로 하고 다시 입력을 받도록 해야함.

# 3. 유저가 정답을 맞추면 정답을 맞췄다는걸 알리고 정답을 공개, 그리고 게임을 끝내기.
# 혹은 유저가 9회동안 정답을 맞추지 못하면 도전횟수가 다 소진되었다는 걸 알리고 정답을 공개, 그리고 게임을 끝내기

import random

# 랜덤 숫자 3개 뽑기 함수
def pickup_number():
    '''랜덤 숫자 3개 뽑기 함수'''
    auto_numbers = []

    # for i in range(3):
    #         num = random.randint(0,9)
    #         while num in list:
    #             num = random.randint(0,9)
    #         list.append(num)
    # return list

    while len(auto_numbers) < 3:
        num = random.randint(0,9)
        if num not in auto_numbers:
            auto_numbers.append(num)
    return auto_numbers


# num_list = pickup_number()
# print(num_list)

# 임의의 3개 숫자를 입력하여 맞추기

# 숫자 입력 3개를 While문 사용하기 
# 입력한 숫자가 중복이거나 범위를 벗어났을 경우 무효 = 조건문 달 것


def input_number():
    '''3개 숫자 입력한 뒤, 중복 및 범위 여부 확인하는 함수'''
    guess_numbers = []

    while len(guess_numbers) < 3: 
        # 숫자를 1개씩 입력하는 행위를 3번 반복하는 반복문
        three_num = int(input("{}번째 숫자를 입력하세요: ".format(len(guess_numbers) + 1)))

        if three_num < 0 or three_num > 9:
            print("입력한 값이 범위를 벗어났습니다. 다시 입력하세요.")
        elif three_num in guess_numbers:
            print("입력한 값이 중복된 숫자입니다. 다시 입력하세요.")
        else:
            guess_numbers.append(three_num)

    return guess_numbers

def sbo_score(guess, answer):
    '''입력한 숫자 3개를 스트라이크, 볼으로 계산해주는 함수'''
    i = 0
    strike_count = 0
    ball_count = 0
    out_count = 0

    while i < len(guess):

        if guess[i] == answer[i]:
            strike_count += 1
            i += 1

        elif guess[i] in answer:
            ball_count += 1
            i += 1

        else:
            out_count += 1 
            i += 1
    
    return strike_count, ball_count, out_count
# return {'st': strike_count, 'ba' : ball_count, 'ot': out_count}




# 숫자 야구 실행

answer = pickup_number()
innings = 0



while True:
    # 9회 이닝까지 반복함

    if innings > 9:
        print(f'답: {answer}')
        print('9회 초과. 게임 종료')
        break

    guess = input_number()
    st, ba, ot = sbo_score(guess, answer)
    print("{}sb, {}ba, {}ot".format(st, ba, ot))
    innings += 1

    if st == 3:
        print(f'답:{answer}')
        print(f'{innings}이닝 만에 맞췄습니다. 게임 종료')
        break




             

          



     


     

