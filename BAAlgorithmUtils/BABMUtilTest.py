#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys, os
sys.path.append('../')

from BAAlgorithmUtils.BABMUtil import BABMUtil

def testFunc(matcher, content, duplMode):
    print('\n')
    print('matcher: ' + matcher)
    print('content: ' + content)
    print('duplMode: ' + str(duplMode))
    bmUtil = BABMUtil()
    bmUtil.setMatcher(matcher)
    print('bad char offset: ' + str(bmUtil.badCharTable))
    print('good suffix offset: ' + str(bmUtil.goodSuffixTable))
    result = bmUtil.search(content, duplMode)
    print('result: ' + str(result))
    print('\n')

if __name__ == '__main__':
    testFunc('example', '', False)
    testFunc('abcdd', '', False)
    testFunc('acddbcdd', '', False)
    testFunc('FGFAEFG', 'ABCDEFGHIJKL', False)
    testFunc('AEFAEF', 'ABCDEFGHIJKL', False)
    testFunc('AEFAEF', 'ABCDEFGHIJKLAEFAEFTYB', False)
    testFunc('AEFAEF', 'AEFAEFABCDEFGHIJKLAEFAEFAEFAEFTAEFAEFYBAEFAEF', False)
    testFunc('AEFAEF', 'AEFAEF', False)
    testFunc('AEFAEF', 'AEFAE', False)
    testFunc('AA', 'AAAAAAAAA', False)
    testFunc('AA', 'AAAAAAAAA', True)