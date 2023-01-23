# Define a new function called get_factors() that takes a single integer as a parameter. The
# function should then calculate all the factors of the integer (including 1 and itself), and return these
# values in the form of a Python list. If a negative integer or zero is given for the parameter, then the
# function should simply return an empty list.
# 
# Write a simple program to test your get_factors() function with different arguments.

def get_factors(integer):
    factors = []
    
    for i in range(1, integer + 1):
        if integer % i == 0 :
            factors.append(i)
    return factors
def main():
    integer = input("Enter and integer value: ")
    
    while not isinstance(integer, int):
        try:
            integer = int(integer)
        except ValueError:
            print("[!] Invalid input.") 
            integer = input("Enter and integer value: ")
    
    factors = get_factors(integer)
    
    for i in factors:
        print(i)
    
if __name__ == "__main__":
    main()