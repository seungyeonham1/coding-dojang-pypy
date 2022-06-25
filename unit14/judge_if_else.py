korea, english, math, science = map(int,input().split())
average = (korea + english + math + science) / 4


if not 0 <= korea <= 100 or not 0 <= english <= 100 or not 0 <= math <= 100 or not 0 <= science <= 100:
    print('잘못된 점수')
    quit()
else:
    pass

if 80 <= average <= 100:
    print('합격')
else:
    print('불합격')

