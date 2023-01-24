# 2. Write a program to output the first 10 square numbers – you should use the function defined 
# in task 1 to perform the square operation on the numbers. 

def func(int):
    square = int ** 2

    return square

for i in range(1, 10):
    print(func(i))