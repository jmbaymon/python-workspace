import random
import pdb
print("Guess a number between 1 and 10")
number = random.randint(1,10)
pdb.set_trace()
guess = input()

if guess == number:
    print(f'Correct in the number was {number}')
else: 
    print(f'Sorry, the number was {number}, not {guess}')
