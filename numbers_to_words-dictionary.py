digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

phone_number = input("Phone: ")
output = ""

for ch in phone_number:
    output += digits_mapping.get(ch, "!") + " "
# If number out of bound of dict, then it will say !
print(output)