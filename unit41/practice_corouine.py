

def find(word):
    result = False # 기본 값은 False
    while True: # 코루틴 무한 루프 
        line = (yield result)  # 코루틴 바깥에서 값을 전달
        result = word in line # 받아온 값에 찾는 단어가 있으면 결과를 할당함


f = find('Python')
next(f)

print(f.send('Hello, Python')) # send가 보낸 문자열을 line에 저장
print(f.send('Hello, world'))
print(f.send('Python Script'))

f.close()