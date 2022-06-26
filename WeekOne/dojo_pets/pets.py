class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.health = 100
        self.energy = 50
        
    def sleep(self):
        self.health += 10
        self.energy +=5

    def eat(self):
        print(self.name + ' is happily eating')
        self.energy += 10
        self.health += 5
        print('Energy:',self.energy,'Health:', self.health)

    def play(self):
        self.energy -= 20
        print(self.name + ' is having fun playing')
        print('Energy:', self.energy)

    def make_noise(self):
        print((f'Harry: {self.noise}'))