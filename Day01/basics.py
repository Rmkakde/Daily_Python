#Variables
"""A variable is a placeholder for information you want Python to recall later in the coding process when you need to complete an action. 
Technically, the variable acts as an address for where the data is stored in memory.
Rules:
1. Contain Letter, digit, Underscore.
2. Cannot start with digit
3. Case sensitive
4. No spaces allowed
5. Python keywords are not allowed
"""
num1 = 5
num2 = 6
print(num1 + num2)

Myname = "Rishi"
Surname = "K"
print(Myname+" "+Surname) # String Concatenation

#Data Types
A = 5 # Integer
B = 5.0 # Float 
C = False # Boolean
D = None # Null
E = 6j # Complex (real, imagenary) j represent the imagenary part
F = "Rishi" # String
G = """
This is a 
Multiline string
"""     # Multiline string

# We can use type() function to check type of variable
print (type(E))
