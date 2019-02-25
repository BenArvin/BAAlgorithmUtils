#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os
sys.path.append('../')

from BAAlgorithmUtils.RBTreeUtil import RBTree

def start1():
    print('\n********************************')
    trainSamples = [
        {'key': 3, 'content': '3-1'},
        {'key': 2, 'content': '2-1'},
        {'key': 1, 'content': '1-1'},
        {'key': 4, 'content': '4-1'},
        {'key': 5, 'content': '5-1'},
        {'key': 6, 'content': '6-1'},
        {'key': 7, 'content': '7-1'},
        {'key': 16, 'content': '16-1'},
        {'key': 15, 'content': '15-1'},
        {'key': 14, 'content': '14-1'},
        {'key': 13, 'content': '13-1'},
        {'key': 12, 'content': '12-1'},
        {'key': 11, 'content': '11-1'},
        {'key': 10, 'content': '10-1'},
        {'key': 8, 'content': '8-1'},
        {'key': 9, 'content': '9-1'},
    ]
    trainsString = ''
    tree = RBTree()
    for sample in trainSamples:
        trainsString = trainsString + ', ' + str(sample['key'])
        tree.set(sample['key'], sample['content'])
    print('Sample: ' + trainsString[2 : len(trainsString)])
    print('\nRB Tree:')
    tree.fullPrint()

    keyForDelete = 1
    print('\nAfter delete ' + str(keyForDelete) + ':')
    tree.delete(keyForDelete)
    tree.fullPrint()

    keyForDelete = 2
    print('\nAfter delete ' + str(keyForDelete) + ':')
    tree.delete(keyForDelete)
    tree.fullPrint()

    keyForDelete = 8
    print('\nAfter delete ' + str(keyForDelete) + ':')
    tree.delete(keyForDelete)
    tree.fullPrint()

    keyForDelete = 11
    print('\nAfter delete ' + str(keyForDelete) + ':')
    tree.delete(keyForDelete)
    tree.fullPrint()

    keyForDelete = 13
    print('\nAfter delete ' + str(keyForDelete) + ':')
    tree.delete(keyForDelete)
    tree.fullPrint()
    print('********************************\n')

if __name__ == '__main__':
    start1()