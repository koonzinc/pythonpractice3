chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    empty_list = []
    for x in list1:
        empty_list.append(x)
    for y in list2:
        empty_list.append(y)
    return empty_list


    
print(merge_list(chunk_one, chunk_two))
