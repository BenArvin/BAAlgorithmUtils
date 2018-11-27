#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os
sys.path.append('../')

from BAAlgorithmUtils.BAKMPUtil import BAKMPUtil

def testFunc(matcher, content):
    print('\n')
    print('matcher:')
    kmpUtil = BAKMPUtil()
    kmpUtil.setMatcher(matcher)
    kmpUtil.printPMTable()
    print('content: ' + content)
    print('result: ' + str(kmpUtil.search(content)))
    print('\n')

if __name__ == '__main__':

    testFunc('ABCDABD', 'BBCABCDABABCDABCDABDE')
    testFunc('ABCDABD', 'BBCABCDABABCDABCDABDEABCDABD')
    testFunc('ABCDABD', 'AAAAAAAAAAAAAAAAAAAAAAAAAAA')
    testFunc('ABCDABD', 'BBBBBBBBBBBBBBBBBBBBBBBBBB')
    testFunc('ABCDABD', 'BBBBB')
    testFunc('ABCDABD', 'ABCDABD')
    testFunc('ABCDABD', 'ABCDAB')