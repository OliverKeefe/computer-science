# Task 2 
# Now modify the script to also record and output the number of times each number has been rolled. 

# Fixed, now actually records count of specific numbers after user stops rolling.
import random

def dice_roll():
    return random.randint(1, 6)

def main():
    roll_count = 0
    number_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    while True:
        user_input = input("Wish to roll the dice? Y/N")

        if user_input.lower() == 'y':
            roll_count += 1
            roll = dice_roll()
            number_counts[roll] += 1
            print("Roll", roll_count, ":", roll)
        
        elif user_input.lower() == 'n':
            print("Number of rolls:", roll_count)
            for i in range(1, 7):
                print("Number of", i, "rolls:", number_counts[i])
            exit()
        
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()