#2. 
import math

def calculate_area_x(height, width):
    area_one = height * width
    return area_one

def calculate_area_z(height, length):
    area_three = height * length
    return area_three

def calculate_area_y(length, width):
    area_two = length * width
    return area_two

def calculate_volume(length, width, height):
    volume = length * width * height
    return volume

def main():
    user_input_one = (int(input("Enter the Length: ")))
    user_input_two = (int(input("Enter the Height: ")))
    user_input_three = (int(input("Enter the Width: ")))

    print("Your inputted values are:", user_input_one, user_input_two, user_input_three)
    print("Area of each side on the Y axis:", calculate_area_y(user_input_two, user_input_three))
    print("Area of each side on the X axis:", calculate_area_x(user_input_one, user_input_three))
    print("Area of each side on the Z axis:", calculate_area_z(user_input_one, user_input_two))
    print("Volume is:", calculate_volume(user_input_one, user_input_two, user_input_three))
    
if __name__ == "__main__":
    main()