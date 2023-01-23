import time

def countdown_clock(time_sec):
    while time_sec != 0:
        time.sleep(1)
        print(time_sec)
        time_sec -= 1
    else:
        exit()
        

def main():
    time_sec = int(input("Enter your start time in seconds: "))

    print(countdown_clock(time_sec))    

if __name__ == "__main__":
    main()