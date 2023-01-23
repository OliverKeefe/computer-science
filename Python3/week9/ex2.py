def main():
    student_names = []
    choice = ''

    while True:
        print()
        print(" Student List Program:\n", "-+-+-+-+-+-+-+-+-+-+-+-+-\n", "[a] : Add new students \n", "[b] : Show student list\n", "[c] : Delete student\n", "[X] : Exit\n",)
        choice = (input("Select menu option: "))
        if choice == 'a':
            user_input = input("Enter your student names here: ")
            if user_input == '' or user_input == ' ':
                print("Your students are: ")
                choice = ''
            else:    
                student_names.append(user_input)
        elif choice == 'b':
            print("Your student are: ")
            for i in student_names:
                print(i, end="\n")
            choice = ''
        elif choice == 'c':
            remove_name = input("Enter the student name you wish to remove: ")
            if remove_name != '' and remove_name in student_names:
                student_names.remove(remove_name)
            else:
                print("[!] Student could not be found...")  
            choice = ''
        elif choice == 'X' or choice == 'x':
            exit()
        else:
            print("[!] Invalid input!")
            print("[!] Please try entering an option from the menu!")

if __name__ == "__main__":
    main()
    # Fixed to show error when student doesn't exist
    