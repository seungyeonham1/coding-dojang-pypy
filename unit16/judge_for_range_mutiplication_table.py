

#a = int(input())

#for i in range(1, 10, 1):
#    print(a, '*', i, '=', a * i, end = '\n')




number = int(input())
COUNT = 0 # 상수는 변하지 않는 수를 의미하며, 파이썬의 상수는 항상 대문자로 쓰는 걸 권장함

for i in range(1, 10, 1):
    gugudan = number * i
    COUNT = COUNT + 1
    print(COUNT)
    print(number, '*', i, '=', gugudan, end = '\n')