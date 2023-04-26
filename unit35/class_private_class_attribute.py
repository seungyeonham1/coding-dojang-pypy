

class Knight:
    __item_limit = 10 

    def print_item_limit(self):
        print(Knight.__item_limit) # 클래스 안에서만 접근할 수 있음

x = Knight()
x.print_item_limit() 

print(Knight.__item_limit) # 클래스 바깥에선 접근할 수 없음