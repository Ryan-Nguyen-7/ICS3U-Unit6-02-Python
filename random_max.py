#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on Decemebr 2020
# This program generates 10 random numbers and determines the greatest

import random


def find_greatest(list_of_randoms):
    # this function determines the greatest number out of an array
    greatest = list_of_randoms[0]

    for counter in range(0, 10):
        if greatest < list_of_randoms[counter]:
            greatest = list_of_randoms[counter]

    return greatest


def main():
    # this function generates 10 random numbers and outputs the greatest one

    list_of_randoms = []

    # generates numbers, puts them in list
    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)
        list_of_randoms.append(random_number)
        print("Random number {0}: {1}".format(loop_counter + 1, random_number))

    # calls find_greatest function
    greatest = find_greatest(list_of_randoms)
    
    # final answer
    print("Greatest: {0}".format(greatest))


if __name__ == "__main__":
    main()
