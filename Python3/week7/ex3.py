import string

def is_palindrome(phrase):
    phrase = phrase.lower().translate(str.maketrans("", "", string.punctuation))
    return phrase == phrase[::-1] # Fixed, abstracted whole thing to a function, original was convoluted.
 
def main():
    user_input = input("Enter a string to ascertain whether it's a palindrome: ")

    if is_palindrome(user_input) == True:
        print(user_input, "is a palindrome.")
    else: 
        print(user_input, "is not palindrome.")

if __name__ == "__main__":
    main()