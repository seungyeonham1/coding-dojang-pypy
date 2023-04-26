
# 학생 클래스가 아닌 사람 목록을 관리하는 클래스

class Person:
    def greeting(self):
        print('안녕하세요.')

class PersonList:
    def __init__(self):
        self.person_list = []  # 리스트 속성에 Person 인스턴스를 넣어서 관리
                                # Personlist와 Person은 동등한 관계가 아닌 포함 관계 (has-a 관계)
                                # 사람 목록은 사람을 가지고 있다.

    def append_person(self, person):
        self.person_list.append(person) # 리스트 속성에 Person 인스턴스를 추가하는 함수