#1. 
def kilograms_to_pounds(weight_in_kilograms):
    weight_in_pounds = weight_in_kilograms * 2.20462262
    
    return weight_in_pounds

#2.
def pounds_to_kilograms(weight_in_pounds):
    weight_in_kilograms = weight_in_pounds / 2.20462262
    
    return weight_in_pounds

#3. 
def kilometres_to_miles(distance_in_kilometres):
    distance_in_miles = distance_in_kilometres * 0.621371
    
    return distance_in_miles

#4. 
def miles_to_kilometres(distance_in_miles):
    distance_in_kilometres = distance_in_miles / 0.621371
    
    return distance_in_kilometres

#5.
def celsius_to_fahrenheit(temperature_in_celsius):
    temperature_in_fahrenheit = (temperature_in_celsius * 1.8) + 32
    
    return temperature_in_fahrenheit

#6. 
def fahrenheit_to_celsius(temperature_in_fahrenheit):
    temperature_in_celsius = (temperature_in_fahrenheit -32) * 5/9
    
    return temperature_in_celsius


def main():
    user_input = (float(input("Input the value you wish to convert: ")))
    print("lbs to kg:", user_input,"lbs, is equal to:", kilograms_to_pounds(user_input), "kg")
    print("kg to lbs:", user_input, "kg, is equal to:", pounds_to_kilograms(user_input), "lbs")
    print("km to miles:", user_input,"km, is equal to:", kilometres_to_miles(user_input), "miles")
    print("miles to km:", user_input,"miles, is equal to:", miles_to_kilometres(user_input), "km")
    print("celsius to fahrenheit:", user_input,"celsius, is equal to:", celsius_to_fahrenheit(user_input), "fahrenheit")
    print("fahrenheit to celsius:", user_input,"fahrenheit, is equal to:", fahrenheit_to_celsius(user_input), "celsius")

if __name__ == "__main__":
    main()
