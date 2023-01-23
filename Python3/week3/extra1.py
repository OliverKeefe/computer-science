import math

def calculate_hypotenuse(width, height):
    hypotenuse = math.hypot(width, height)
    
    return hypotenuse

def main():
    height = float(input("Enter the Height of the triangle: "))
    width = float(input("Enter the Width of the triangle: "))
    hypotenuse = calculate_hypotenuse(width, height)
    print("The hypotenuse of this triangle is:", hypotenuse)
    angle_a =  math.sin(**-1)

if __name__ == "main":
    main()