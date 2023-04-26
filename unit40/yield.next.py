

def number_generator():
    yield 0
    yield 1
    yield 2

g = number_generator()

a = next(g)
print(a)

b = next(g)
print(b)

c = next(g)
print(c)