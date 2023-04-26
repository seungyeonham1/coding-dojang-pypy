


class Person:
    def __init__(self):
        self.bag = [] 

    def put_bag(self, stuff):  # put_bag 메서드
        self.bag.append(stuff) 

james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('칼')

print(james.bag)
print(maria.bag)


