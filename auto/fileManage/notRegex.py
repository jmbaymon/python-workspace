# Without regex 
def isAreaCode(text):
    if len(text) != 3:
        return False
    
    for i in range(0,2):
        if not text[i].isdecimal():
            return False
    return True


print("478 is area code: ")
print(isAreaCode('478'))

print("Jam is area code: ")
print(isAreaCode('Jam'))


