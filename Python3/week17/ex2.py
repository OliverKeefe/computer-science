# Define a new function called histogram() that takes one Python list as a parameter – for this
# exercise we can assume that the list will contain only integers. The function should then print a
# simple histogram using asterisks based on the values in the list.
# For example, histogram([2,8,4,1]) would print the following:
#       >>>
#       **
#       ********
#       ****
#       *
#       >>>
# To test your function, create some sample Python lists containing integers, and write some function
# calls to the histogram() function with the different lists.

def histogram(list1):
    astrix = '*'
    hist = []
    
    for i in list1: 
        ii = int(i)
        hist_slice = str(astrix * ii)
        hist.append(hist_slice)
        
    return hist
    
def main():
    user_input = ''
    user_list = []
    
    while True:
        user_input = input("Enter an integer to add to the list or s to stop:")

        if user_input != 's':
            try:
                user_list.append(user_input)

            except ValueError:
                print("[!] Invalid input")
                user_input = input("Enter an integer to add to the list or s to stop:")

        elif user_input == 's':
            final_list = histogram(user_list)

            for i in final_list:
                print(i)
            
            exit()
        
if __name__ == "__main__":
    main()