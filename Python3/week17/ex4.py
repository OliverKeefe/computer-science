# Define a new function called overlap() that takes two parameters: a and b, where a and b are
# both Python lists of data items. The function should return True if the two lists have at least one
# element in common, or False if they have no elements in common. You must not use the Python in
# operator for this exercise. Note: you might like to re-use the is_member() function from Exercise 3
# to help with this exercise.
# Create some sample Python lists of random values (random numbers and/or words), and write some
# function calls to test your overlap() function with the different lists.

def overlap(a, b):
    intersects = False
    a = set(a)
    b = set(b)
    
    if a.intersection(b):
        intersects = True
    elif b.intersection(a):
        intersects = True
    return intersects

def main():
    list1 = [1, 2, 3, 4, 5, 6, "Cabbage", "Apple", "C", 12.443]
    list2 = [3456.1, 2, 343, 14, 4, 6, "Apple", "X", "Orange", 213.75]
    list3 = [1, 2, 3, "Hello", 5, 6]
    list4 = [3456.223, "f", "5832", 14, 112.3, 6.01]
    print(overlap(list1, list2), overlap(list3, list4))
    
if __name__ == "__main__":
    main()