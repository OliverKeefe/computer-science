def main_menu():
    menu_ui = [
        "\nTelephone Directory\n",
        "Main Menu",
        "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-",
        "[1] Create new phone contact",
        "[2] Display all contacts",
        "[3] Search",
        "[4] Delete a contact",
        "[Q] Quit"
    ]

    for i in menu_ui:
        print(str(i))

def create_dict(name, number):
    return {name: number}

def search_key(dictionary, query):
    return [key for key, query in dictionary.items() if query == key]

def search_value(dictionary, value):
    return [key for key, val in dictionary.items() if val == value]

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
        elif choice == 'q' or choice == 'Q':
            print("You have selected: Option [Q] Exiting...")
            exit()
        else:
            print("[!] Invalid option...")
            

if __name__ == "__main__":
    main()