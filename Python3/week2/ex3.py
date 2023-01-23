# A program for numbers 
# a = 3 - 4 + 10 
# b = 5 * 6 
# c = 7.0/8.0 
# print ("These are the values:", a, b, c) 
# print ("Increment", a, "by one: ") 
# a = a + 1 
# print (a) 
# print ("The sum of", a, "and", b, "is") 
# d = a + b 
# print (d) 
# number = int( input("Input a number ") ) 
# r = number * 2 
# print ("your number times 2 is", r)

# Task 1:
# Code explanations:
# a, b, c, d, number, r : Are variables
# print : A function that outputs an expected value
# int : A function that parses a user input from a String into an Int
# input : a function that gets user input and converts to a string value

def mathfunc(input):
    output = number 
    output += 3
    output *= 2
    output -= 4
    output -= number * 2 +3
    
    return output

def main():
    number = int(input("Enter your number: "))
    print (mathfunc(number))
    
if __name__ == "__main__":
    main()