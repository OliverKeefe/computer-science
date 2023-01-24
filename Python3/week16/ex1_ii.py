# 2. Write two Python scripts to output the first 12 entries in the n times table, where n is an input 
# from the user – one script should use a for loop and the other should use a while loop. 

def main():
    n = int(input("Input number to multiply: "))
    ii = 1
    nn = n * 12

    for i in range(1, 12): 
       print(n, "x", i, "=", i*n)
    
    while ii < 12:
        print(n, "x", ii, "=", ii*n)
        ii += 1
        
if __name__ == "__main__":
    main()