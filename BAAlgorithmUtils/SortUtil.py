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