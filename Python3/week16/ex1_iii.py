# 3. Write two Python scripts to output the first x entries in the n times table, where x and n are 
# both user inputs – one script should use a for loop and the other should use a while loop. 

def main():
    n = int(input("Input number to multiply: "))
    ii = 1
    nn = n * int(input("Enter how many times you wish to multiply it: "))

    while not n.isinstance(n, int):
        try:
            int(n)
        except ValueError:
            print("Invalid, your input must be an integer.")
            n = int(input("Input number to multiply: "))

    while not nn.isinstance(nn, int):
        try:
            int(nn)
        except ValueError:
            print("Invalid, your input must be an integer.")
            nn = n * int(input("Enter how many times you wish to multiply it: "))

    for i in range(1, 12): 
       print(n, "x", i, "=", i*n)
    
    while ii < 12:
        print(n, "x", ii, "=", ii*n)
        ii += 1
        
if __name__ == "__main__":
    main()