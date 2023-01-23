def main():

    capital = float(input("Enter your investment principal in GBP: £"))
    interest_rate = float(input("Enter your interest rate out of 100: "))
    interest_rate = interest_rate / 100
    year_count = 1
    target_year_count = int(input("How many years do you wish to invest for? : "))

    def interest_calculator(principal, interest):
        annual_interest = (principal * interest) + principal
        return annual_interest

    while year_count <= target_year_count:
        print("Year: ", year_count, "£", capital)
        capital = round(interest_calculator(capital, interest_rate), 2)
        year_count += 1

if __name__ == "__main__":
    main()