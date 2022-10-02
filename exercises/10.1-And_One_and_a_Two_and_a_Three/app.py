contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}
#Your code here:
def contact_loop(dictionary):
    dictionary_keys = dictionary.keys()
    dictionary_values = dictionary.values()

    keys_arr = []
    values_arr = []

    for x in dictionary_keys:
        keys_arr.append(x)
    for y in dictionary_values:
        values_arr.append(y)
    
    line1 = keys_arr[0] + ' : ' + values_arr[0]
    line2 = keys_arr[1] + ' : ' + values_arr[1]
    line3 = keys_arr[2] + ' : ' + values_arr[2]

    print(line1)
    print(line2)
    print(line3)

contact_loop(contact)
