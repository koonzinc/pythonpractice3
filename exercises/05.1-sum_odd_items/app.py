arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sum_odds(items):
    total_of_odds = 0

    for x in items:
        if (x % 2) == 0:
            pass
        else:
            total_of_odds += x

    return total_of_odds

print(sum_odds(arr))
