
# 재귀호출?
# 함수 자기 자신을 호출하는 방식을 재귀호출이라 부름
# 알고리즘을 구현할 때 아주 유용함
# 파이썬에서는 최대 재귀 깊이가 1,000으로 정해져 있음
# 그렇기 때문에, 재귀호출을 사용할려면 종료 조건을 만들어줘야함


# 재귀호출 사용

# def hello():
#    '''최대 재귀 깊이를 초과하여 RecursionError가 발생하는 재귀호출 함수'''

#     print('Hello, world!')
#     hello()

# hello()

def hello(count):
    ''' 반복 횟수를 계산하기 위해 매개변수 count를 지정'''
    if count == 0:
        return
    
    print('Hello, world!', count)

    count -= 1
    hello(count)

hello(5)



# 재귀호출로 팩토리얼 구현

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

