def main():
    month = input("Enter a month, e.g. September... : ")

    if month == 'November' or month == 'December' or month == 'January' or month == 'Febuary':
        print(month, "is in Winter.") 
    elif month == 'March' or month == 'April' or month == 'May':
        print(month, "is in Spring.")
    elif month == 'June' or month == 'July' or month == 'August':
        print(month, "is in Summer.")
    elif month == 'September' or month == 'October':
        print(month, "is in Autumn.")
    else:
        print(month, "Is not a month...")
 

    if month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
        print(month, "has 31 days.")
    elif month == 'April' or month == 'June' or month == 'September' or month == 'November':
        print(month, "has 30 days.")
    elif month == 'Febuary':
        print(month, "has 28 days.")
    else:
        print("Subsequently, it doesn't have any days...") 

if __name__ == "__main__":
    main()