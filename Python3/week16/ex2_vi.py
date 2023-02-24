# 6. Write a new function definition that takes a character (i.e. a string of length 1) as a parameter 
# and returns a Boolean value True if it is a vowel, or False if it is not. Write a simple program 
# to test the function. 

def vowel_or_no_vowel(char):
    vowels = ("a", "e", "i", "o", "u")

    is_vowel = False

    for i in vowels:
        if i == char:
            is_vowel = True
    
    return is_vowel

def main():
    input_char = input("Input a character to test if it's a vowel: ")
    if len(input_char) > 1:
        len_char = len(input_char) - 1
        input_char = input_char[:len(input_char)-len_char] 

    print(vowel_or_no_vowel(input_char))

if __name__ == "__main__":
    main()