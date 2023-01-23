def main():
    number = int(input("Enter an integer: "))

    if number >= 2:
        #for n in range(2, number):
         #   if (number % n) == 0:
          #      print(n, end = ' ')
                
        for nn in range(2, number + 1):
            for i in range(2, nn):
                if (nn % i) == 0:
                    break
            else:
                print(nn, end = ' ')
        


if __name__ == "__main__":
    main()