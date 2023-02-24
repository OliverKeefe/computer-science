# 3. Define a new function max2() that takes two numbers as parameters and returns the largest. 
# You should use an if else statement inside the function definition. (It is true that Python has a 
# max() function built in, but writing one yourself is good practise). Write a simple program to 
# test the function. 

def max2(param1, param2):
    x = ""
    if param1 > param2:
        x = str(param1 + " is largest.")
        
    elif param2 > param1:
        x = str(param2 + " is largest.")

    elif param1 == param2:
        x = "They are both the same."
    return x

def main():
    input_one = input("Enter the first value: ")
    while not isinstance(float(input_one), float):
        print("Must be float ") 
        input_one = input("Enter the first value: ")

    input_two = input("Enter the second value: ")
    while not isinstance(float(input_two), float):
        print("Must be float ") 
        input_two = input("Enter the second value: ")
            
    print(max2(input_one, input_two))

if __name__ == "__main__":
    main()
