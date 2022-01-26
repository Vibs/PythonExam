class Owner:
    clinic = "Best Pet Clinic"

    def __init__(self, id, name, pets):
        self.id = id
        self.name = name
        if isinstance(pets, list):
            self.pets = pets
        else:
            self.pets = [pets]

class Cat:
    def __init__(self, name, lives = 9):
        self.name = name
        self.lives = lives

    
  
cat = Cat("Bastian", 6)
cat.name = "Cleo"



owner = Owner(42, "Vibe Jensen", cat)

print(owner.pets)

print(owner.clinic) # Best Pet Clinic
Owner.clinic = "Not the best clinic"
print(owner.clinic) # Not the best clinic


  
    #def __repr__(self):
     #   return f'Cat ({self.name}, {self.lives})'