import time

class TimeIterator:
  def __init__(self, start, stop):
    self.start = start
    self.stop = stop

  def __getitem__(self, index):
    if index < self.stop - self.start:
      return time.strftime('%H:%M:%S', time.gmtime(self.start + index))
    # gmtime(secs) 형식 = 입력된 초를 기준
    else:
      raise IndexError
    

start, stop, index = map(int, input().split()) # 0, 3, 2

for i in TimeIterator(start, stop): # 0, 3
    print(i) # i=0  i=1 i=2

print('\n', TimeIterator(start, stop)[index], sep = '')