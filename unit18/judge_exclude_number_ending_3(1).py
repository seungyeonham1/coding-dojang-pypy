

start, stop = map(int, input().split())

i = start

while True:
    if not 1 <= start <= 200:
        break
    elif not 10 <= stop <= 200:
        break


# i가 stop이랑 같은 경우, 코드를 중단시킨다. 다만 i가 출력조건을 만족시킨다면, 출력하고 중단시킨다.
    if i == stop:
        if not i % 10 == 3:
            print(i, end = ' ')
        break
        
# i가 10으로 나눴을 때 나머지가 3이 아닌 경우, i를 출력함
    if not i % 10 == 3:
        print(i, end = ' ')

# i는 1을 증가시킨다.
    i += 1

    

