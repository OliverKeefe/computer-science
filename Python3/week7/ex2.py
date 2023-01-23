def main():
    original_string = input("Enter a word: ")
    reverse_string = original_string[::-1]

    if reverse_string == original_string:
        print(original_string, "is a palindrome!")
    else:
        print(original_string, "is not a palindrome.")

if __name__ == "__main__":
    main()