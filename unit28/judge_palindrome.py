word = [
    'apache\n', 'decal\n', 'did\n', 'neep\n', 'noon\n', 'refer\n', 'river\n'
    ]

with open('words.txt', 'w') as file:
    file.writelines(word)

# with open('words.txt', 'r') as file:
#     line = file.readlines() # 파일 내용 전체를 리스트 형태로 읽어서 가져온다

#     for i in line:
#         i = i.strip('\n') # 개행 문자를 제거한다
#         if list(i) == list(reversed(i)): # 개행 문자를 제거한 리스트 문자열과 반대로 뒤집은 문자열이 회문인 경우
#             print(i) # 회문인 단어를 출력

with open('words.txt', 'r') as file:
    line = file.readlines()

    for i in line:
        i = i.strip('\n')
        if i == ''.join(reversed(i)):
            print(i)



# 다른 사람이 코딩한 것 참고용 
# with open('words.txt', 'r') as file:
#     for line in file:
#         words = line.split() # 공백을 기준으로 리스트로 만듬
#         for word in words:
#             if list(word) == list(reversed(word)):
#                 print(word.strip()) # 가운데 공백을 제거함


