#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:
randomlist = []
for i in range(10):
    randoms = random.randint(1, 1000)
    randomlist.append(randoms)

my_list = my_list + randomlist
print(my_list)
