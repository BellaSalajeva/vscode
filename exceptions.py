#Don't let progamme crash. Print a valid message
# if string entered for int
#try running these 2 lines of code
#If encouter value error type, dont crash prog, print error message
# "exception error"

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    #What happens if prog encounters value error
    print("Invalid value")

#PyCharm, if "Process finished with exit code 0" means prog didn't crash
