class Cat:
    def __init__(self, name, lives = 9):
        self.name = name
        self.lives = lives

    @property
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self, lives):
        if lives >= 0:
            self.__lives = lives
        else:
            self.__lives = 9
            print("You can't set your cat's lives to less than 0")

    def __repr__(self):
        return f'Cat ({self.name}, {self.lives})'

    
cat = Cat("Bastian", 6)
cat.name = "Cleo"
cat.lives = 6


class Owner:
    clinic = "Best Pet Clinic"

    def __init__(self, name, pets):
        self.name = name
        if isinstance(pets, list):
            self.pets = pets
        else:
            self.pets = [pets]

    def __add__(self, other):
        # duplikanter fjernet ved at konvertere til set
        joint_pets = set(self.pets).union(set(other.pets))
        joint_pets = list(joint_pets)

        return Owner([self.name, other.name], joint_pets)
    
    def __eq__(self, other):
        return self.name == other.name and set(self.pets) == set(other.pets)

    def __len__(self):
        return len(self.pets)

    def __repr__(self):
        return f'Owner ({self.name}, {self.pets})'


owner1 = Owner("Vibe Jensen", cat)
owner2 = Owner("Ninni Jensen", cat)
owner3 = owner1

owner4 = owner1 + owner2 # uden duplikeret kat
owner1 == owner3 # True
len(owner1) # 1



print(owner1.pets)

print(owner1.clinic) # Best Pet Clinic
Owner.clinic = "Not the best clinic"
print(owner1.clinic) # Not the best clinic


  
   

