my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

#Your code go from here:
def maxInteger(array):
    biggest_num = 0
    for x in array:
        if x > biggest_num:
            biggest_num = x
    return biggest_num

print(maxInteger(my_list))