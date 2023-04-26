# 문자열이 저장된 words.txt 파일이 주어짐(문자열은 한 줄로 저장됨)
# words.txt 파일에서 문자 c가 포함된 단어를 각 줄에 출력하는 프로그램을 만드세요.
# 단어를 출력할 땐 순서대로 출력해야하며, 콤마와 점은 출력하지 않음



word = [ 'fortunately, ', 'however, ', 'for the reputation of asteroid B-612, ', 'a Turkish dictator made a law that his subjects, ',
'under pain of death, ', 'should change to European costume. ', 'So in 1920 the astronomer gave his demonstration all over again, ', 
'dressed with impressive style and elegance. ', 'And this time everybody accepted his report.'
]

with open('words.txt', 'w') as file:
    file.writelines(word)


with open('words.txt', 'r') as file:
    #text = file.readline() # text는 파일에서 문자열을 읽어온다
    #words = text.split() # 공백을 기준으로 문자열을 분리하여 리스트로 만듬
    #for word in words: 
    #    if 'c' in word: # words안의 단어 문자열이 'c'가 있는 경우
    #        print(word.strip(',.')) # 콤마와 점을 제거한 뒤 'c'가 포함된 문자열을 출력한다.

    text = file.readline().split() # 메서드 체이닝을 활용하여 공백을 기준으로한 문자열을 분리하여 리스트로 만듬 
    for i in text:
        if 'c' in i:
            print(i.strip(',.'))