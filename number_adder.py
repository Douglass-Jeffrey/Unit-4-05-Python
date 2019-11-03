#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This adds positive numbers


import random


def main():

    loopsum = 0
    loopcounter = 0

    try:
        n_value = input("Input the amount of integers you wish to add: ")
        n_value_int = int(n_value)
    except Exception:
        print("Please input only valid integers")

    # this function compares the random_int and value_1
    while n_value_int > loopcounter:
        try:
            number = input("Add your numbers: ")
            number_int = int(number)
        except Exception:
            print("Please input only valid integers")
            break
        if (number_int < 0):
            continue
        else:
            loopsum = loopsum + number_int
        loopcounter += 1
    print("The sum of positive numbers is: " + str(loopsum))
    

if __name__ == "__main__":
    main()
