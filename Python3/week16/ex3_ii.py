# Task 2 
# Now modify the script to also record and output the number of times each number has been rolled. 

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
            print("Roll", roll_count, ":", dice_roll())
        
        elif user_input == 'n' or user_input == 'N':
            exit()
        
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()