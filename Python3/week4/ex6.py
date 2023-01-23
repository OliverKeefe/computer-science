import string
import numpy as np

def main():
    user_input = (input("Input a series of numbers, for example: 1 2 3 4 5 6 7 8 9 ... here: "))
    split_input = user_input.split()
    print("You've entered:", user_input)
    desired_output = [int(i) for i in split_input]
    print("The sum of your number series is:", np.sum(desired_output))

if __name__ == "__main__":
    main()