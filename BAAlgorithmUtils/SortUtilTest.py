#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys, os
sys.path.append('../')

from BAAlgorithmUtils.SortUtil import bubbleSort

def bubbleSortTest(originalItems, ascending):
    if ascending == True:
        print('\nBubble sort(Ascending)')
    else:
        print('\nBubble sort(Descending)')
    print('Original: ' + str(originalItems))
    print('Sorted: ' + str(bubbleSort(originalItems, ascending)))

if __name__ == '__main__':
    bubbleSortTest([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48], True)
    bubbleSortTest([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48], False)