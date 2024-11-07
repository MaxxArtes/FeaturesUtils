#!/bin/python3

import math
import os
import random
import re
import sys


def plusMinus(arr):
    # Write your code here
    positivos = 0
    negativos = 0
    zeros = 0
    for item in arr:
        if item > 0:
            positivos+=1
        elif item < 0:
            negativos+=1
        else:
            zeros+=1
    proporcao_positivos = format((positivos / n), ".6f")
    proporcao_negativos = format((negativos / n), ".6f")
    proporcao_zeros = format((zeros / n), ".6f")
    
    return print(proporcao_positivos), print(proporcao_negativos), print(proporcao_zeros)
    
    
if __name__ == '__main__':
    n = int(input( 'digite a quantidade de elementos a serem colocados no seu array:').strip())

    arr = list(map(int, input('digite o array de valores a serem calculado ex:(-4 3 -9 0 4 1): ').rstrip().split()))

    plusMinus(arr)
