print("This program will tell you how many years it will take for an") 
print("initial investment of £500 to reach £1000 if the interest rate is 6%") 
print()

balance = float(input("Enter your balance: ")) 
years = 1
target = float(input("Enter your target value: "))
interest_rate = float(input("Enter the interest rate out of 100: "))
interest_rate = interest_rate / 100
print(interest_rate)

if target < balance:
    print("Invalid input, your starting balance is greater than your target!..")
    exit()


while (balance < target): 
    balance = balance + (balance * interest_rate) 
    print(years, "£", round(balance, 2))
    years = years + 1 

print("It will take", years - 1, "years for your investment to reach", target) 

# Re-read question and fixed! - Now actually works! Woo!