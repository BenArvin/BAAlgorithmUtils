#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os
sys.path.append('../')

from BAAlgorithmUtils.BSTUtil import BSTUtil

def start1():
    print('\n********************************')
    trainSamples = [
        {'key': 5, 'content': '5-1'},
        {'key': 3, 'content': '3-1'},
        {'key': 4, 'content': '4-1'},
        {'key': 2, 'content': '2-1'},
        {'key': 1, 'content': '1-1'},
        {'key': 8, 'content': '8-1'},
        {'key': 7, 'content': '7-1'},
        {'key': 6, 'content': '6-1'},
        {'key': 9, 'content': '9-1'},
    ]
    trainsString = ''
    bstUtil = BSTUtil()
    for sample in trainSamples:
        trainsString = trainsString + ', ' + str(sample['key'])
        bstUtil.set(sample['key'], sample['content'])
    print('Sample: ' + trainsString[2 : len(trainsString)])
    print('\nBST:')
    bstUtil.fullPrint()
    print('\n>>>>>>>>>>>>>> delete 1')
    bstUtil.delete(1)
    bstUtil.fullPrint()
    print('\n>>>>>>>>>>>>>> delete 5')
    bstUtil.delete(5)
    bstUtil.fullPrint()
    print('\n>>>>>>>>>>>>>> delete 3')
    bstUtil.delete(3)
    bstUtil.fullPrint()
    print('********************************\n')

def start2():
    print('\n********************************')
    trainSamples = [
        {'key': 9, 'content': '9-1'},
        {'key': 8, 'content': '8-1'},
        {'key': 12, 'content': '12-1'},
        {'key': 7, 'content': '7-1'},
        {'key': 6, 'content': '6-1'},
        {'key': 5, 'content': '5-1'},
        {'key': 4, 'content': '4-1'},
        {'key': 3, 'content': '3-1'},
    ]
    trainsString = ''
    bstUtil = BSTUtil()
    for sample in trainSamples:
        trainsString = trainsString + ', ' + str(sample['key'])
        bstUtil.set(sample['key'], sample['content'])
    print('Sample: ' + trainsString[2 : len(trainsString)])
    print('\nBST:')
    bstUtil.fullPrint()
    print('********************************\n')

if __name__ == '__main__':
    start1()
    start2()