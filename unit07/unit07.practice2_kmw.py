#print(1, 2, 3, sep=', ') # sep에 콤마와 공백을 지정
#print(4, 5, 6, sep=',') # sep에 콤마만 지정
#print('Hello', 'Python', sep='') #sep에 빈 문자열을 지정
#print(1920, 1080, sep='x') #sep에 x를 지정

print(1,2,3, sep='\n') #1,2,3 값을 한 줄로 출력
print('1\n2\n3') #문자열 안에 \n을 사용하여 줄 바꿈
#\n : 다음 줄로 이동하며, 개행이라 불림
#\t : 탭 문자, 여러 칸을 띄움
#\\ : 문자 자체를 출력할 때는 \를 2번 씀

print(1,2,3, sep='\\')

# print는 기본적으로 출력하는 값에 \n을 붙임.
# 한 줄에 여러 개 값을 출력하기 위해선 end를 사용함
# print(1, end= '') # end에 빈 문자열을 지정하면 다음번 출력이 바로 뒤에 오게 됨
# print(2, end= '')
# print(3)

# 만약 출력값 사이를 띄워주고 싶다면
# print(1, end=' ') # end에 작은 따옴표 사이 공백을 한 칸 띄워 준다.
# print(2, end=' ')
# print(3)
