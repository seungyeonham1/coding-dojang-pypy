x = input().split()
y = map(float, input().split())

stat = dict(zip(x,y)) #스탯은 x,y 입력받은 값을 zip함수로 묶어서 딕셔너리로 만듬
print(stat)