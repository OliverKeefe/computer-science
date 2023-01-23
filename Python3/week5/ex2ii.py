def main():
    # x = input("Enter your sentence: ")
    x = "The University of Essex is great!"

    y = x.split()
    print(y)
    for i in y:
        # print(i, end=", ")
        print(i, " - ", len(i))
        

if __name__ == "__main__":
    main()