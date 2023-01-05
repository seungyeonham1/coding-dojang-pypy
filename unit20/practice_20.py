

# fizz , buzz
# 조건이 더 많은 문을 if문에 둘것

# for i in range(1, 101): # 1부터 100까지 100번 반복
#   print(i)


for i in range(1, 101):

    if i % 2 == 0 and i % 3 == 0:
        print('DJ MAX')
    elif i % 2 == 0 :
        print('DJ')
    elif i % 3 == 0 :
        print('MAX')
    else:
        print(i)


# for i in range(1, 101):
#     if i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)


# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:  # if i % 15 == 0: 
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)


# for i in range(1,101):
#     print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)