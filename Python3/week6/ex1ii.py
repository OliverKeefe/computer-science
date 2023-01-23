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
        print(month, "Isn't a month...")
 
if __name__ == "__main__":
    main()