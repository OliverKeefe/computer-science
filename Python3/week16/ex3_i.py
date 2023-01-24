# Exercise 3 – Random Numbers and Dice Exercise 
# There are a few ways to produce random numbers in Python; for example, you can use the standard 
# random module: 
# import random 
# print( random.random() ) 
# This will print a random floating point number in the range [0,1] 
#
# There are also many other random number generators included in this module, such as: 
#       • randrange(a,b) chooses an integer in the range [a,b]
#       • uniform(a,b) chooses a floating point number in the range [a,b]
#       • randint(a,b) is very similar to randrange(a,b) – you can experiment with it to work out 
#         the difference in the output 
# Task 1 
#
# Use an appropriate random number generator from above to make an electronic six sided dice. You 
# should create a new Python script to first generate random numbers between 1 and 6. Then put the 
# generator inside a loop and write a prompt to ask the user if they wish to roll again. Your script should 
# keep a record of how many rolls have been made in total.
import random

def dice_roll():
    for i in range(10):
        roll = random.randint(1, 6)

    return roll

def main():
    roll_count = 0

    while True:
        user_input = input("Wish to roll the dice? Y/N")

        if user_input == 'y' or user_input == 'Y':
            roll_count += 1
            print(dice_roll())
        
        elif user_input == 'n' or user_input == 'N':
            exit()
        
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()