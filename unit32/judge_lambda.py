

# 파일 이름 한꺼번에 바꾸기

# 표준 입력으로 숫자.확장자 형식으로 된 파일 이름 여러개가 입력됨
# 파일 이름이 숫자 3개 이면서 앞에 0이 들어가는 형식으로 출력되게 만들것
# 1.png -> 001.png 
# 람다 표현식을 사용하며, 출력 결과는 리스트 형태


#files = input().split()

#print(list(map(lambda x:'{0:03d}'.format(int(x.split('.')[0])) + '.' + x.split('.')[1] ,files)))






x = '1.jpg'

print('{0}'.format('1', 'jpg'))
print('{1}'.format('1', 'jpg'))
print('{0}.{1}'.format('1', 'jpg'))
print(x.split('.'))
print(x.split('.')[0])
print(x.split('.')[1])
print(x.split('.')[0] + '.' + x.split('.')[1])

print('{0:03d}'.format(int(x.split('.')[0])) + '.' + x.split('.')[1])