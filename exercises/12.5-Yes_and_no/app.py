theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
newBools = list(map(lambda number: 'woko' if number == 0 else 'wiki', theBools))
print(newBools)

