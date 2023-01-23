import math
import numpy as np

def largest_number(series):
    result = max(series)
    return result

def smallest_number(series):
    result = min(series)
    return result

def list_length(series):
    result = len(series)
    return result

def list_sum(series):
    result = sum(series)
    return result

def list_mean(series):
    result = sum(series) / len(series)
    return result

def main():
    choice = ''
    user_input = 0
    series = []

    while user_input != '':
            user_input = input('Input a series of integers: ')
            if user_input != '':
                int_input = int(user_input)
                series.append(int_input)
                print(series)

if __name__ == "__main__":
    main()
    #Fixed! Woo!