def main():
    
    while True: 
        number = float(input("Enter a number, any number: "))

        if number > 0:
            print(number, "is positive...")
        elif number < 0:
            print(number, "is negative...")
        elif number == 0:
            print("You have entered 0... Goodbye!..")
            break

if __name__ == "__main__":
    main()