#!/usr/bin/python3
import sys

# check if a file name was provided as an argument
if len(sys.argv) < 2:
    print("Usage: Factorization of numbers")
    # to terminate the file and return error code
    sys.exit(1)


def factors(num):
    a = 0
    b = 0
    if num == 0 or num == 1:
        a = num
        b = num
        return a,b
    # range start to stop
    for i in range(2, num + 1):
        if num % i == 0:
            a = i
            # // always returns an integer
            b = num // i
            return a, b
        else:
            a = num
            b = num
    return a, b


# get the file name from first argument
file_name = sys.argv[1]

# open the file and read contents line by line
with open(file_name, 'r') as file:
    for line in file:
        # convert line to int then find the 2 factors
        number = factors(int(line.strip()))

        # output result for the line
        print("{} = {} * {}".format(line.strip(), number[0], number[1]))
