def main():
    x = 'X'
    n = int(input("Enter the number of X's you want printed: "))
    max_count = 0

    while True:
        if max_count < n:
            print(x * n)
            max_count += 1
        elif max_count >= n:
            break
        else:
            pass

if __name__ == "__main__":
    main()