# 이 코드는 words_row 리스트에 있는 문자열의 ""를 “ ” 로 변경하는 코드다. 변경된 문자열은, 변경 전과 변경 후를 모두 출력해 줘야 하며
# 최종적으로 변환 코드가 몇번 돌았는지에 대한 횟수를 출력해야 한다.
# 아래의 출력 예시를 참고하고 필요한 부분을 구현해야 한다.

#-------------------------------------------------
# 예시 :
# 변경 전: 망한 게임에는 "망한이유" 가 있다.
# 변경 후: 망한 게임에는 “망한이유” 가 있다.

# 변경 전: "맹공" 스택이 1 증가할 때마다 주는 피해가 10 증가한다. "맹공" 스택은 5회 까지 중첩 가능하다.
# 변경 후: “맹공” 스택이 1 증가할 때마다 주는 피해가 10 증가한다. “맹공” 스택은 5회 까지 중첩 가능하다.

# 변경 전: "이게" "왜" "안됨?"
# 변경 후: “이게” “왜” “안됨?”
# >>>> 전체 문자 변환 완료 (변환 횟수: 3)
#-------------------------------------------------

words_row = [
     '망한 게임에는 "망한이유" 가 있다.',
     '"맹공" 스택이 1 증가할 때마다 주는 피해가 10 증가한다. "맹공" 스택은 5회 까지 중첩 가능하다.',
     '"이게" "왜" "안됨?"'
     ]

# R_COUNT = 0

# for i in words_row: # words_row의 요소를 하나씩 꺼내 i에 할당한다.

#     #if words_row[i] == '"':
#         new_word = i.replace('"', '“') # '“'로 대체한다.
#         R_COUNT += 1
#         #new_list.append(new_word)
        
#         print('변경 전:', i) 
#         print('변경 후:', new_word) 

# print(f'>>>> 전체 문자 변환 완료 (변환 횟수: {R_COUNT})')


R_COUNT = 0 # 수정한 횟수 카운트 용 
replaced_words_row = []

for row in words_row: # words_row의 요소를 하나씩 꺼내 i에 할당한다.
    if '"' in row:
        TARGET_COUNT = 0 # “ ” 앞, 뒤따옴표 따로 넣기 위한 홀수, 짝수 구분 용도로 카운트 사용 
        new_word_list = [] # 따옴표 수정한 리스트를 저장하기 위한 새로운 리스트 선언

        for word in row:
            if word == '"': # 따옴표가 있다면 
                TARGET_COUNT += 1 # 타겟 카운트 1 증가한다

                if not TARGET_COUNT % 2 == 0: # 타켓 카운트가 홀수인 경우
                    word = '“'  # 앞 따옴표로 수정하고 
                else:
                    word = "”"  # 짝수인 경우는 뒤 따옴표로 수정한다.

            new_word_list.append(word) # 그리고 수정된 문자열을 앞에 선언한 새로운 수정 리스트에 append 한다.
        R_COUNT += 1 # 수정한 횟수 1 증가한다.
    replaced_words_row.append(''.join(new_word_list))


P_COUNT = 0 # 마지막 출력에 개행을 넣지 않기 위한 카운트용 선언 
for original, replaced in zip(words_row, replaced_words_row):
    print(f'변경 전: {original}')
    print(f'변경 후: {replaced}')
    P_COUNT += 1

    if not P_COUNT == len(words_row):
        print() # 개행
    else :
        continue

print(f'>>>> 전체 문자 변환 완료 (변환 횟수: {R_COUNT})')