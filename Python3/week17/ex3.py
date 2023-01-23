# Define a new function called is_member() that takes two parameters: x and a, where x is a single
# data item (that could be a number or string) and where a is a Python list of data items. The function
# should return True if x is a member of list a, or False if not. You must not use the Python in
# operator for this exercise.
# To test your function, create some sample Python lists of data items, and write some function calls to
# test the is_member() function with the different lists.

def is_member(x, a):
    membership = False
    
    for i in a:
        if i == x:
            membership = True
            
    return membership
        
def main():
    list1 = [1, 2, 3, 4, 5, 6, "Cabbage", "Apple", "C", 12.443]
    print(list1)
    item1 = 1
    item2 = "Cabbage"
    item3 = 12.443
    item4 = 129.44
    print(is_member(item1, list1), is_member(item2, list1), is_member(item3, list1), is_member(item4, list1))
    
if __name__ == "__main__":
    main()