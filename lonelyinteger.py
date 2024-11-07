import math
import os
import random
import re
import sys


def lonelyinteger(a):
    result = 0
    for num in a:
        result ^= num
    return result

if __name__ == '__main__':
    n = int(input('digite a quantidade de elementos no array: ').strip())

    a = list(map(int, input('digite o valores a serem colocados no array ex:(1 2 3 2 1): ').rstrip().split()))

    result = lonelyinteger(a)

    print('o numero unico é: ',str(result) + '\n')
