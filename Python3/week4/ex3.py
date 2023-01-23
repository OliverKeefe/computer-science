def while_loop_two_params(a, b):
    print(a)
    while a < b:
        a += 1
        print(a)
    else:
        pass

def for_loop_two_params(a, b):
    print(a)
    for a in range(a, b):
        a += 1
        print(a)
    else:
        pass
    
def print_number_array(a):
    for i in a:
        print(i)
    else:
        pass
    
even_numbers = [0,2,4,6,8,10,12,14,16,18,20]
odd_numbers = [1,3,5,7,9,11,13,15,17,19]

def while_loop_two_params_minus(a, b):
    print(a)
    
    while a > b:
        a -= 1
        print(a)
    else:
        pass

def while_loop_times_tables(a):
    x = a * 10
    c = 1
    while c != 11:
        print(c*a)
        c += 1
    else:
        pass

def for_loop_times_tables(a):
    for i in range(1,11):
        print(a * i)
    else:
        pass

def main():
    #1: 
    print(while_loop_two_params(5, 15))
    input("Press any key to continue... ")
    #2:
    print(for_loop_two_params(6, 16)) 
    input("Press any key to continue... ")
    #3:
    print(print_number_array(even_numbers)) 
    input("Press any key to continue... ")
    #4:
    print(print_number_array(odd_numbers))
    input("Press any key to continue... ")
    #5:
    print(while_loop_two_params_minus(10, 1))
    input("Press any key to continue... ")
    #6: 
    print(while_loop_two_params_minus(8, 1))
    input("Press any key to continue... ")
    #7: Fixed!
    print(while_loop_times_tables(4))
    input("Press any key to continue... ")
    #8:
    print(for_loop_times_tables(5))
    input("Press any key to continue... ")
    #9: Fix these two also, should be power 2 up to 16 not all nums 
    print(while_loop_two_params(2**1, 2**16))
    input("Press any key to continue... ")
    #10. 
    print(for_loop_two_params(2**1, 2**16))
    input("Press any key to continue... ")

if __name__ == "__main__":
    main()