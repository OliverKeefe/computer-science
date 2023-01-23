
def check_input_valid(user_input):
    try:
        float(user_input)
        return True
    except ValueError:
        return False

def main():
    charge_modifier = False
    final_charge = 0
    final_message = "Your package shipment will cost:"
    
    while True:
        parcel_weight = (input("Enter your parcel weight in Kilograms: "))
        if check_input_valid(parcel_weight) == True:
            parcel_weight = float(parcel_weight)
            break
        elif check_input_valid(parcel_weight) == False:
            print("[!] Inalid input...")

    while True:
        air_shipment = input("Do you wish to select air shipment? This will incur 50% additional charge! Y/N? [Default: N] : ")
        
        if air_shipment == 'N' or air_shipment == 'No' or air_shipment == 'n':
            charge_modifier = False
            print("[*] Air shipment not selected...")
        elif air_shipment == 'Y' or air_shipment == 'Yes' or air_shipment == 'y':
            charge_modifier = True
            print("[!] Warning: Air shipment selected! This will incur 50% additional charge.")
        elif charge_modifier == False:
            print("[*] Air shipment was not selected...")
        if parcel_weight < 2.5:
            final_charge = 4.95
        elif parcel_weight >= 2.5 and parcel_weight < 10:
            final_charge = 8.95
        elif parcel_weight >= 10 and parcel_weight < 30:
            final_charge = 15.95
        elif parcel_weight >= 30 and parcel_weight < 40:
            final_charge = 22.95
        elif parcel_weight >= 41:
            print("[!] Your parcel is too heavy, please use a different courier...")
            break
        if charge_modifier == True:
            print(final_message, "£", (final_charge * 0.5) + round(final_charge))
            break
        elif charge_modifier == False:
            print(final_message, "£", round(final_charge, 2))
            break

if __name__ == "__main__":
    main()

    #  fix! - Needs error message or loop if someone enters invalid input