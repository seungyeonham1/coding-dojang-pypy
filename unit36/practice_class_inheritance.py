

# 리스트에 기능 추가하기

class AdvancedList(list): # AdvancedList는 기반 클래스 list를 상속받는 파생 클래스 

    def replace(self, one, hundred):
        while one in self:
            self[self.index(one)] = hundred
            








x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)  # 매개변수1: one, 매개변수2: hundred 
print(x)