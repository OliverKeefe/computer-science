# 4. Define a new function max_of_three() that takes three numbers as parameters and 
# returns the largest. Write a simple program to test the function. 

def max_of_three(param1, param2, param3):
    params = (param1, param2, param3)
    largest = param1

    for i in params:
        if i > largest:
            largest = i

    return largest

def main():
    input_one = input("Enter the first value: ")
   
    while not isinstance(input_one, float):
        try:
            float(input_one)
            break
        except ValueError:
            print("Must be float ") 
            input_one = input("Enter the first value: ")

    input_two = input("Enter the second value: ")

    while not isinstance(input_two, float):
        try:
            float(input_two)
            break
        except ValueError:
            print("Must be float ") 
            input_two = input("Enter the second value: ")

    input_three = input("Enter the second value: ")

    while not isinstance(input_three, float):
        try:
            float(input_three)
            break
        except ValueError:
            print("Must be float ") 
            input_three = input("Enter the third value: ")

    print(max_of_three(input_one, input_two, input_three), "is largest.")

if __name__ == "__main__":
    main()



