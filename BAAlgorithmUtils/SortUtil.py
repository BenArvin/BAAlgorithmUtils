#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys

def bubbleSort(originalItems, ascending):
    if originalItems == None or len(originalItems) < 2:
        return originalItems
    sortedItems = originalItems
    itemsLen = len(sortedItems)
    for i in range(0, itemsLen - 1, 1):
        for j in range(0, itemsLen - i - 1, 1):
            needExchange = False
            if ascending == True and sortedItems[j] > sortedItems[j+1]:
                needExchange = True
            elif ascending == False and sortedItems[j] < sortedItems[j+1]:
                needExchange = True

            if needExchange == True:
                tmp = sortedItems[j+1]
                sortedItems[j+1] = sortedItems[j]
                sortedItems[j] = tmp
    return sortedItems

def selectionSort(originalItems, ascending):
    if originalItems == None or len(originalItems) < 2:
        return originalItems
    sortedItems = originalItems
    itemsLen = len(sortedItems)
    for i in range(0, itemsLen, 1):
        tmpIndex = 0
        for j in range(1, itemsLen - i, 1):
            needExchange = False
            if ascending == True and sortedItems[j] > sortedItems[tmpIndex]:
                tmpIndex = j
            elif ascending == False and sortedItems[j] < sortedItems[tmpIndex]:
                tmpIndex = j
        tmp = sortedItems[itemsLen-i-1]
        sortedItems[itemsLen-i-1] = sortedItems[tmpIndex]
        sortedItems[tmpIndex] = tmp
    return sortedItems