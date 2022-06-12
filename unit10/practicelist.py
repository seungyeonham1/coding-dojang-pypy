
#() = 튜플, 튜플은 리스트와 달리 저장된 요소를 변경/추가/제거할 수 없음, 괄호를 사용하지 않아도 만들 수 있음
#tuple(range(횟수)),tuple(range(시작,끝)),tuple(range(시작,끝,증가폭))

#[] = 리스트, 리스트 안에 저장된 값 = 요소
#list(range(횟수)), list(range(시작,끝)), list(range(시작,끝,증가폭))

#list와 tuple은 서로 바꿔 만들 수 있음
# a = [1, 2, 3]
# tuple(a)
# (1, 2, 3)

# b = (4, 5, 6)
# list(b)
# [4, 5, 6]



a = list(range(5,-10,-2)) #a는 5부터 -10까지 -2만큼 감소하는 리스트 패킹
print(a) #a를 출력