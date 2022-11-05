class Hero():
    def __init__(self, name, spell, rage):
        self.name = name
        self.spell = spell
        self.rage = rage

    def __str__(self):
        return f"Имя персонажа: {self.name} \nНавык : {self.spell}\nОсобый навык: {self.rage}"

war = Hero('Артур','Сияние света','Берсерк')

print(war)