


# 표준 입력으로 문자 입력
# 'the' 의 개수를 출력하는 프로그램을 만들 것 = count('the')
# 단, 모든 문자가 소문자인 'the'만 찾으면 되며,  'them', 'there', 'their' 등은 포함되지 말아야함 

# 입력값 
# the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the.

# 특정문자 삭제하기 활용 the. the,


user_input = input().split()

COUNT = 0

for i in user_input: # 유저 입력값을 i에 할당하고 하나씩 꺼내면서 반복한다
    if i.strip(',.') == 'the': # i의 ',' , '.' 문자들을 제거한 문자열이 'the'인 경우엔 
        COUNT += 1  # 카운트 값에 1을 증가시킨 뒤,
print(COUNT) # 모든 반복이 끝나고, the의 카운트를 출력한다.

