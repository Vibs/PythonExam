class Pet:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


class Cat(Pet):
    def __init__(self, name, lives = 9):
        super().__init__(name)
        self.lives = lives

    def had_accident(self, lives_lost = 1):
        self.lives -= lives_lost
        if self.lives == 0:
            print(f'Oh no! {self.name} is dead :O')
        if self.lives < 0:
            print(f'{self.name} is extra-dead')

    def __str__(self):
        return f'The Cat {self.name} has {self.lives} lives left'

cat = Cat("Cleo")
print(cat) # The Cat Cleo has 9 lives left
cat.had_accident(3)
print(cat) # The Cat Cleo has 6 lives left








print(isinstance(cat, Cat)) # True
print(isinstance(cat, Pet)) # True






    #def __init__(self, name, lives):
     #   self.lives = 9