#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

if number >= 0:
    last = number % 10
    if last > 5:
        string1 = 'and is greater than 5'
        print('Last digit of {} is {} {}'.format(number, last, string1))
    elif last == 0:
        print('Last digit of {} is {} and is 0'.format(number, last))
    else:
        string2 = 'and is less than 6 and not 0'
        print('Last digit of {} is {} {}'.format(number, last, string2))

else:
    conv = -1 * number
    last = -1 * (conv % 10)
    if last == 0:
        print('Last digit of {} is {} and is 0'.format(number, last))
    else:
        string2 = 'and is less than 6 and not 0'
        print('Last digit of {} is {} {}'.format(number, last, string2))
