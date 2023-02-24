def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result

def main():
    
    while True:
        user_input = input("Enter an integer. $: ")

        try:
            user_input = int(user_input)
            print(factorial(user_input))
        except ValueError:
            print("[!] Error, input must be an integer number.")
    

if __name__ == "__main__":
    main()