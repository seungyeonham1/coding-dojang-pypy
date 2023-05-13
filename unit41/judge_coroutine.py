

def calc():
    sum = 0
    while True:
        x = (yield sum)
        num1, operator, num2 = x.split()
        if operator == '+':
            sum = int(num1) + int(num2)
        elif operator == '-':
            sum = int(num1) - int(num2)
        elif operator == '*':
            sum = int(num1) * int(num2)
        elif operator == '/':
            sum = int(num1) / int(num2)
        

       
expressions = input().split(', ')

c = calc()
next(c)

for e in expressions:
    print(c.send(e))

c.close()