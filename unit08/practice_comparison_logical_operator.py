#korean = 92
#english = 47
#mathematics = 86
#science = 81
#print(korean >= 50 and english >=50 and mathematics >=50 and science >= 50)


kr, en, ma, sc = map(int, input().split()) # 과목 점수를 입력 받는다
print(kr >=50 and en >= 50 and ma >= 50 and sc >= 50) # 50점 이상일 시 true, 미만일 시 false
