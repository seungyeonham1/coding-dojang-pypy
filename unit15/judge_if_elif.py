"""
age = int(input())
balance = 9000

""" 

#if 7 <= age <= 12:
#    balance = balance - 650
#elif 13 <= age <= 18:
#    balance = balance - 1050
#elif age >= 19:
#    balance = balance - 1250

"""
if age < 7:
    quit()
else:
    pass

if 7 <= age <= 12:
    balance = balance - 650
elif 13 <= age <= 18:
    balance = balance - 1050
else:
    balance = balance - 1250 
print(balance)
"""

a = int(input())
money = 9000

if a < 7:
    print('7세 미만 어린이/아동은 무료입니다.')
    quit()
else:
    pass

if 7 <= a <= 12:
    print('만 7세 이상 12세 이하 어린이 요금은 650원 입니다.')
    money -= 650
    print(money)

elif 13<= a <= 18:
    print('만 13세 이상 18세 이하 청소년 요금은 1050원 입니다.')
    money -= 1050
    print(money)

else:
    print('만 19세 이상 성인 요금은 1250원 입니다.')
    money -= 1250
    print(money)