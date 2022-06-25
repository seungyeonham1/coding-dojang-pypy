
age = int(input())
balance = 9000

#if 7 <= age <= 12:
#    balance = balance - 650
#elif 13 <= age <= 18:
#    balance = balance - 1050
#elif age >= 19:
#    balance = balance - 1250

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