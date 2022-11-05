class Monkey:
    max_age = 12
    loves_bananas = True
    
    def climb(self):
	    print('I am climbing the tree') 

animal = Monkey()
animal.climb()

kk = Monkey()
kk.climb()

print(animal.max_age,animal.loves_bananas)
print(kk.max_age, kk.loves_bananas)
