# 5. Define a new function string_length() that takes a string as a parameter and returns the
# length of the string. You should NOT use the built-in Python len() function for this task. 
# Write a simple program to test the function

def string_length(string):
    length = 0

    for i in string:
        length += 1
    
    return length

input_string = input("Enter a string: ")
print(string_length(input_string))