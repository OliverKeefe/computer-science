# 1. Write a Python function definition that takes one integer (whole number) as a parameter, 
# calculates the square of that number, and returns the result. Then write a simple program to 
# test the function; this should prompt the user to enter a number to be squared, a function call 
# passing this number as an argument, and finally the value returned by the function should 
# then be printed back to the user. 

def func(int):
    square = int ** 2

    return square

user_input = int(input("Enter a whole number: "))
print(func(user_input))