"""3
Exercise 3
You should not use any imported modules to complete this exercise.
1. Make sure you have completed the telephone directory exercise from last week (Week 18,
Exercise 2). Make a copy of your code to use in this exercise.
2. Add two new options to the menu system in your telephone directory program; one called
“Save Data” and the other called “Load Data”. The “Save Data” option should make a function
call to a function named savedata() and the “Load Data” option should make a function call
to a function named loaddata().
3. In your program define a new function called savedata() that will write the contents of the
telephone directory (the Python dictionary) to a new text file, telephone.txt. To achieve
this, you will need to find a suitable method for reading the data out of the Python dictionary
data structure and format it appropriately for the text file.
4. In your program define another new function called loaddata() that will read the contents of
a text file, telephone.txt, and insert this content back into the telephone directory (the
Python dictionary) in the correct format/structure identical to that of the original program. To
test this function you will need to first save some data into the telephone.txt file using the
savedata() function above, and then exit and restart your telephone directory program.
Hint: you might need to adjust the savedata() function to make the loaddata() function
easier to write; just remember that any changes you make to one function will likely affect the
other."""

# def read_file(filename):
#     with open(filename, 'r') as file:
#         contents = file.read
# 
#         return contents

def save_data(dictionary, file_path):
    with open(file_path, 'w') as file:
        for key, value in dictionary.items():
            file.write(f"{key}:{value}\n")

def load_data(file_path):
    loaded_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split(':')
            loaded_dict[key] = value
    return loaded_dict

def main_menu():
    menu_ui = [
        "\nTelephone Directory\n",
        "Main Menu",
        "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-",
        "[1] Create new phone contact",
        "[2] Display all contacts",
        "[3] Search",
        "[4] Delete a contact",
        "[5] Save data",
        "[6] Load data",
        "[Q] Quit"
    ]

    for i in menu_ui:
        print(str(i))

def create_dict(name, number):
    return {name: number}

def main():
    telephone_directory = {}
    header = "Name      " + "   Telephone Number"
    divider = "-" * len(header)
    while True:
        main_menu()
        choice = input("\nPlease select options 1 - 5 or Q to quit.\n$:")
        if choice == '1':
            print("You have selected: Option [1] Create new contact...")
            name = input("Contact name. $: ")
            telephone_number = input("Contact telephone number. $: ")
            try:
                telephone_number = int(telephone_number)
            except ValueError:
                print("[!] Inavlid input, please enter a valid telephone number")
                telephone_number = input("Contact telephone number. $: ")
            
            d = create_dict(name, telephone_number)
            telephone_directory.update(d)
            print(telephone_directory)

        elif choice == '2':
            print("You have selected: Option [2] Display all contacts...")
            print(header)
            print(divider)

            for key, value in telephone_directory.items():
                print(key, ' : ', value)
            print("\n")

        elif choice == '3':
            print("You have selected: Option [3] Search...")
            search_for = input("Which contact's number would you like to search for? $: ")
            print("The telephone number for", search_for, "is:", telephone_directory[search_for],"\n")

        elif choice == '4':
            print("You have selected: Option [4] Delete a contact...")
            delete = input("Which contact would you like to remove? $: ")

            if delete in telephone_directory:
                telephone_directory.pop(delete, None)
                print(delete, "has been deleted.")

        elif choice == '5':
            save_file = input("Enter the path in which you wish to save your data $: ")
            try:
                telephone_directory = load_data(save_file)
            except ValueError:
                print("[!] Inavlid file path.")
                save_file = input("Enter the path to your data file $: ")
            
        elif choice == '6':
            print("You have selected: Option [6] Load data...")
            save_file = input("Enter the path in which you wish to save your data $: ")
            try:
                telephone_directory = load_data(save_file)
            except ValueError:
                print("[!] Inavlid file path.")
                save_file = input("Enter the path to your data file $: ")
        
        elif choice == 'q' or choice == 'Q':
            print("You have selected: Option [Q] Exiting...")
            exit()
        else:
            print("[!] Invalid option...")
            

if __name__ == "__main__":
    main()
