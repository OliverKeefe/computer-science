# 7. Define a new function reverse() that takes a string as a parameter, and then computes and 
# returns the reversal of the string. For example, reverse("Hello World") should return 
# the string "dlroW olleH". Write a simple program to test the function. 

def reverse(str):
    reversed_str = str[::-1]

    return reversed_str

def main():
    user_input = input("Enter a string: ")
    print(reverse(user_input))

if __name__ == "__main__":
    main()