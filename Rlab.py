#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
    sys.exit(1)

def fct(num):
    """
    Return tuple (p, q) of prime factors of n
    """
    if num % 2 == 0:
        return (2, num//2)
    # add step size of 2 to remove even numbers in loop
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            if prime(i) and prime(num//i):
                return (i, num//i)
    return None
def prime(lim):
    """
    Returns true if num is a prime number, false if not
    """
    if lim < 2:
        return False
    elif lim == 2:
        return True
    elif lim % 2 == 0:
        return False
    else:
        for i in range(3, int(lim**0.5) + 1, 2):
            if lim % i == 0:
                return False
        return True
file_name = sys.argv[1]

with open(file_name, 'r') as file:
    for line in file:
        number = fct(int(line.strip()))
        if number is None:
            print("{} has no prime factors.".format(line.strip()))
        else:
            print("{}={}*{}".format(line.strip(), number[1], number[0]))
