"""
Exercise 1 – Character Search


1. Write a program to prompt the user to enter a string (one single word or a short phrase) and
store this in a variable. Then prompt the user to enter a single character (one letter). The
program should then search the original string for the character and simply output whether or
not the character exists in the string.


2. Next, modify the program to then search the string for the character and output how many
times the character exists in the stored string.


3. Modify the program again to now output the stored string, showing instances of the entered
character and an underscore for the other remaining letters (spaces should be displayed as
spaces).
For example, the phrase "Hello World" with the chosen letter 'l' would display:
_ _ l l _ _ _ _ l _


4. Add some simple validation to the program to prevent the user from entering punctuation
characters in both the string and the search character (i.e. only allow letters a-z and spaces).

Modify the program from the Character Search Exercise above to allow for further search characters
to be entered one at a time (until the user enters a blank string ""). As each search character is
entered the program should either output a suitable message if it does not exist in the stored string,
or it should output the string with the characters entered showing. For example: if the secret string is

“Computer Programming” then the program output could be:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
Enter a character: m
_ _ m _ _ _ _ _ _ _ _ _ _ _ m m _ _ _
Enter a character: e
_ _ m _ _ _ e _ _ _ _ _ _ _ m m _ _ _
Enter a character: b
Sorry 'b' does not exist in the phrase
Enter a character: o
_ o m _ _ _ e _ _ _ o _ _ _ m m _ _ _
Enter a character: p
_ o m p _ _ e _ p _ o _ _ _ m m _ _ _

Etc...

"""


# need func to pass json to dict
# func to randomly select a word and definition
# func to split randomly selected word into list or tuple of chars 
# func to prompt to take user input and compare against whether char in answer and if user has enough goes left
#  
import json

def json_to_dict(filename):
    with open(filename, 'r') as json_file:
        json_string = json_file.read()
    
    data = json.loads(json_string)
    result = {item['word']: item['definition'] for item in data}

    return result

def main_menu():
    return 0

def main():    
    wordlist_dict = {}
    hangman_logo = ["HANGMAN"]
    
    menu_ui = [

    ]

    while True:
        for i in menu_ui:
            print(i)

    wordlist_dict = json_to_dict("oxford_dictionary.json")
    print(wordlist_dict)

    

if __name__ == "__main__":
    main()
