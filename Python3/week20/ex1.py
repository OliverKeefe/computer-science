def save_data(dictionary, file_path):
    try:
        with open(file_path, 'w') as file:
            for key, value in dictionary.items():
                file.write(f"{key}:{value}\n")
    except FileNotFoundError:
        print("[!] Error, Invalid file path.")

def load_data(file_path):
    to_dict = {}
    try: 
        with open(file_path, 'r') as file:
            for line in file:
                key, value = line.strip().split(':')
                to_dict[key] = value
    except FileNotFoundError:
        print("[!] Error, file not found.")
    except ValueError:
        to_dict = {}
    
    return to_dict

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
            print("You have selected: Option [5] Save data...")
            save_file = input("Enter the path in which you wish to save your data $: ")
            try:
                save_data(telephone_directory, save_file)
            except ValueError:
                print("[!] Inavlid file path.")
                save_file = input("Enter the path in which you wish to save your data $: ")

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