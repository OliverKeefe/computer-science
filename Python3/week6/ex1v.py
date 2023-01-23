def main():
    exam_result = int(input("Enter your exam result as a percentage (out of 100): "))

    if exam_result >= 80 and exam_result <= 100:
        print("You have recieved a distinction!")
    elif exam_result >= 101:
        print("[!] Invalid input.")
    elif exam_result >= 40 and exam_result <= 101:
        print("You have passed!")
    elif exam_result < 40:
        print("You've failed, sorry.")
    else:
        print("[!] Invalid input.")

if __name__ == "__main__":
    main()