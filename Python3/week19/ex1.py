"""
Exercise 1
1. Create a new directory called ‘Week 19’, and in that directory create a new plain text file
called myhome.txt using TextPad or any similar simple text editor (not MS Word). In the text
file, write five lines of text that describes your home town.
2. Write a new Python program that can open this text file, myhome.txt, read its contents, and
output (print) it to the screen.
3. Add some code to your Python program that will add some new text to the end of the text file,
myhome.txt. The text you write to the file should include the current date and your name.
Open the now modified text file in another application (TextPad for example) to check the
modification works as you would expect.
4. In the same Python script define a new function called uppercase() that will read the
contents from the text file, myhome.txt, translate all of the text to uppercase, and write this
to a new text file, myhome2.txt.
Now write a function call at the end of your script to test your uppercase() function. Open
the new text file in another application to check it works as you would expect.
5. In the same Python script define a new function called insert() that prompts the user to
enter a line of text. The function should translate this text to uppercase, and then add this to
the start of the text file myhome2.txt.
Now write a function call at the end of your script to test your insert() function. And again,
open the text file in another application to check the modification works as you would expect.
Note: there is no easy built-in function in Python that inserts text at a given position in a file.
Hint: to solve this task think about what the final file should look like and how you would
construct that file from scratch """

import datetime

def insert(filename, arg, text):
    with open(filename, arg) as file:
        file.write(text)

def read_file(filename):
    with open(filename, 'r') as file:
        contents = file.read()
        return contents

def output_file_contents(filename):
    with open(filename, 'r') as file:
        return file.read()

def uppercase(text):
    return text.upper()

def main():
    file = "myhome.txt"

    # 'a' - Append file, 'w' - Write file (overwrites whatever previously written etc...)
    while True:
        user_input = input("Enter some text to append it to the myhome.txt file or /q to quit$: ")
        if user_input == '/q':
            print("Exiting...")
            exit()

        try:
            user_input = uppercase(user_input)
            contents = output_file_contents(file)
            insert(file, 'w', user_input + " ")
            insert(file, 'a', contents)
        except ValueError:
            print("[!] Error, invalid input.")
          
        print(output_file_contents(file))

if __name__ == "__main__":
    main()