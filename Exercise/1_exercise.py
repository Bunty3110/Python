def highest_even(list):
    highest = 0
    for i in list:
        if i % 2 == 0 and i > highest:
            highest = i
    return highest
print(highest_even([10, 25, 32, 41, 35, 16]))