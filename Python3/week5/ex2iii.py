import re
import string

def main():
    x = input("Enter your sentence: ")
    n = int(input("Enter the index of the character to remove:"))

    #split = re.findall(f"[\w]+|[{string.punctuation}]", x)
#
    #split_result = ' '.join(y[::n] if y[::n].isalnum() else y for y in split)
    #
    ## Removes the random spaces that kept appearing.
    #for i in string.punctuation:
    #    split_result = split_result.replace(f' {i}', i)
    #
#
    #x = input("Enter your sentence: ")

    print(x[::n])
    # print(split_result)
        
if __name__ == "__main__":
    main()