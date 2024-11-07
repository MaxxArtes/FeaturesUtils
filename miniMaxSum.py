import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Ordena a lista para facilitar o cálculo das somas
    arr_sorted = sorted(arr)
    
    # Calcula a soma mínima (ignorando o maior número)
    minimo = sum(arr_sorted[:-1])
    
    # Calcula a soma máxima (ignorando o menor número)
    maximo = sum(arr_sorted[1:])
    
    # Exibe os resultados
    print('soma máxima: ',minimo,'e soma mínima: ',maximo)
    
if __name__ == '__main__':

    arr = list(map(int, input('digite a lista de numeros ex:(1 2 3 4 5): ').rstrip().split()))

    miniMaxSum(arr)
