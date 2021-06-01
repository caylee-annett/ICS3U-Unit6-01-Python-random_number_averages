#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: June 2021
# This program calculates the average of ten random numbers and uses a list

import random


def main():
    # This function calculates the average

    number_list = []
    sum_of_numbers = 0

    # Process & Output
    print("This program calculates the average of 10 random numbers.")
    print("")
    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)
        print("The random number is: {}".format(random_number))
        number_list.append(random_number)
    for loop_counter in range(len(number_list)):
        sum_of_numbers = sum_of_numbers + number_list[loop_counter]
    average = sum_of_numbers / len(number_list)
    print("")
    print("The average is: {}".format(average))
    print("\nDone.")


if __name__ == "__main__":
    main()
