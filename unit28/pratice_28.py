
# 회문: 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장
# 회문 예시: level, SOS, rotator, nurses run

# 문자열이 회문인지 판별하는 방법 = 가운데 문자를 기준으로 왼쪽과 오른쪽 문자가 같은 경우
# 회문 판별은 문자열의 길이가 가장 중요하다.

# 회문 판별 방법: 반복문으로 검사, 시퀀스 뒤집기로 검사, 리스트와 reversed로 검사, 문자열 join 메서드와 reversed로 검사


#word = input('단어를 입력하세요: ')

# is_palindrome = True # 회문 판별값을 저장할 변수, 초기값은 True
# for i in range(len(word) // 2): # 0부터 문자열의 길이의 절반만큼 반복시킨다
#     # level인 경우 인덱스 0 값과 -1 값이 같아야함 
#     if word[i] != word[-1 - i]: # 왼쪽 문자와 오른쪽 문자가 다르다면 (0, -1) (1, -2) (2, -3)
#         is_palindrome = False # 회문이 아니기 때문에 
#         break # 반복문이 멈춘다
# print(is_palindrome) # 회문 판별값을 출력한다


# # 시퀀스 뒤집기로 문자 검사하기

# word = input('단어를 입력하세요: ')
# print(word == word[::-1]) # 문자열 전체에서 인덱스를 1씩 감소시키면서 요소를 가져오는데, 문자열을 반대로 뒤집음


# 리스트와 reversed 사용하기

# word = input('단어를 입력하세요: ')
# print(list(word) == list(reversed(word)))


# 문자열의 join 메서드와 reversed 사용하기


#word = input('단어를 입력하세요: ')
#print(word == ''.join(reversed(word)))




# N-gram: 문자열에서 N개의 연속된 요소를 추출하는 방법
# 단어의 빈도를 세는 데 이용됨, 그래서 검색엔진, 빅데이터, 법언어학 분야에서 사용됨

# # 글자 단위 N-gram
# text = 'tomato'

# for i in range(len(text) - 1):
#     print(text[i], text[i + 1], sep='')

# # 단위 단위 N-gram
# text = 'this is python script'
# words = text.split()

# for i in range(len(words) - 1):
#     print(words[i], words[i + 1])

# # zip으로 2-gram

text = 'hello'

two_gram = zip(text, text[1:])
for i in two_gram:
    print(i[0], i[1], sep='')


# zip과 리스트 표현식으로 N-gram

# text = 'hello'
# # 리스트에 *를 붙이는 방법은 리스트 언패킹이라 함
# a = list(zip(*[text[i:] for i in range(3)]))
# print(a) 