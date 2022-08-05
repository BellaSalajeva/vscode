def greet_user(first_name, last_name): #add parameters into (). place holders defined in functions for receiving info
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard!")


print("Start")
greet_user("John", "Smith") #positional arguments
print("Finish")

# argument = value supplied to a function. info
# If you have parameters, supply the argument or get an error
# type error

#key-word argument below
greet_user(last_name = "Smith", first_name="John") #improve readability
# order will not be confused then, unlike ("Smith", "John")

#calc_cost(50, 5, 0.1) ??? what means.
# key-word argument best used esp for numerical values. increase readability
#calc_cost(total=50, shipping=5, discount=0.1)
#key-word arg should come after positional arguments
#bad greet_user(first="John", "Smith")
#ok greet_user("John", last="Smith")
greet_user("John", last_name="Bill") #ok
