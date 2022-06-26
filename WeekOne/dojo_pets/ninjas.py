# Harry = Pet('Harry', 'Dog', ['roll-over', 'sit'], 'woof!')

from pets import Pet

class Ninjas:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(self.first_name + ' is taking ' + self.pet.name + ' for a walk!')
        self.pet.play()

    def feed(self):
        if self.pet.type == 'Dog':
            print(self.first_name, "is feeding", self.pet_food[1],'to', self.pet.name)
        self.pet.eat()

    def bathe(self):
        print(self.first_name, 'is giving', self.pet.name, 'a bath.')
        self.pet.make_noise()

    def give_treat(self):
        if self.pet.type == 'Dog':
            print(self.first_name, 'gives', self.pet.name, 'some', self.treats[3])
            self.pet.eat()

# class Pet:
#     def __init__(self, name, type, tricks, noise):
#         self.name = name
#         self.type = type
#         self.tricks = tricks
#         self.noise = noise
#         self.health = 100
#         self.energy = 50
        
#     def sleep(self):
#         self.health += 10
#         self.energy +=5

#     def eat(self):
#         print(self.name + ' is happily eating')
#         self.energy += 10
#         self.health += 5
#         print('Energy:',self.energy,'Health:', self.health)

#     def play(self):
#         self.energy -= 20
#         print(self.name + ' is having fun playing')
#         print('Energy:', self.energy)

#     def make_noise(self):
#         print((f'Harry: {self.noise}'))


Harry = Pet('Harry', 'Dog', ['roll-over', 'sit'], 'woof!')
Ben = Ninjas('Benjamin', 'Smith', ['fish', 'kibbles','veggies','chicken'], ['Pizza', 'kibbles'], Harry)


Ben.feed()
Ben.walk()
Ben.bathe()
Ben.give_treat()