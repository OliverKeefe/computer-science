import uuid

class HolidayPackage:
    def __init__(self, customer_name, uid, destination_country, destination_city, people_catered_for, nights, price_per_night, seasonal_discount):
        self.customer_name = customer_name
        self.uid = uid
        self.destination_country = destination_country
        self.destination_city = destination_city
        self.people_catered_for = people_catered_for
        self.nights = nights
        self.price_per_night = price_per_night
        self.seasonal_discount = seasonal_discount

def search_by(criterion, query, database):
    filtered_database = []
    search_results = 0

    for ele in database:
        if ele[criterion] == query:
            filtered_database.append(ele)
            search_results += 1

    query_to_string = str(query)
    results_to_string = str(search_results)
    search_term_info = ("You have searched for: " + query_to_string)
    result_count = ("Search results: " + results_to_string)

    return search_term_info, result_count, filtered_database

# Func that controls the way in which UI and output is displayed in the terminal using the format specification mini-language.
def format_text(text):
    formatted_text = print()

    for ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8 in text:
        formatted_text = print("{:<18}{:<9}{:<24}{:<20}{:<24}{:<12}{:<20}{}".format(ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8))

    return formatted_text

# Func that allows user to delete a database entry by specific header criteria e.g. UID, 
def delete_by(criterion, query, database):
    for ele in database:
        if ele[criterion] == query:
            database.remove(ele)

def sort_tuple_alphabetically(database, criterion):
    n = len(database)

    for i in range(n):
        for ele in range(n-i-1):
            if database[ele][criterion] > database[ele + 1][criterion]:
                database[ele], database[ele + 1] = database[ele + 1], database[ele]

    return database

def main():
    # All options displayed to the user at the main menu screen.
    main_menu_ui = ('\nHoliday Packages Database:', 
        '-+-+-+-+-+-+-+-+-+-+-+-+-', 
        '[a] Enter a new holiday package', 
        '[b] Display inventory (all destinations)', 
        '[c] Search for a holiday package (view details)', 
        '[d] Delete a holiday package', 
        '[e] Show all holiday packages with seasonal discount', 
        '[f] Show all holiday packages with no discount', 
        '[g] Sort inventory A-Z (all destinations)',
        '[h] Show all holiday packages less than specified amount',
        '\n[/q] Quit\n'
        )

    # All options displayed to the user at the search menu screen.
    search_menu_ui = ('\nSearch Menu:', 
        '-+-+-+-+-+-+-+-+-+-+-+-+-', 
        '[a] Customer name', 
        '[b] UID', 
        '[c] Destination country', 
        '[d] Destination city', 
        '[e] People catered for', 
        '[f] Nights', 
        '[g] Price per night',
        '[h] Seasonal discount availability',  
        '\n[/q] Return to Main Menu\n'
        )

    sort_menu_ui = ('\nSort Menu:', 
        '-+-+-+-+-+-+-+-+-+-+-+-+-', 
        '[a] Customer name', 
        '[b] Destination country', 
        '[c] Destination city', 
        '\n[/q] Return to Main Menu\n'
        )

    # All header criteria displayed to the user upon displaying, sorting or searching the database.
    headers = [('CUSTOMER NAME', 
                'UID', 
                'DESTINATION COUNTRY', 
                'DESTINATION CITY', 
                'PEOPLE CATERED FOR', 
                'NIGHTS', 
                '£ PRICE PER NIGHT', 
                'SEASONAL DISCOUNT AVAILABLE?'
                )]

    # Line divider that seperates outputted results from header criteria.
    divider = "-----------------------------------------------------------------------------------------------------------------------------------------------------------"
    menu_choice = ''
    search_menu_choice = ''
    package_database = []

    # Main menu loop
    while menu_choice == '':
        for i in main_menu_ui:
            print(i)
        menu_choice = input("Choose an option (a to h) or /q to Quit\n$:")

        if menu_choice == 'a' or menu_choice == 'A':
            input_customer_name = input("\nCustomer Name $: ")
            input_destination_country = input("Destination Country $: ")
            input_destination_city = input("Destination Town / City $: ")
            input_people_catered_for = input("Number of Guests $: ")

            while not isinstance(input_people_catered_for, int):
                try:
                    input_people_catered_for = int(input_people_catered_for)
                except ValueError:
                    print("\n[!] Invalid input\n")
                    input_people_catered_for = input("Number of Guests $: ")

            input_nights = input("Number of Nights $:")

            while not isinstance(input_nights, int):
                try:
                    input_nights = int(input_nights)
                except ValueError:
                    print("\n[!] Invalid input\n")
                    input_nights = input("Number of Nights $:")

            input_price_per_night = input("Price per Night $: £")

            while not isinstance(input_price_per_night, float):
                try:
                    input_price_per_night = float(input_price_per_night)
                except:
                    print("\n[!] Invalid input\n")
                    input_price_per_night = input("Price per Night $: £")

            input_seasonal_discount_invalid = True

            while input_seasonal_discount_invalid == True:
                input_seasonal_discount = input("\nIs a seasonal discount available for this holiday package? Y/N: ")

                if input_seasonal_discount == 'Y' or input_seasonal_discount == 'y' or input_seasonal_discount == 'Yes' or input_seasonal_discount == 'yes':
                    input_seasonal_discount = 'Yes'
                    print("New holiday package created.")
                    input_seasonal_discount_invalid = False
                    

                elif input_seasonal_discount == 'N' or input_seasonal_discount == 'n' or input_seasonal_discount == 'No' or input_seasonal_discount == 'no':
                    input_seasonal_discount = 'No'
                    print("New holiday package created.")
                    input_seasonal_discount_invalid = False

                else:
                    print("\n[!] Invalid input, please enter Yes or No.\n")
            
            # Assigns a UUID4, shortens the length to 8 chars in length.
            assign_uid = str(uuid.uuid4())
            assign_uid = assign_uid[:len(assign_uid)-28]

            holiday_package = HolidayPackage(
                input_customer_name, 
                assign_uid, 
                input_destination_country, 
                input_destination_city, 
                input_people_catered_for, 
                input_nights, 
                input_price_per_night, 
                input_seasonal_discount
                )
                                             
            holiday_package = tuple((
                holiday_package.customer_name, 
                holiday_package.uid, 
                holiday_package.destination_country, 
                holiday_package.destination_city, 
                holiday_package.people_catered_for, 
                holiday_package.nights, 
                holiday_package.price_per_night, 
                holiday_package.seasonal_discount
                ))

            package_database.append(holiday_package)
            # print(package_database)
            # print(package_database[0])
            menu_choice = ''

        elif menu_choice == 'b' or menu_choice == 'B':
            format_text(headers)
            print(divider)
            format_text(package_database)

            if package_database == []:
                print("The holiday package database is currently empty.")
            
            menu_choice = ''

        elif menu_choice == 'c' or menu_choice == 'C':
            search_menu = True

            while search_menu == True:
                for i in search_menu_ui:
                    print(i)
                input_criterion = -1
                search_menu_choice = (input("Choose an option (a to g) or /q to return to main menu\n$:  "))

                if search_menu_choice == 'a' or search_menu_choice == 'A':
                    input_criterion = 0
                    print("To return to main menu, enter: /q")
                    print("Selected search criterion: Customer Name")
                    input_query = input("$: ")
                    
                    if input_query == '/q' or input_query == '/Q':
                        search_menu = False
                        menu_choice = ''

                elif search_menu_choice == 'b' or search_menu_choice == 'B':
                    input_criterion = 1
                    print("To return to main menu, enter: /q")
                    print("Selected search criterion: UID")
                    input_query = input("$: ")

                    if input_query == '/q' or input_query == '/Q':
                        search_menu = False
                        menu_choice = ''

                elif search_menu_choice == 'c' or search_menu_choice == 'C':
                    input_criterion = 2
                    print("To return to main menu, enter: /q")
                    print("Selected search criterion: Destination Country")
                    input_query = input("$: ")

                    if input_query == '/q' or input_query == '/Q':
                        search_menu = False
                        menu_choice = ''

                elif search_menu_choice == 'd' or search_menu_choice == 'D':
                    input_criterion = 3
                    print("To return to main menu, enter: /q")
                    print("Selected search criterion: Destination City")
                    input_query = input("$: ")

                    if input_query == '/q' or input_query == '/Q':
                        search_menu = False
                        menu_choice = ''

                elif search_menu_choice == 'e' or search_menu_choice == 'E':
                    input_criterion = 4
                    print("To return to main menu, enter: /q")
                    print("Selected search criterion: People Catered For")
                    input_query = input("$: ")

                    while not isinstance(input_query, int):
                        try:
                            input_query = int(input_query)
                        except ValueError:
                            print("\n[!] Invalid input\n")
                    
                    if input_query == '/q' or input_query == '/Q':
                        search_menu = False
                        menu_choice = ''

                elif search_menu_choice == 'f' or search_menu_choice == 'F':
                    input_criterion = 5
                    print("To return to main menu, enter: /q")
                    print("Selected search criterion: Nights")
                    input_query = input("$: ")

                    while not isinstance(input_query, int):
                        try:
                            input_query = int(input_query)
                        except ValueError:
                            print("\n[!] Invalid input\n")

                    if input_query == '/q' or input_query == '/Q':
                        search_menu = False
                        menu_choice = ''

                elif search_menu_choice == 'g' or search_menu_choice == 'G':
                    input_criterion = 6
                    print("To return to main menu, enter: /q")
                    print("Selected search criterion: Price per Night")
                    input_query = input("$: £")

                    while not isinstance(input_query, float):
                        try:
                            input_query = float(input_query)
                        except ValueError:
                            print("\n[!] Invalid input\n")

                    if input_query == '/q' or input_query == '/Q':
                        search_menu = False
                        menu_choice = ''

                elif search_menu_choice == 'h' or search_menu_choice == 'H':
                    input_criterion = 7
                    print("To return to main menu, enter: /q")
                    print("Selected search criterion: Seasonal Discount Availability")

                    while True:
                        print("Would you like to search for holiday packages eligable for seasonal discount or ineligable?\n[a] Eligable for Seasonal Discount\n[b] Ineligable for Seasonal Discount")
                        input_query = input("$: ")

                        if input_query == 'A' or input_query == 'a':
                            input_query = 'Yes'
                            break

                        elif input_query == 'B' or input_query == 'b':
                            input_query = 'No'
                            break

                        else:
                            print("[!] Invalid input")

                        if input_query == '/q' or input_query == '/Q':
                            search_menu = False
                            menu_choice = ''

                    if input_query == '/q' or input_query == '/Q':
                        menu_choice = ''
                        search_menu = False

                elif search_menu_choice == 'q' or search_menu_choice == 'Q' or search_menu_choice == '/q':
                    search_menu = False
                    menu_choice = ''

                else: 
                    print("[!] Invalid input")

                # This if statement ensures that the program does not crash if the user exits this menu before selecting the criteria by which to search by.
                # Also prints output if the user specifies an input query and criterion.
                if input_criterion >= 0:
                    criterion,query,filtered_database = search_by(input_criterion, input_query, package_database)
                    final_criterion = str(criterion)
                    final_query = str(query)
                    format_text(headers)
                    print(divider)
                    print(final_criterion)
                    print(final_query)
                    format_text(filtered_database)

        elif menu_choice == 'd' or menu_choice == 'D':
            print("Enter the UID of the holiday package you wish to remove.")
            delete_package = input("$: ")
            delete_by(1, delete_package, package_database)
            print("Removing", delete_package, "...")
            menu_choice = ''

        elif menu_choice == 'e' or menu_choice == 'E':
            input_criterion = 7
            input_query = 'Yes'
            criterion,query,filtered_database = search_by(input_criterion, input_query, package_database)
            final_criterion = str(criterion)
            final_query = str(query)
            format_text(headers)
            print(divider)
            print(final_criterion)
            print(final_query)
            format_text(filtered_database)
            menu_choice = ''

        elif menu_choice == 'f' or menu_choice == 'F':
            input_criterion = 7
            input_query = 'No'
            criterion,query,filtered_database = search_by(input_criterion, input_query, package_database)
            final_criterion = str(criterion)
            final_query = str(query)
            format_text(headers)
            print(divider)
            print(final_criterion)
            print(final_query)
            format_text(filtered_database)
            menu_choice = ''

        elif menu_choice == 'g' or menu_choice == 'G':
            sort_menu = True
            while sort_menu == True:
                for i in sort_menu_ui:
                    print(i)
                sort_menu_choice = input("Choose an option (a to c) or /q to Quit.\n$: ")
                
                if sort_menu_choice == 'a' or sort_menu_choice == 'A':
                    format_text(headers)
                    print(divider)
                    filtered_a_to_z = format_text(sort_tuple_alphabetically(package_database, 0))
                    print(filtered_a_to_z)
                    # formatted_filtered_a_to_z = format_text(filtered_a_to_z)
                    # final_filtered_a_to_z = print(formatted_filtered_a_to_z)
                    sort_menu = False
                    menu_choice = ''

                elif sort_menu_choice == 'b' or sort_menu_choice == 'B':
                    format_text(headers)
                    print(divider)
                    filtered_a_to_z = format_text(sort_tuple_alphabetically(package_database, 1))
                    print(filtered_a_to_z)
                    sort_menu = False
                    menu_choice = ''

                elif sort_menu_choice == 'c' or sort_menu_choice == 'C':
                    format_text(headers)
                    print(divider)
                    filtered_a_to_z = format_text(sort_tuple_alphabetically(package_database, 2))
                    print(filtered_a_to_z)
                    sort_menu = False
                    menu_choice = ''

                elif sort_menu_choice == 'q' or sort_menu_choice == 'Q' or sort_menu_choice == '/q':
                    sort_menu = False
                    menu_choice = ''

                else:
                    print("\n[!] Invalid input.\n")

        elif menu_choice == 'h' or menu_choice == 'H':
            input_max_cost = input("Enter the maximum holiday cost.\n$: £")

            while not isinstance(input_max_cost, float):
                try:
                    input_max_cost = float(input_max_cost)
                except ValueError:
                    print("\n[!] Invalid input\n")
                    input_max_cost = input("Enter the maximum holiday cost.\n$: £")

            filtered_database = []
            filter_results = 0

            for ele in package_database:
                if (ele[6] * ele[4]) * ele[5] <= input_max_cost:
                    filtered_database.append(ele)
                    filter_results += 1

            max_cost_to_string = str(input_max_cost)
            results_to_string = str(filter_results)
            search_term_info = ("You have searched for holidays packages costing less than: " + max_cost_to_string)
            result_count = ("Search results: " + results_to_string)
            format_text(headers)
            print(divider)
            print(search_term_info)
            print(result_count)
            format_text(filtered_database)
            menu_choice = ''

        elif menu_choice == 'q' or menu_choice == 'Q' or menu_choice == '/q':
            print("Goodbye!")
            exit()

        else:
            print("[!] Invalid input.")
            print("Please select menu options a - h or /q to quit.")

if __name__ == "__main__":
    main()
