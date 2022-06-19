# repeat_count = 1

# for i in range(5):      # range(5)는 0,1,2,3,4를 생성하는 이터레이터다. 이터레이터는 반복 가능한 객체.
#     print('{0}번째 반복 : {1}'.format(repeat_count, i))
#     repeat_count += 1

# for i in range(5, 12):          # 시작값과 끝나는 값을 지정해서 for문 돌리기.
#     print('Hello, world!', i)

# for i in range(0, 10, 2):       # 시작값과 끝나는 값을 지정하고, 증가 폭도 정해서 for문 돌리기. 시작값을 2로 놓고 증가 폭을 2로 놓으면 짝수만 뽑으면서 돌릴 수 있다.
#     print('Hello, world!', i)

# for i in range(10, -1, -1):     # 10부터 1씩 감소 시키면서 반복하기. 0을 출력하기 위해서는 끝나는 숫자가 -1이 되어야 한다.
#     print('Hello, world!', i)

# for i in reversed(range(10)):   # range는 반복 가능한 객체기 때문에 reversed를 사용할 수 있다.
#     print('Hello, world!', i)


# count = int(input())
# repeat_count = 1

# for i in range(count):
#     print('반복 입력값: {0} / 반복 회수: {1} / i 변수 값: {2}'.format(count, repeat_count, i))
#     repeat_count += 1


a = ('a','b',3,4,5,6)
b = ['a','b',3,4,5,6]
c = {'a': 500,'b': 400, 'c': 300}
d = 'python'

letter_index = 1
reversed_letter_index = 1

# for i in a:
#     print('튜플', i)

# for i in b:
#     print('리스트', i)

# for key in c:
#     print('키 : {0} / 값 : {1}'.format(key, c[key]))

# for letter in d:
#     print('{0}번 문자열: {1}'.format(letter_index, letter))
#     letter_index += 1

# for letter in reversed(d):
#     print('{0}번 뒤집은 문자열: {1}'.format(reversed_letter_index, letter))
#     reversed_letter_index += 1

def reverse_str(string):
    reversed_str_list = []
    for i in reversed(string):
        reversed_str_list.append(i)
    
    result_str = "".join(reversed_str_list)
    return result_str


print(reverse_str(d))