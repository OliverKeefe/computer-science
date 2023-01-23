def main():

    string_list = []

    while True:
        user_input = input("Enter a word for the sentence: ")

        if user_input == 'stop' or user_input == 'Stop' or user_input == 'STOP':
            result = ' '.join(string_list)
            print(result)
            exit()

        else:  
            string_list.append(user_input)


if __name__ == "__main__":
    main()