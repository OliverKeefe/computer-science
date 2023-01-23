import string

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def main():
    original_string = input("Enter a word or phrase: ")
    print(original_string)
    lowercase_string = original_string.lower()
    print(lowercase_string)
    for i in lowercase_string:
        if i in punc:
            new_string = lowercase_string.replace(i, "")
        else:
            new_string = lowercase_string
    print(new_string)
    reverse_string = new_string[::-1]
    print(reverse_string)

    if reverse_string != new_string:
        print("This word / phrase is not a palindrome.")
    else:
        print("This word / phrase is a palindrome!")

if __name__ == "__main__":
    main()

    #Fixed! Yay! 