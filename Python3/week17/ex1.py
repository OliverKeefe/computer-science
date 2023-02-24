# Define a new function called find_longest_word() that takes a string as a parameter; the
# function needs to split the string into individual words, and then return the word with the most
# characters from the string. (In cases where there are more than one word with the most characters,
# the function should return the word that appears first in the string).
# You will need to write a simple program with a suitable function call to test your
# find_longest_word() function

def find_longest_word(string):
    string_to_list = string.split()
    longest_word = max(string_to_list, key=len)
    
    if all(len(word) == len(longest_word) for word in string_to_list):
        return "All strings are the same length"
    else:
        return str("The longest word is: " + longest_word)
    
def main():
    user_string = input("Enter a sentence: ")
    try:
        print(find_longest_word(user_string))
    except ValueError:
        print("[!] Invalid input.")
        user_string = input("Enter a string: ")
        
if __name__ == "__main__":
    main()