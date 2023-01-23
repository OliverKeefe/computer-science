def main():
    s = input("Input your sentence: ")
    l = list(s)
    print(l)

    vowels = 0
    constenants = 0

    #a, e, i, o, u, A, E, I, O, U
    for i in l:
        if i == 'a' or i == 'e' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'O' or i == 'U':
            vowels += 1
        else:
            constenants += 1
    
    print("Contains", vowels, "Vowels.")
    print("Contains", constenants, "Constenants.")

if __name__ == "__main__":
    main()