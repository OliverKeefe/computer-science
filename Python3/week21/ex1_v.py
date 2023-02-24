def fact_q(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result

def main():
    while True:
        q = input("Enter an integer. $: ")

        try:
            q = int(q)
            print(fact_q(q))
        except ValueError:
            print("[!] Error, input must be an integer number.")
    

if __name__ == "__main__":
    main()