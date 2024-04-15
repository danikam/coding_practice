import math
import os
import random
import numpy as np
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def random_with_up_to_N_digits(n):
    range_start = 1
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

def bigSorting(unsorted):
    # Write your code here
    sorted_list = []
    while len(unsorted) > 0:
        lowest = unsorted[0]
        for i in unsorted:
            if int(i) <= int(lowest):
                lowest = i
        sorted_list.append(lowest)
        unsorted.remove(lowest)
    return sorted_list
    
def test_sort():
    test_length=10000
    test_list = []
    test_array = np.zeros(0)
    for i in range(test_length):
        random_int = random.randint(1, 1e100)
        test_list.append(str(random_int))
        test_array = np.append(test_array, random_int)
    sorted_array = np.sort(test_array)
    sorted_str = []
    for element in sorted_array:
        sorted_str.append(str(int(element)))
    print('Test list: ')
    print(test_list)
    print('\nSorted list: ')
    print(sorted_str)
    assert bigSorting(test_list) == sorted_str, 'failed test_sort()'
            

if __name__ == '__main__':
    test_sort()


