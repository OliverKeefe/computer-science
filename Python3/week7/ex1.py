def main():
    month = input("Enter your month: ")
    year = int(input("Enter your year: "))

    def year_function(year):
        leap_year_check = year % 4
        if leap_year_check == 0:
            leap_year = True
        else: 
            leap_year = False

        return leap_year

    def month_function(month):
        if month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
            days = print(month, "has 31 days.")
        elif month == 'April' or month == 'June' or month == 'September' or month == 'November':
            days = print(month, "has 30 days.")
        elif month == 'Febuary' and leap_year == True:
            days = print(month, "has 29 days.")
        elif month == 'Febuary' and leap_year == False:
            days = print(month, "has 28 days.")
        else:
            days = print("Invalid input, it doesn't have any days...") 

        return days

    leap_year = year_function(year)

    if leap_year == True:
        print(year, "is a leap year.")
    else:
        print(year, "isn't a leap year.")

    days = month_function(month)
    print(days)


if __name__ == "__main__":
    main()