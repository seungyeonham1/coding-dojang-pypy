
# 단어가 줄 단위로 저장된 words.txt 파일이 주어짐

# 다음 소스 코드를 완성하여 10자 이하인 단어의 개수가 출력되게 만드세요.

word = [ 'anonymously\n', 'compatibility\n', 'dashboard\n', 'experience\n', 'photography\n', 'spotlight\n', 'warehouse\n']

with open('words.txt', 'w') as file:
    file.writelines(word)

with open('words.txt', 'r') as file:
    count = 0
    words = file.readlines() # 파일을 한 줄씩 읽는다.
    for i in words:
        if len(i.strip('\n')) <= 10: # 개행(\n)을 제거한 나머지 문자열 길이가 10이하인 경우
            count += 1 # 카운트 값이 1 증가한다.
    print(count) # 카운트 된 값이 출력됨

