
# 표준 입력으로 정수 3개 입력 (시작하는 초,  반복을 끝내는 초, 인덱스)
# 초의 범위 0 ~ 100000, 입력되는 인덱스 범위 0 ~ 10

# 시간 값은 문자열, 시:분:초 형식, 숫자가 한 자리일 경우 앞에 0을 붙임
# 1초는 00:00:01, 23:59:59를 넘길 시 00:00:00부터 다시 시작
# 시간은 반복을 끝낼 초 직전까지만 출력함.(반복을 끝낼 초는 포함되지 않음)


class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __getitem__(self, index):
    
        hour = (self.start + index) // 60 // 60 % 24
        minute = (self.start + index) // 60 % 60
        second = (self.start + index) % 60

        if index < self.stop - self.start:
            return '{0:02d}:{1:02d}:{2:02d}'.format(hour, minute, second)

        else:
            raise IndexError

start, stop, index = map(int, input().split()) # 0, 3, 2

for i in TimeIterator(start, stop): # 0, 3
    print(i) # i=0  i=1 i=2

print('\n', TimeIterator(start, stop)[index], sep = '')