def fact_5(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result

def main():
    n = 5
    try:
        print(fact_5(n))
    except ValueError:
        print("[!] Error, input must be an integer number.")
    

if __name__ == "__main__":
    main()