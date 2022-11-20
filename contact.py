from datetime import date

class Contact:
    def __init__(self, id, first_name, last_name, birth_day, profession):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_day = birth_day
        self.profession = profession

class Girlfriend(Contact):
    def __init__(self, id, first_name, last_name, birth_day, profession):
        super().__init__(id, first_name, last_name, birth_day, profession)
    
    def get_information(self):
        return f'ID:{self.id}\nFullname - {self.first_name} {self.last_name}\nBirth_day - {self.birth_day}\nProfession - {self.profession}'


class Uncle(Contact):
    def __init__(self, id, first_name, last_name, birth_day, profession):
        super().__init__(id, first_name, last_name, birth_day, profession)
    
    def get_information(self):
        return f'ID:{self.id}\nFullname - {self.first_name} {self.last_name}\nBirth_day - {self.birth_day}\nProfession - {self.profession}'

class Brother(Contact):
    def __init__(self, id, first_name, last_name, birth_day, profession):
        super().__init__(id, first_name, last_name, birth_day, profession)
    
    def get_information(self):
        return f'ID:{self.id}\nFullname - {self.first_name} {self.last_name}\nBirth_day - {self.birth_day}\nProfession - {self.profession}'

c = Girlfriend('1', 'Emily', 'Clark', date(day = 8, month=9, year=1989), 'Kitcher')
d = Uncle('2', 'Tony', 'Stark', date(day = 11, month=4, year=1977), 'Teacher')
e = Brother('3', 'John', 'Snow', date(day=22, month=6, year=1984), 'Gamer')
print(c.get_information())
print('---'*28)
print(d.get_information())
print('---'*28)
print(e.get_information())
