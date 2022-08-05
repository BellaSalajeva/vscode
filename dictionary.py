# In a dictionary {}, key-value pairs can be stored
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

customer["name"] = "Jack Smith" # to change name
# to add new key-value pairs
customer["birthdate"] = "Jan 1 1980"

print(customer["name"]) #case-sensitive
# or
print(customer.get("name")) #get none and not error
print(customer.get("birthdate", "Jan 1 1980")) #dont have key birthdat, prints out jan 1 1980
