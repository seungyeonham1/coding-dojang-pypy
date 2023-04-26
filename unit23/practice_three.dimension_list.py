
# 가로 (열) col
# 세로 (행) row
# 높이  ver

#a = [[[0 for col in range(3) ] for row in range(4)] for ver in range(2)]
#print(a)





# h 높이 = 2
# r 세로 = 4 
# c 가로 = 3
# 리스트 표현식을 사용하여 3차원 리스트로 만들어라


#answer = [[[0 for c in range(3)]for row in range(4)] for h in range(2)]

answer = [[[0] * 3 for r in range(4)] for h in range(2)]
print(answer)


