def square(number):
    return number * number

#result = square(3)
#print(result) 
# or
print(square(3))

# if
def square(number):
    print(number * number)

print(square(3))
#returns 9 followed by None
#WHY?
#9 is printed from first print in def
#no return in function. means None is returned from func
#by def all functions return None
