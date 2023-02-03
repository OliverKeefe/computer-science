# There are 36 possible outcomes when you roll two standard six-sided dice. Two nested loops over a 
# range(1,7) is one way to determine all of these combinations, and simple addition can be used to 
# calculate the sum of the two dice. 
# Create a Python dictionary to store the 36 possible combinations: The dictionary key should be the 
# sum of a roll, and the dictionary value should be a Python list of Python tuples, where each tuple is a 
# 2-tuple containing the values of the two dice. 
# To make sure your solution works correctly, print the contents of the dictionary in an appropriate 
# format. 
# The output should look something like this: 
# >>> 
# sum 2 : possible rolls : [(1, 1)] 
# sum 3 : possible rolls : [(1, 2), (2, 1)] 
# sum 4 : possible rolls : [(1, 3), (2, 2), (3, 1)] 
# sum 5 : possible rolls : [(1, 4), (2, 3), (3, 2), (4, 1)] 
# sum 6 : possible rolls : [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)] 
# sum 7 : possible rolls : [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)] 
# sum 8 : possible rolls : [(2, 6), (3, 5), (4, 4), (5, 3), (6, 2)] 
# sum 9 : possible rolls : [(3, 6), (4, 5), (5, 4), (6, 3)] 
# sum 10 : possible rolls : [(4, 6), (5, 5), (6, 4)] 
# sum 11 : possible rolls : [(5, 6), (6, 5)] 
# sum 12 : possible rolls : [(6, 6)] 
# >>>
# Now repeat the task again, but with three dice.

import itertools as iter

def main():
    x = range(1,7)
    y = 2
    while y <= 12:
        combinations = list(iter.product(x, repeat=2))
        combinations = [i for i in combinations if sum(i) == y]
        print("sum", y, ": possible rolls :", combinations)
        y += 1

if __name__ == "__main__": 
    main()