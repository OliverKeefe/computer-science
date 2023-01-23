import string

def main():
    english_alphabet = list(string.ascii_lowercase)
    user_input = input("Enter your sentence: ")
    converted_string = user_input.lower()

    def determine_if_pangram(str):
        for char in english_alphabet:
            if char not in str:
                return False
            else:
                return True

    if (determine_if_pangram(converted_string) == True):
        print(user_input, " - is a pangram! Woo!")
    else:
        print(user_input, " - is not a pangram, sorry.")
    
if __name__ == "__main__":
    main()