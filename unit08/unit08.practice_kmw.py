


#a = 4
#b = 1
#c = True
#print(a == b) # a와 b는 같다 
#print(type(c))


# boolean은 if 문에서 많이 사용
# boolean은 True/False 존재

#a = 'Hello'
#b = 'World'
#c = 'Python'

#print(a != b)

# 연산자 == 는 동등하다 라는 의미 
# 연산자 != 는 동등하지않다 라는 의미

#a = 14
#b = 15
#c = 29

#print(a+b == c)
#print(a-b < c)
#print(a*b < c)

# 부등호 정리 
# >는 초과, <는 미만, >=는 이상, <=는 이하


#a = 15
#b = 30
#c = 15


#print(a+b is not c)
#print(a is not c)

# is는 동등하다 라는 의미, is not은 동등하지 않다 라는 의미

 
#a = 15 #a는 int객체
#b = 15 #b는 int객체
#c = 30.0 #c는 float 객체

#print(id(c))

#id 함수는 객체의 고유한 값(메모리 주소)를 구함
#서로 같은 객체인지 다른 객체인지 비교할 때 주로 id 함수를 사용

#a = 10
#b = 11
#c = 13
#d = 10
#e = 12
#h = 23

#f=a+c
#g=b+e

#print(a != b and a == d)
#print(f == g or not c == h)


#논리 연산자 and/or/not
#and : 두 개의 값이 모두 True여야 True / 하나라도 다르면 False
#or : 두 값 중 하나라도 True면 True /  두 값이 모두 False 여야 False
#not : 논리 값을 뒤집음 not true는 False를 의미하고, not False는 True를 의미


math = int(input()) # 수학 점수가 80이상이면 A, 50점이상 80점 미만 B, 50점미만 C
student = ''
rank_input = input()

if math >= 80:
    student = 'A'
elif math >= 50 and math < 80:
    student = 'B'
else :
    student = 'C'

result_check = (student == rank_input)

print(result_check)



#print(bool(1))
