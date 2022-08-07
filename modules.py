# A file with python code. To organise code into multiple files
# Add info from converters.py
import converters # converters is an object

print(converters.kg_to_lbs(70))

# or instead of importing the whole module, we can just import the functions
from converters import kg_to_lbs

kg_to_lbs(100)

# cleaner + easier

# Use modules to better organise our code.
# Instead of writing all code functions, break up across multiple files
# Each file is called a module containing related functions and classes
# Import modules into another module