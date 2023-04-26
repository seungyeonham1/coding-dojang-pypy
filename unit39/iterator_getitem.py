

class Counter:
    def __init__(self, stop):
        self.stop = stop # 반복을 끝낼 숫자

# 클래스에서 __getitem__만 구현해도 이터레이터가 됨 (__iter__, __next__ 생략 가능)
    def __getitem__(self, index): # 인덱스를 받음
        if index < self.stop: # 인덱스가 반복을 끝낼 숫자보다 작은 경우
            return index # 인덱스를 반환
        else: # 인덱스가 반복을 끝낼 숫자보다 크거나 같은 경우
            raise IndexError # 예외를 발생하여 반복을 끝냄
        
print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

for i in Counter(3):
    print(i, end=' ')


