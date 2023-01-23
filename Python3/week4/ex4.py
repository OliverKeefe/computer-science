def while_loop_times_tables(a):
    x = a * 20
    c = 1
    while c != 21:
        print(c*a)
        c += 1
    else:
        pass

def for_loop_times_tables(a):
    for i in range(1,21):
        print(a * i)
    else:
        pass

def main():
    user_input = int(input("Enter an int that you want the timestables of: "))
    times_tables_full = [1*user_input,2*user_input,3*user_input,4*user_input,5*user_input,6*user_input,7*user_input,8*user_input,9*user_input,10*user_input,11*user_input,12*user_input,13*user_input,14*user_input,15*user_input,16*user_input,17*user_input,18*user_input,19*user_input,20*user_input,]
    print(while_loop_times_tables(user_input))
    print(for_loop_times_tables(user_input))

if __name__ == "__main__":
    main()