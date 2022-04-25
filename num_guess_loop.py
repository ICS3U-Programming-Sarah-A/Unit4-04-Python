#!/usr/bin/env python3

# Created by: Sarah
# Created on: Apr. 25, 2022
# This program asks the user to enter a number. It checks to see if user_num is
# == to random_num. If not, it keeps going until user gets the number correct.
# Once they get it correct, it breaks out of the loop.

import random


def main():
    # initialize the loop counter & rand create variable
    counter = 0
    random_number = random.randint(0, 9)

    while True:
        # get the user number as a string
        user_number_string = input("Enter a number between 0-9: ")
        print("")

        try:
            # converts user input to integer
            user_number_int = int(user_number_string)

            # sets a range
            if user_number_int >= 0 and user_number_int <= 9:
                counter = counter + 1

                # checks to see if user_num == rand_num or not & then displays
                # it.
                if user_number_int == random_number:
                    print("")
                    print("{} is the correct guess!".format(user_number_int))
                    break
                else:
                    print("{} is incorrect. Please try again.".
                          format(user_number_int))
                    print("")
                    print("Tracking {0} times through the loop."
                          .format(counter))
                    print("")
            else:
                print("Please enter a number within the range.")

        # handles the error case
        except Exception:
            print("{} is not a number, please try again.".
                  format(user_number_string))


if __name__ == "__main__":
    main()
