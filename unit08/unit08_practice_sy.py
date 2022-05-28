# # a = 3
# # b = 1
# # c = True
# # d = False
# # print(type(c))
# # print(type(d))

# # print(a == b) 
# # print(a == a) # bool 자료형은 False, True만 존재한다. 참 거짓으로만 동작하며, 주로 if 문에서 조건분기를 사용할때 이 자료형을 많이 활용한다.

# x = 'hello'
# y = 'hello1'
# z = 'hello'

# print(x == y)
# print(x == z)
# print(x + '1' == y) # 스트링은 + 연산자를 사용할 수 있음. 따라서 이 경우 x에 '1' 이라는 스트링을 더했고, 결과는 'hello1' 이 된다. y와 같기때문에 True

# a = 10 # a는 int 객체
# a1 = 10 
# a2 = 10.0 # a2는 float 객제
# b = 15
# c = 20

# print(a > b)
# print(a < c)
# print(a >= a1)
# print(a == a2)
# # 비교 연산자. 값만을 비교한다.

# print(a is a2)
# # 객체 비교. 객체 id를 기준으로 비교하기 때문에 값이 같더라도 다른 객체라면 false를 반환한다.

# print(id(a))
# print(id(a2))
# # 두 객체의 id를 확인한다. 다른 객체라는 것을 알 수 있음.

# print(True and True)
# print(True and False)
# print(False and True)
# print(True and True and False)
# # and 논리 연산자. 모든 값이 True인 경우에만 True를 반환한다.

# print(True or True)
# print(True or False)
# print(False or False)
# print(True or False or False)
# # or 논리 연산자. 값 중에 단 하나라도 True가 있다면 True를 반환한다.

# print(not True)
# print(not False)
# # not 논리 연산자. True와 False 논리값을 뒤집는다. 이 경우 True는 False가 되고 False는 True가 된다.

# print(not True and False or not False)
# # 논리 연산자가 여러개 쓰여있는 경우 not - and - or 순으로 판단한다.
# # not True와 not False를 먼저 체크한다. 따라서 이 경우 False and False or True가 된다.
# # or True가 있기 때문에 앞의 결과와 상관 없이 True를 반환한다.
# # 순서를 명확하게 표현하는 것이 좋기 때문에 괄호로 표현하는 것이 좋다.

# print(10 == 10 and 5 != 10) # True and True = True
# print(not 10 == 10 or 10 == 5) # False or False = False
# print(10 is 10.0 and 0 != None) # False and True = False



# a_list = [1,2,3,4,5,6,7,8,9,10]
# a_result = []

# for i in a_list:
#     if not i == 5:
#         a_result.append(i)
#     else :
#         continue


# for i in a_result:
#     print(i)

math = int(input()) # 수학이 80점 이상이면 A, 50점 이상 80점 미만이면 B, 50점 미만은 C
student = '' # 랭크를 기록할 변수
rank_input = input() # 예상 랭크 받기

if math >= 80: # 입력받은 점수별로 랭크 부여하기
    student = 'A'
elif math >= 50 and math < 80:
    student = 'B'
else :
    student = 'C' # 위 조건에 다 해당하지 않으면 어차피 C니까 그냥 else로 처리한다.

result_check = student == rank_input # 예상 랭크랑 실제 랭크랑 같은가?

print(result_check) # 결과를 Bool 타입으로 출력한다.