print(1,2,3)
print('a','b','c')

print(1,2,3, sep=', ')
print('a','b','c', sep='\n')
print('a','b','c', sep='') # sep 사용하여 다양하게 나눠보기. 여기서 sep ='\n'을 하면 각 요소를 세로로 한 줄씩 출력할 수 있다는 것을 알 수 있다.

a, b, c = 'apple', 'orange', 'kiwi'
print(a,b,c, sep='\n') # 스트링을 변수로 전언하고 sep 사용해서 한줄로 뿌리기. 여기서는 공백 없이 전부 이어서 출력한다.

# sep은 구분자의 의미를 가짐. sep에 선언된 스트링을 사용하여 print할 각 요소를 나눈다. sep=''인 경우 공백 없이 모든 스트링을 전부 이어서 출력한다.

print('a','b','c', sep='\n') # 개행 문자 사용하여서 한줄로 출력하게 만들기
print('a\nb\nc') # \n은 개행'문자'이므로 다음과 같이 직접 스트링에 넣어서 사용할 수도 있다. 다만 제어문자기 때문에 실제로 출력되진 않는다.

# 제어 문자는 이스케이프 시퀀스.
# \n : 개행
# \t : 탭 (일반적으로 스페이스 4회)
# \\ : \ 문자 자체를 출력하는 용도로 사용한다.

print(a)
print(b)
print(c) # print는 기본적으로 맨 끝에 \n을 자동적으로 사용한 것과 같이 동작한다. print(a, end='\n') 과 같다.

print(a, end='')
print(b, end='')
print(c) # end=''를 지정해서 문자열 맨 뒤에 아무것도 넣지 않도록 처리. 이러면 print(a,b,c sep='') 과 같은 결과가 된다.

print(a, end=', ')
print(b, end=', ')
print(c) # end=''를 지정해서 문자열 맨 뒤에 공백 한개와 콤마 한개를 넣도록 처리. 이러면 print(a,b,c sep=', ') 과 같은 결과가 된다.



a = [1,2,3,4,5,6,7,8,9,10]
a_print = []


for i in a :
    a_print.append(a)
    if len(a_print) == 1:
        print('출력 시작 /\n',i, sep='')
    elif len(a_print) > 1 and len(a_print) != len(a):
        print(i)
    else : 
        print(i,end='\n/ 출력 종료')