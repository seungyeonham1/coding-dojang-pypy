# a = 50

# if a == 40 :
#     a += 10
# elif a == 30 :
#     a += 10
# else :              # 이 코드에서는 a != 40 과 같음
#     a -= 10

# print(a)


# if True :
#     print('T')
# else :
#     print('F')

# if False:
#     print('T')
# else :
#     print('F')

# if None:
#     print('T')
# else:
#     print('F')

# if 0:
#     print('T')
# else:
#     print('F')

# if 1:
#     print('T')
# else:
#     print('F')

# if 0x1F:
#     print('T')
# else:
#     print('F')

# if 0b1000:
#     print('T')
# else:
#     print('F')

# if 13.5:
#     print('T')
# else:
#     print('F')

# if 'Hello':
#     print('T')
# else:
#     print('F')

# if '':
#     print('T')
# else :
#     print('F')



def tf_check(challenge):
    if challenge :
        print('response: True')
        return True
    else :
        print('response: False')
        return False

def tf_check_reverse(challenge):
    if not challenge :
        print('response: True')
        return True
    else :
        print('response: False')
        return False

tf_check(1)

# x = 10
# y = 30

# if x == 10 or y == 20:
#     print('T')
# else :
#     print('F')

# if x > 0:
#     if x < 20 :
#         print('20보다 작은 양수')

# if x > 0 and x < 20 :
#     print('20보다 작은 양수')

# # 위 두개는 같은 동작을 하는 코드다. 중첩 if문으로 구현할 것 같으면 and 연산자를 사용하는 것이 좀 더 저렴하게 돈다.
# # 파이썬에서는 더 저렴하게 만들 수 있다.

# if 0 < x < 20:
#     print('20보다 작은 양수')