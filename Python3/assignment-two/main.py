def load_file(filepath):
    with open(filepath, 'r') as file:
        contents = file.read()
        return contents

def main():
    menu_choice = ''
    main_menu_ui = [
        "Sudoku Puzzle Board Validator",
        "[1] Import a puzzle board file",
        "[2] Save a puzzle board file",
        "[Q] Quit"
    ]
    
    while menu_choice == '':
        for i in main_menu_ui:
            print(i)
        menu_choice = input("Please select an option. $: ")
        if menu_choice == "1":
            filepath = input("Please enter your puzzle board file's path. $: ")
            print("[*] Attempting to import file...")
            try:
                print(load_file(filepath))
                print("[+] Success, file imported corectly.")
            except FileExistsError:
                print("[!] Error, the specified file does not exist. Is the file path correct?..")

if __name__ == "__main__":
    main()