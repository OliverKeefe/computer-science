#1. 
import math

def calculate_volume(user_input):
    volume = (4/3) * math.pi * (user_input**3)
    return volume

def main():
    user_input = (float(input("Enter the radius of the sphere: ")))
    print(calculate_volume(user_input))

if __name__ == "__main__":
    main()