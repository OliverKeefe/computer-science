def profit(current_price, purchase_price, shares):
    purchase_price *= shares
    current_price *= shares
    p = purchase_price - current_price
    return p

def loss(purchase_price, current_price, shares):
    purchase_price *= shares
    current_price *= shares
    l = purchase_price - current_price 
    return l

def main():
    portfolio= [
        ( "23-Aug-2019", 43.50, 25, 'CAT', 92.45 ),
        ( "15-Mar-2017", 42.80, 50, 'DD', 51.19 ),
        ( "7-Dec-2018", 42.10, 75, 'EK', 34.87 ),
        ( "6-Dec-2017", 37.58, 100, 'GM', 37.58 )
    ]
    stock_one = portfolio[0]
    stock_two = portfolio[1]
    stock_three = portfolio[2]
    stock_four = portfolio[3]
    (purchase_date_one, purchase_price_one, shares_one, symbol_one, current_price_one) = stock_one
    (purchase_date_two, purchase_price_two, shares_two, symbol_two, current_price_two) = stock_two
    (purchase_date_three, purchase_price_three, shares_three, symbol_three, current_price_three) = stock_three
    (purchase_date_four, purchase_price_four, shares_four, symbol_four, current_price_four) = stock_four
    profit_one = False
    profit_two = False
    profit_three = False
    profit_four = False

    pl_one = profit(purchase_price_one, current_price_one, shares_one)
    pl_two = profit(purchase_price_two, current_price_two, shares_two)
    pl_three = profit(purchase_price_three, current_price_three, shares_three)
    pl_four = profit(purchase_price_four, current_price_four, shares_four)
    choice = ''

    while choice == '':
        print("\nMain Menu\n")
        print("Number Sequences:\n-+-+-+-+-+-+-+-+-+-+-+-+-\n", "[1] : Portfolio Details \n", "[2] : Total Portfolio Value\n", "[Q] : Quit\n",)
        choice = (input("Select menu option: "))

        if choice == '1':
            print("Portfolio:")
            print("----------------------------------------------------------------")
            print("Stock:", symbol_one, "| Purchased on:", purchase_date_one, "| Position size:", shares_one)
            print("\n", "Purchase price per share: $", purchase_price_one, "\n", "Current market price: $", current_price_one, "\n Position P&L: $", pl_one)
            print("----------------------------------------------------------------")
            print("Stock:", symbol_two, "| Purchased on:", purchase_date_two, "| Position size:", shares_two)
            print("\n", "Purchase price per share: $", purchase_price_two, "\n", "Current market price: $", current_price_two, "\n Position P&L: $", pl_two)
            print("----------------------------------------------------------------")
            print("Stock:", symbol_three, "| Purchased on:", purchase_date_three, "| Position size:", shares_three)
            print("\n", "Purchase price per share: $", purchase_price_three, "\n", "Current market price: $", current_price_three, "\n Position P&L: $", pl_three)
            print("----------------------------------------------------------------")
            print("Stock:", symbol_four, "| Purchased on:", purchase_date_four, "| Position size:", shares_four)
            print("\n", "Purchase price per share: $", purchase_price_four, "\n", "Current market price: $", current_price_four, "\n Position P&L: $", pl_four)
            print("----------------------------------------------------------------")
            choice = ''
        elif choice == '2':
            print("$", pl_one + pl_two + pl_three + pl_four)
            choice = ''
        elif choice == 'Q' or choice == 'q':
            exit()
        else:
            print("[!] Invalid input!")
            print("[!] Please try entering another character!")


if __name__ == "__main__":
    main()