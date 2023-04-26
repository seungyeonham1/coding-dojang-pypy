

# 함수 c를 호출할 때마다 호출 횟수가 출력되게 만드세요.

def counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        return i
    return count
        
c = counter()
for i in range(10):
    print(c(), end=' ')