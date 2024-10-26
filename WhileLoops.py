### Part Two -- your code goes here. 
import random 

number = random.randint(1,100)

while True:
    guess = int(input("Guess a number from 1 to 100: "))
    
    if guess < number:
        print("Your Guess is too low")
    elif guess > number:
        print("Your Guess is too high")
        continue
    else:
        print(f"{guess} is correct")
        break