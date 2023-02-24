def fact_p(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result

def main():
    p = 5
    while True:
        p = input("Enter an integer. $: ")

        try:
            p = int(p)
            print(fact_p(p))
        except ValueError:
            print("[!] Error, input must be an integer number.")
    

if __name__ == "__main__":
    main()