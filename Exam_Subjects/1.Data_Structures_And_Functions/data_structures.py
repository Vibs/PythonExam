#----------CLASS
from cgitb import text
import string
from tokenize import String


class RaceHorse:

    def __init__(self, name):
        self.name = name


    def __str__(self):
        return f'RaceHorse: name= {self.name}'

    #ligesom toString - kaldes når en instans af klassen kommes ind i print 
    def __repr__(self):
        return f'RaceHorse: name= {self.name}'

    def __add__(self, other):
        return RaceHorse(self.name + other.name)
        

#----------PRIMITVE

my_float = 3.1

my_integer = 4

my_string = 'Hej'
my_string = "Hej"
my_string = '''Hej'''

is_bool = True

#----------LIST
my_values = [3.4, 6, 'hej', 'hej', True, [1, 2, 3]]
same_values = [3.4, 6, True, 'hej', 'hej', [1, 2, 3]]

my_values is same_values # False
my_values == same_values # False

value = my_values[2] # finder værdi ud fra index
my_values[-1][0] = 4 # sætter værdi på index

my_values.append('Hej igen')

del my_values[2:4] # sletter del defineret via slicing

'Hej igen' in my_values # True


#print(my_values)

my_values = same_values

my_values[0] = 'HELLOO'
#print(' ')
#print(my_values + same_values)

#iterable fra reversed
hej = [1, 2, 3]
#print(next(reversed(hej)))

#----------TUPLE

my_tuple = ('Bente', 'Lise', 'Adam', 'Annika')


#! my_tuple[0] = 7 #! IKKE TILLADT

my_tuple[1] # finder værdi

my_tuple[::-1] # omvender via slicing

#print(my_tuple[::-1])

#--------SETS
users_set = {'Bente', 'Lise', 'Adam', 'Annika'}
admins = {'Bente', 'Tom', 'Jens'}

users_set.add('Liv')
users_set.remove('Adam')

# {'Bente', 'Annika', 'Jens', 'Lise', 'Adam', 'Tom'}
usersAndAdmins = users_set.union(admins)

'Bente' in users_set # True



test_set = {'Hej', (1, 2), 5}

r1 = RaceHorse('Bedste hest')
r2 = RaceHorse('Bedste hest')
r3 = r1

horses_set = {r1, r2, r3}

r1 is r3 # True
r1 is r2 # False


r1 == r2 # False
r1.name == r2.name # True
r1.name is r2.name # True



#-------DICTIONARY

h1 = RaceHorse("Komethesten")
h2 = RaceHorse("Dark Horse")

print((h1 + h2).name)

horses = {
    72873: h1,
    432: h2
}

horses['hej'] = 'Jeg er en String'

horses[432]

432 in horses # True
h1 in horses # False


for key in horses:
    print(horses[key])

# == returnerer en liste af tuples med key-value pairs
horses.items()

#--------Built in functions

for i in range(4):
    print(i) # 0, 1, 2, 3

for i in range(1, 10, 2):
    print(i) # 1, 3, 5, 7, 9




#------BUILT IN FUNCTIONS

# link(), tuple(), set(), dict()
my_list = [1, 7, 7, 5, 4, 5]
my_set = {1, 2, 3}
my_dictionary = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

my_list_with_tuples = [(1, 'Vibe Jensen'), (2, 'Cleo')]

new_list = list(my_dictionary)
new_tuple = tuple(my_set)
new_set = set(my_list)
new_dict = dict(my_list_with_tuples)

#---filter()

def isNumber(x):
    return isinstance(x, int) or isinstance(x, float)

my_list = [1, 5, 'Hej', 6.5, True]

filtered_list = filter(isNumber, my_list)

for x in filtered_list:
    print(x) # 1, 5, 6.5

#----sorted()

int_list = [4, 7, 9, 10, 8, 11]

# [4, 7, 8, 9, 10, 11]
sorted_list = sorted(int_list)

# [11, 10, 9, 8, 7, 4]
reversed_list = sorted(int_list, reverse=True)

# [4, 8, 10, 7, 9, 11]
sorted_by_equals = sorted(sorted_list, key= lambda i : i % 2)

print(f'sorted {sorted_by_equals}')

#---range()

r1 = range(3) 
r2 = range(5, 8) 
r3 = range(1, 11, 2) 

# 0, 1, 2
for i in range(3):
    print(i)

# 5, 6, 7
for i in range(5, 8):
    print(i)

# 1, 3, 5, 7, 9
for i in range(1, 11, 2):
    print(i)


#---type()

horse = RaceHorse("Komethesten")

print(type(horse))
print(type([1, 2, 3]))
print(type(2))



# Comprehensions

text = [
    '1. linje 1', 
    '2. linje 2', 
    '3. linje 3', 
    82847
]

# { 1: 'linje 1', 2: 'linje 2', 3: 'linje 3'}
text_without_numbers = { int(t[0]): t[3:] for t in text if isinstance(t, str)}

print(text_without_numbers)

new_set = {i for i in range(325)}

print(new_set)







