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
import random

def json_to_dict(filename):
    with open(filename, 'r') as json_file:
        json_string = json_file.read()
    
    data = json.loads(json_string)
    result = {item['word']: item['definition'] for item in data}
    return result

def select_random(filename):
    with open(filename, 'r') as file:
        json_data = json.load(file)
        random_entry = random.choice(json_data)
        word = random_entry['word']
        definition = random_entry['definition']
        wordlist_dict = {word: definition}
        return wordlist_dict

def game_config(wordlist_dict):
    for key, value in wordlist_dict.items():
        word = key
        definition = value
        word_length = len(word)
        word_to_tuple = tuple(word)
        underscores = "_" * word_length
        underscores_to_list = list(underscores)
    return word, definition, word_to_tuple, underscores_to_list

def char_to_list(user_input, word_to_tuple, underscores_to_list):
    # Check if user_input is inside wordlist_dict
    # if true, get position in tuple, e.g. [2]
    # replace underscores_to_list[2] with word_to_tuple[2] 
    indices = [i for i, x in enumerate(word_to_tuple) if x == user_input]
    for index in indices:
        underscores_to_list[index] = user_input
    return underscores_to_list

def main_menu():
    return 0

def main():    
    debugging = False # Set true for verbose print messages
    wordlist_dict = {}
    word = ""
    definition = ""
    word_to_tuple = ()
    underscores_to_list = []
    hangman_logo = ["HANGMAN"]
    menu_ui = [
        '[1] Singleplayer',
        '[2] Multiplayer',
        '[Q] Exit Game'
    ]
    menu_choice = ''
    lives = 20
    oxford_dictionary = "oxford_dictionary.json"
    turn_count = 1

    while menu_choice == '':
        for i in menu_ui:
            print(i)
        menu_choice = input("Enter the gamemode you wish to play. $: ")

        while menu_choice == '1':
            print("[*] Singplayer mode selected")
            print("[*] Generating word challenge...")
            wordlist_dict = select_random(oxford_dictionary)
            if debugging == True:
                print(wordlist_dict)
            print("[+] Success!\n")
            word, definition, word_to_tuple, underscores_to_list = game_config(wordlist_dict)
            print(word, definition, word_to_tuple, underscores_to_list)

            while lives >= 1 and "_" in underscores_to_list:
                for i in word_to_tuple:
                    print(f"\nLives remaining: {lives}")
                    if debugging == True:
                        print(word_to_tuple)
                    print(" ".join(underscores_to_list))
                    user_input = input("Enter the letter you wish to try. $: ")
                    underscores_to_list = char_to_list(user_input, word_to_tuple, underscores_to_list)
                    lives -= 1
                    # Function that swaps char in tuple with _ in list and deducts a life from lives variable
                
            if lives == 0 and "_" in underscores_to_list:
                print("Wah wah, you've lost...")
                print("The word was:", word + "\n which means", definition)
                menu_choice = ''

            elif not "_" in underscores_to_list:
                print("You win!")
                print("The word was:", word, "which means:", definition)
                menu_choice = ''
    if menu_choice == 'Q' or menu_choice == 'q':
        print("[*] Quitting...")
        exit()

    else:
        print("[!] Error, invalid option.")
        menu_choice = ''

if __name__ == "__main__":
    main()


