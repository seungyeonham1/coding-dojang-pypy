

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def from_string(cls, time_string):
        '''문자열로 인스턴스를 만드는 메서드.'''
        hour, minute, second = map(int, time_string.split(':'))
        return cls(hour, minute, second)


    @staticmethod
    def is_time_valid(time_string):
        '''문자열이 올바른 시간인지 검사하는 메서드'''
        hour, minute, second = map(int, time_string.split(':'))
        return hour<=24 and minute <= 59 and second <= 60


time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')