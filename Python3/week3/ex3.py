import math

def radius_to_area(radius):
    area = math.pi * (radius**2)
    return area

def diameter_to_radius(diameter):
    area = math.pi * ((diameter / 2) **2)
    return area

def hypotenuse(width, height):
    hypotenuse = math.hypot(width, height)
    return hypotenuse

def main():
    radius = 4
    diameter = 26
    width = 10
    height = 5
    print(radius_to_area(radius), diameter_to_radius(diameter), hypotenuse(width, height))
    
if __name__ == "__main__":
    main()