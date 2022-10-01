list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


#Your code here:
def merge_two_list(number_list):
    odd_list = []
    even_list = []
    for x in number_list:
        if (x % 2) == 0:
            even_list.append(x)
        else:
            odd_list.append(x)

    final_list = []

    final_list.append(odd_list)
    final_list.append(even_list)
    
    return final_list

print(merge_two_list(list_of_numbers))

