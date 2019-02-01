#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os
sys.path.append('../')

from BAAlgorithmUtils.BSTUtil import BSTTree

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
    bstTree = BSTTree()
    for sample in trainSamples:
        trainsString = trainsString + ', ' + str(sample['key'])
        bstTree.set(sample['key'], sample['content'])
    print('Sample: ' + trainsString[2 : len(trainsString)])
    print('\nBST:')
    bstTree.fullPrint()
    print('\n>>>>>>>>>>>>>> delete 1')
    bstTree.delete(1)
    bstTree.fullPrint()
    print('\n>>>>>>>>>>>>>> delete 5')
    bstTree.delete(5)
    bstTree.fullPrint()
    print('\n>>>>>>>>>>>>>> delete 3')
    bstTree.delete(3)
    bstTree.fullPrint()
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
    bstTree = BSTTree()
    for sample in trainSamples:
        trainsString = trainsString + ', ' + str(sample['key'])
        bstTree.set(sample['key'], sample['content'])
    print('Sample: ' + trainsString[2 : len(trainsString)])
    print('\nBST:')
    bstTree.fullPrint()
    print('********************************\n')

if __name__ == '__main__':
    start1()
    start2()