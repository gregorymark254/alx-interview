#!/usr/bin/python3


def minOperations(n):
    """
    returns the fewest number of operation need to result in exactly
    n H characters in the file
    """
    a = 0
    b = 2
    while n > 1:
        while n % b == 0:
            a += b
            n = n / b
        b += 1
    return a
