# for i in range(1, 101): # 1 부터 100까지 반복. 총 100회 반복한다.
#     if i % 3 == 0:      # 3의 배수면 Fizz
#         print('Fizz')
#     elif i % 5 ==0:     # 5의 배수면 Buzz
#         print('Buzz')
#     else:               # 아무것도 해당하지 않으면 그냥 숫자 출력
#         print(i)


# for i in range(1, 101): # 1 부터 100까지 반복. 총 100회 반복한다.
#     if i % 15 == 0:      # 3의 배수면 Fizz. i % 3 == 0 and i % 5 == 0 과 같다. 코드를 줄일 수 있지만, 가독성은 그만큼 떨어진다.
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:     # 5의 배수면 Buzz
#         print('Buzz')
#     else:               # 아무것도 해당하지 않으면 그냥 숫자 출력
#         print(i)

for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)