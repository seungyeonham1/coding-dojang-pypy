

start, end = map(int, input().split())

a = [2 ** i for i in range(start, end+1)]
a.pop(1)
a.pop(-2)
print(a)