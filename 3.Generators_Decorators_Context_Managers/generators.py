#----IKKE som generator function
fibonacci_nums = []

def create_fibonacci():
    n1 = 0
    n2 = 1
    while True:
        fibonacci_nums.append(n1)
        n1, n2 = n2, n1 + n2


#create_fibonacci()
#print(fibonacci_nums)

#----SOM generator function
fibonacci_nums = []

def generate_fibonacci():
    n1 = 0
    n2 = 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2

generator = generate_fibonacci()
print(generator)

fibonacci_nums.append(next(generator))
fibonacci_nums.append(next(generator))
fibonacci_nums.append(next(generator))
fibonacci_nums.append(next(generator))
fibonacci_nums.append(next(generator))
fibonacci_nums.append(next(generator))
print(fibonacci_nums)


#-----Generator expression

generator = (i for i in range(900000000000))

num_list = []

num_list.append(next(generator))
num_list.append(next(generator))
num_list.append(next(generator))
num_list.append(next(generator))
num_list.append(next(generator))

print(num_list)


