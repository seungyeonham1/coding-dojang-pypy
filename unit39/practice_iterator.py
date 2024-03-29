

# 특정 수의 배수를 만드는 이터레이터
# 배수는 0부터 지정된 숫자보다 작을 때까지

class MultipleIterator:
    def __init__(self, stop, multiple):
        self.stop = stop
        self.multiple = multiple
        self.current = 0


    def __iter__(self):
        return self
    
    def __next__(self):
        self.current += 1
        if self.current * self.multiple < self.stop:
            return self.current * self.multiple
        else:
            raise StopIteration


for i in MultipleIterator(20, 3):
    print(i, end= ' ')

print()
for i in MultipleIterator(30, 5):
    print(i, end = ' ')