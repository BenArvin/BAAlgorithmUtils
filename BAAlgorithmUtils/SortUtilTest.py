#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys, os
sys.path.append('../')

from BAAlgorithmUtils.SortUtil import bubbleSort, selectionSort, quickSort, bucketSort

def bubbleSortTest(originalItems, ascending):
    if ascending == True:
        print('\nBubble sort(Ascending)')
    else:
        print('\nBubble sort(Descending)')
    print('Original: ' + str(originalItems))
    print('Sorted: ' + str(bubbleSort(originalItems, ascending)))

def selectionSortTest(originalItems, ascending):
    if ascending == True:
        print('\nSelection sort(Ascending)')
    else:
        print('\nSelection sort(Descending)')
    print('Original: ' + str(originalItems))
    print('Sorted: ' + str(selectionSort(originalItems, ascending)))

def quickSortTest(originalItems, ascending):
    if ascending == True:
        print('\nQuick sort(Ascending)')
    else:
        print('\nQuick sort(Descending)')
    print('Original: ' + str(originalItems))
    print('Sorted: ' + str(quickSort(originalItems, ascending)))

def bucketSortTest(originalItems, ascending):
    if ascending == True:
        print('\nBucket sort(Ascending)')
    else:
        print('\nBucket sort(Descending)')
    print('Original: ' + str(originalItems))
    print('Sorted: ' + str(bucketSort(originalItems, ascending)))

if __name__ == '__main__':
    bubbleSortTest([3, 44, 38, 5, 5, 47, 15, 36, 26, 27, 2, 46, 15, 4, 19, 50, 48], True)
    bubbleSortTest([3, 44, 38, 5, 5, 47, 15, 36, 26, 27, 2, 46, 15, 4, 19, 50, 48], False)
    selectionSortTest([3, 44, 38, 5, 5, 47, 15, 36, 26, 27, 2, 46, 15, 4, 19, 50, 48], True)
    selectionSortTest([3, 44, 38, 5, 5, 47, 15, 36, 26, 27, 2, 46, 15, 4, 19, 50, 48], False)
    quickSortTest([3, 44, 38, 5, 5, 47, 15, 36, 26, 27, 2, 46, 15, 4, 19, 50, 48], True)
    quickSortTest([3, 44, 38, 5, 5, 47, 15, 36, 26, 27, 2, 46, 15, 4, 19, 50, 48], False)
    bucketSortTest([3, 44, 38, 5, 5, 47, 15, 36, 26, 27, 2, 46, 15, 4, 19, 50, 48], True)
    bucketSortTest([3, 44, 38, 5, 5, 47, 15, 36, 26, 27, 2, 46, 15, 4, 19, 50, 48], False)