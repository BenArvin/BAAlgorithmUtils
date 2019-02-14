#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys

def __swap(items, i, j):
    if items == None:
        return
    itemsLen = len(items)
    if i < 0 or i >= itemsLen or j < 0 or j >= itemsLen:
        return
    tmp = items[j]
    items[j] = items[i]
    items[i] = tmp

def bubbleSort(originalItems, ascending):
    if originalItems == None or len(originalItems) < 2:
        return originalItems
    sortedItems = originalItems
    itemsLen = len(sortedItems)
    for i in range(0, itemsLen - 1, 1):
        didSwap = False
        for j in range(0, itemsLen - i - 1, 1):
            needSwap = False
            if ascending == True and sortedItems[j] > sortedItems[j+1]:
                needSwap = True
            elif ascending == False and sortedItems[j] < sortedItems[j+1]:
                needSwap = True

            if needSwap == True:
                __swap(sortedItems, j, j+1)
                didSwap = True
        if didSwap == False:
            break
    return sortedItems

def selectionSort(originalItems, ascending):
    if originalItems == None or len(originalItems) < 2:
        return originalItems
    sortedItems = originalItems
    itemsLen = len(sortedItems)
    for i in range(0, itemsLen, 1):
        tmpIndex = 0
        for j in range(1, itemsLen - i, 1):
            if ascending == True and sortedItems[j] > sortedItems[tmpIndex]:
                tmpIndex = j
            elif ascending == False and sortedItems[j] < sortedItems[tmpIndex]:
                tmpIndex = j
        __swap(sortedItems, itemsLen-i-1, tmpIndex)
    return sortedItems

def __quickSortAction(items, ascending, left, right):
    if right - left <= 0 or right >= len(items) or right < 0 or left >= len(items) or left < 0:
        return
    flag = items[left]
    tmpLeft = left
    tmpRight = right
    moveLeft = False
    while(1):
        if tmpLeft >= tmpRight:
            break

        needSwap = False
        if ascending == True and items[tmpLeft] > items[tmpRight]:
            needSwap = True
            moveLeft = not moveLeft
        elif ascending == False and items[tmpLeft] < items[tmpRight]:
            needSwap = True
            moveLeft = not moveLeft

        if needSwap == True:
            __swap(items, tmpLeft, tmpRight)

        if moveLeft == True:
            tmpLeft = tmpLeft + 1
        else:
            tmpRight = tmpRight - 1

    __quickSortAction(items, ascending, left, tmpLeft - 1)
    __quickSortAction(items, ascending, tmpLeft + 1, right)

def quickSort(originalItems, ascending):
    if originalItems == None or len(originalItems) < 2:
        return originalItems
    sortedItems = originalItems
    __quickSortAction(originalItems, ascending, 0, len(sortedItems) - 1)
    return sortedItems