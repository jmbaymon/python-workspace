# 
# Example file for variables
#

# Declare a variable and initialize it

f=0
print(f)


# # re-declaring the variable works

f="abc"
print(f)


# # ERROR: variables of different types cannot be combined
print("Jamal is " + str(19))



# Global vs. local variables in functions
def some():
    global f
    f="def"
    print(f)

some()
print(f)

#ERROR  undefines f 
# del f
print(f)
