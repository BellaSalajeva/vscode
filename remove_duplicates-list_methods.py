numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
#print(uniques)
## If want to change numbers list to remove its duplicates then below
numbers = uniques
print(numbers)