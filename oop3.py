class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def calculate_age(self, time):
        self.time = time
        return f'{self.age}'

    def __str__(self):
        return f'{self.name}, {self.age + self.time}, {self.gender}'

    
p = Person('John', 23, 'male')
p.calculate_age(17) 
print(p)
