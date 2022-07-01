

a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]  # 리스트 a를 반복한다, 만약 문자열 길이가 5인 경우에

print(b) # b에서 문자열 길이 5인 값을 출력한다