# Define a new function called is_perfect() which takes a single integer as a parameter. The
# function should return True if the integer is a perfect number, or False if it is not a perfect number.
# Note: you might like to re-use the get_factors() function from Exercise 5 to help with this
# exercise.
# Note: A perfect number is one whose factors (except itself) sum to itself. For example, the factors of
# 6 are 1, 2, 3, and 6. Since 1 + 2 + 3 = 6, then the number 6 is considered to be a perfect number.
# Write a simple program to test your is_perfect() function.

def is_perfect(integer):
    perfect = 0
    
    for i in range(1, integer):
        if integer % i == 0:
            perfect += i
        
    return perfect == integer

def main():
    integer = input("Enter an integer value: ")
    while not isinstance(integer, int):
        try:
            integer = int(integer)
            
        except ValueError:
            print("[!] Invalid input.") 
            integer = input("Enter and integer value: ")
        
    print(integer, "is a perfect number?", is_perfect(integer))
    
if __name__ == "__main__":
    main()