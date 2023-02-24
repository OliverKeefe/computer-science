# 3. Write two Python scripts to output the first x entries in the n times table, where x and n are 
# both user inputs – one script should use a for loop and the other should use a while loop. 

def main():
    n = int(input("Input number to multiply: "))
    x = int(input("Enter how many times you wish to multiply it: "))
    while not isinstance(n, int):
        try:
            n = int(n)
        except ValueError:
            print("Invalid, your input must be an integer.")
            n = int(input("Input number to multiply: "))

    while not isinstance(x, int):
        try:
            x = int(x)
        except ValueError:
            print("Invalid, your input must be an integer.")
            x = int(input("Enter how many times you wish to multiply it: "))

    for i in range(1, x+1): 
       print(n, "x", i, "=", i*n)
    
    ii = 1
    while ii <= x:
        print(n, "x", ii, "=", ii*n)
        ii += 1
        
if __name__ == "__main__":
    main()