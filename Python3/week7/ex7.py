import math
from math import sqrt, ceil
import numpy as np

def even_numbers(maximum_number):
    for n in range(0, maximum_number + 1):
        # Check is even
        if n % 2 == 0:
            x = print(n, end=" ")
    return x

def odd_numbers(maximum_number):
    for n in range(0, maximum_number):
        # Check if odd
        if n % 2 != 0:
            x = print(n, end=" ")
    return x

def square_numbers(maximum_number):
# Do the square
    start = 1

    def square_func(start, maximum_number):
        for i in range(1, maximum_number+1):
            sqrt_i = sqrt(i)
            if sqrt_i == ceil(sqrt_i):
                yield i
    for i in square_func(1, maximum_number):
        print(i)

def cube_numbers(maximum_number):
# Do the cube
    start = 1

    def cube_func(start, maximum_number):
        for i in range(start, maximum_number+1):
            cbrt_i = np.cbrt(i)
            if i == 9:
                    print(3**3)
            if cbrt_i == ceil(cbrt_i):
                yield i
                
    for i in cube_func(1, maximum_number):
        print(i)

def triangle_numbers(maximum_number):
    start = 1
    ceiling = 1
    for i in range(start, maximum_number+1):
        if (ceiling + i) < maximum_number:
            ceiling += i
            print(int(i*(i+1)/2))

def main():
    choice = ''

    while choice == '':
        print("\n","Week 7, Exercise 7 Main Menu\n")
        print(" Number Sequences:\n", "-+-+-+-+-+-+-+-+-+-+-+-+-\n", "[a] : Even number \n", "[b] : Odd numbers\n", "[c] : Square numbers\n", "[d] : Cube numbers\n", "[e] : Triangle numbers\n", "[Q] : Quit\n",)
        choice = (input("Select menu option: "))

        if choice == 'a':
            maximum_number = int(input("Enter your max number: "))
            x = print(even_numbers(maximum_number))
            choice = ''
        elif choice == 'b':
            maximum_number = int(input("Enter your max number: "))
            x = print(odd_numbers(maximum_number))
            choice = ''
        elif choice == 'c':
            maximum_number = int(input("Enter your max number: "))
            x = print(square_numbers(maximum_number))
            choice = ''
        elif choice == 'd':
            maximum_number = int(input("Enter your max number: "))
            x = print(cube_numbers(maximum_number))
            choice = ''
        elif choice == 'e':
            maximum_number = int(input("Enter your max number: "))
            x = print(triangle_numbers(maximum_number))
            choice = ''
        elif choice == 'Q' or choice == 'q':
            exit()
        else:
            print("[!] Invalid input!")
            print("[!] Please try entering another character!")

if __name__ == "__main__":
    main()