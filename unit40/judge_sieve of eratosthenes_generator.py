

# 에라토스테네스의 체 ?
# 자연수 1을 제거 > 2를 제외한 2의 배수 제거 > 3을 제외한 3의 배수 제거 > 5를 제외한 5의 배수 제거 > 7을 제외한 7의 배수 제거

import math

def prime_number_generator(start, stop):
  n = stop
  # 구하고자 하는 수 만큼 True를 갖는 리스트 생성
  check = [True] * n
  # n의 최대 약수가 sqrt(n) 이하이므로 계산한 후, 소숫점이 있을 경우 올림으로 최대 반복 횟수 계산
  max_length = math.ceil(math.sqrt(n))

  for i in range(2, max_length):
    # True일 경우, 소수
    if check[i]:
      # i이후 i의 배수들을 지워나감
      for j in range(i+i, n, i):
       check[j] = False

  # 리스트의 True로 남아있는 인덱스(소수)를 추출
  yield from [i for i in range(start, stop) if check[i]]

 
start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))

for i in g:
    print(i, end=' ')