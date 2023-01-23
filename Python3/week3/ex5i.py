# # import math module  
# import cmath  
# a = float(input('Enter a: '))  
# b = float(input('Enter b: '))  
# c = float(input('Enter c: '))  
#   
# # calculate the discriminant  
# d = (b**2) - (4*a*c)  
#   
# # find two solutions  
# sol1 = (-b-cmath.sqrt(d))/(2*a)  
# sol2 = (-b+cmath.sqrt(d))/(2*a)  
# print('The solution are {0} and {1}'.format(sol1,sol2))   

# 34x^2 + 68x - 510
# x1 = -b + sqrt /(b^2 - 4ac) / 2a

import cmath


def main():
    a = float(input("Input value for coefficient a: "))
    b = float(input("Input value for coefficient b: "))
    c = float(input("Input value for coefficient c: "))

    find_roots = cmath.sqrt((b**2) - (4 * a * c))
    x_one = (-b + find_roots) / (2 * a)
    x_two = (-b - find_roots) / (2 * a)

    x_one_rounded = round(x_one.real, 3)
    x_two_rounded = round(x_two.real, 3)

    print("x1:", x_one_rounded, "x2:", x_two_rounded)

if __name__ == "__main__":
    main()