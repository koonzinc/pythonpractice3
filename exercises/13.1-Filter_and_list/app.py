
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def new_names(names):
    if names[0] == 'R':
        return names

resulting_names = list(filter(new_names, all_names))

print(resulting_names)




