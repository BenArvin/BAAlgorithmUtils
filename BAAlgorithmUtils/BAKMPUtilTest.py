#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os
sys.path.append('../')

from BAAlgorithmUtils.BAKMPUtil import BAKMPUtil

def testFunc(matcher, content, duplMode):
    print('\n')
    print('matcher:')
    kmpUtil = BAKMPUtil()
    kmpUtil.setMatcher(matcher)
    valueString = ''
    countString = ''
    for tableItem in kmpUtil.PMTable:
        valueString = valueString + str(tableItem['value']) + '\t'
        countString = countString + str(tableItem['count']) + '\t'
    print(valueString)
    print(countString)
    print('content: ' + content)
    print('duplMode: ' + str(duplMode))
    print('result: ' + str(kmpUtil.search(content, duplMode)))
    print('\n')

if __name__ == '__main__':

    testFunc('ABCDABD', 'BBCABCDABABCDABCDABDE', False)
    testFunc('ABCDABD', 'BBCABCDABABCDABCDABDEABCDABD', False)
    testFunc('ABCDABD', 'AAAAAAAAAAAAAAAAAAAAAAAAAAA', False)
    testFunc('ABCDABD', 'BBBBBBBBBBBBBBBBBBBBBBBBBB', False)
    testFunc('ABCDABD', 'BBBBB', False)
    testFunc('ABCDABD', 'ABCDABD', False)
    testFunc('ABCDABD', 'ABCDAB', False)
    testFunc('AA', 'AAAAAAAAA', True)
    testFunc('AA', 'AAAAAAAAA', False)