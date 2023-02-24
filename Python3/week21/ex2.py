def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

def main():

    while True:
        user_input = input("Enter an integer. $: ")
        try:
            user_input = int(user_input)
            print(recursive_factorial(user_input))
        except ValueError:
            print("[!] Error, input must be an integer number.")
        
if __name__ == "__main__":
    main()