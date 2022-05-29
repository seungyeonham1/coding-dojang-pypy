
#year, month, day, hour, minute, second = map(int, input().split())
#print(year,month,day, sep= '-', end='T')
#print(hour,minute,second, sep=':')

year, month, day, hour, minute, second = input().split() # 6개의 입력 받은 값을 공백 기준으로 분리
print(year,month,day, sep ='-', end='T') # 날짜 출력한 뒤, sep에 -로 지정, end에 T 문자열로 지정
print(hour,minute,second, sep=':') # 시간 출력한 뒤, sep에 :로 지정