# 4. Define a new function max_of_three() that takes three numbers as parameters and 
# returns the largest. Write a simple program to test the function. 

def max_of_three(param1, param2, param3):
    params = (param1, param2, param3)
    largest = param1

    for i in params:
        if i > largest:
            largest = i

    if largest == param1:
        return str(param1) + " is largest."
    elif largest == param2:
        return str(param2) + " is largest."
    else:
        return str(param3) + " is largest."

def main():
    input_one = input("Enter the first value: ")
    while not isinstance(float(input_one), float):
        print("Must be float") 
        input_one = input("Enter the first value: ")

    input_two = input("Enter the second value: ")
    while not isinstance(float(input_two), float):
        print("Must be float") 
        input_two = input("Enter the second value: ")

    input_three = input("Enter the third value: ")
    while not isinstance(float(input_three), float):
        print("Must be float") 
        input_three = input("Enter the third value: ")

    print(max_of_three(float(input_one), float(input_two), float(input_three)))

if __name__ == "__main__":
    main()



