import math as m
import random as r

inp = input('Get a number between 0 and: ')
random_no = r.randint(0, int(inp))
square_root = m.sqrt(random_no)
print(f'This is your random number: {random_no}')
print(f'and its square root {square_root}')




from cat import Cat

cat = Cat('Cleo')
cat.meow()

