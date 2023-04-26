
n = int(input())
text = input()
words = text.split() # 공백을 기준으로 문자열을 분리

if (len(words) < n): # 입력한 문자열의 길이가 입력한 정수 값보다 작은 경우
    print('wrong') # 틀린 값을 출력
else: # 입력한 정수 값과 같거나 큰 경우엔 
    n_gram = zip(*[words[i:] for i in range(n)]) # 입력한 정수값만큼 n-gram을 반복함
    for i in n_gram:
        print(i)
    