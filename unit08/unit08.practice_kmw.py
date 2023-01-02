#a = 4
#b = 1
#c = True
#print(a == b) # a와 b는 같다 
#print(type(c))


# boolean은 if 문에서 많이 사용
# boolean은 True/False 존재

# 문자열을 비교할 땐 '==', '!=' 연산자로 비교할 수 있으며, 대소문자를 구분함
# '==' 연산자는 참조값만 고려

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
# is 연산은 참조값과 객체를 둘다 고려함

 
#a = 15 #a는 int객체
#b = 15 #b는 int객체
#c = 30.0 #c는 float 객체
#d = 15.0 #d는 float 객체
#a1 = 15

#print(id(a))
#print(id(a1))
#print(id(d))

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

# and
# True and True =  True
# True and False = False
# False and True = False
# False and False = False

# or
# True or True = True
# True or False = True
# False or False = True
# False ore False = False

# not
# not True = False
# not False = True
# not True and False or not False =  not True and False 먼저 비교한 뒤 나온 결과를 or not False와 다시 비교한다.
# ((not True) and False) or (not False) = False and False = False or not False = False or True = True(최종)

#math = int(input()) # 수학 점수가 80이상이면 A, 50점이상 80점 미만 B, 50점미만 C
#student = ''
#rank_input = input()

#if math >= 80:
#    student = 'A'
#elif math >= 50 and math < 80:
#    student = 'B'
#else :
#    student = 'C'

#result_check = (student == rank_input)

#print(result_check)



#print(bool(1))


#print('Python' and True) # 파이썬에서 논리 연산자는 마지막으로 단란 평가를 실시한 값을 반환한다. 따라서 논리 연산자는 무조건 불을 반환하지 않는다.
#print('Python' and False)
#print(False and 'Python')
#print(True and 'Python')
#print(0 and 'Python')
#print(True or 'Python') # or 연산자는 마지막으로 단락 평가를 실시한 값이 반환됨
#print(0 or 'Python')
#print(True or 0)

#print(0.2 is 0.2)
#print(0.3 is 0.2)
#print(id(0.3))
#print(id(0.2))
#print(0.3 is 0.2+0.1)
#print(0.3 == 0.2+0.1)


a = 0.3
b = 0.2
c = 0.1
a1 = 0.3

d = 3
e = 2
f = 1
d1 = 3
d2 = 3.0

#print(a is b+c)
#print(a is a1)
#print(a == a1)
#print(a == b+c)
#print(d is e+f)
#print(d is d1)
#print(d == d1)
#print(d == e+f)

#print(id(a))
print(id(d))
print(id(d1))
#print(id(e+f))
#print(id(d2))
#print(id(d1 * 1.0))
#print(id(d1 * 1.0) is id(d2))
#print((d1 * 1.0) == (d2))
print(id(d1) == id(d))
print(id(d1) is id(d))