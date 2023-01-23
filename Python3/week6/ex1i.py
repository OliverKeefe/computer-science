def main():
    num_one = float(input("Enter your first number: "))
    num_two = float(input("Enter your second number: "))

    if num_one > num_two:
        print("The first number, is bigger...")
    elif num_one == num_two:
        print("Both numbers are the same...")
    else:
        print("The second number, is bigger...")

if __name__ == "__main__":
    main()
    #Fixed