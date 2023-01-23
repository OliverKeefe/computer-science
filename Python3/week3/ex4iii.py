import math

def calculate_volume(height, diameter):  
    radius = diameter / 2
    volume = math.pi * pow(radius,2) * height
    return volume

def main():
    user_input_one = (float(input("Enter the Height: ")))
    user_input_two = (float(input("Enter the Diameter: ")))

    print("The volume of your cylinder is:", round(calculate_volume(user_input_one, user_input_two), 2))

if __name__ == "__main__":
    main()