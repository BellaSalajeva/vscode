numbers = [5, 2, 1, 5, 7, 4]
numbers.append(20) #add 2- to end of list
numbers.insert(0,10) #at index 0 add number 10
numbers.remove(5) # remove number 5
numbers.clear() #remove all values. get empty list
numbers.pop() #remove last item in list
numbers.index(5) #returns index of first occurence of this item. error if number doesnt exist in list

print(50 in numbers) #returns false, does not return an error.
print(numbers.count(5)) #returns a 2 since 2 number 5's
print(numbers.sort()) #returns None. object in python that returns no value (None).
# Instead so this in 2 steps
numbers.sort()
numbers.reverse() #do this to change order from ascending to descending
print(numbers) #returns a sorted list from smallest to largest(ascending order)

numbers2 = numbers.copy()#get copy of list
numbers.apend(10)
print(numbers)
print(numbers2) #2nd list will not have the new 10 value
