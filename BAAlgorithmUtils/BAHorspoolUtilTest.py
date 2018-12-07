#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys, os
sys.path.append('../')

from BAAlgorithmUtils.BAHorspoolUtil import BAHorspoolUtil

def testFunc(matcher, content, duplMode):
    print('\n')
    print('matcher: ' + matcher)
    print('content: ' + content)
    print('duplMode: ' + str(duplMode))
    horspoolUtil = BAHorspoolUtil()
    horspoolUtil.setMatcher(matcher)
    print('offset table: ' + str(horspoolUtil.offsetTable))
    result = horspoolUtil.search(content, duplMode)
    print('result: ' + str(result))
    print('\n')

if __name__ == '__main__':
    testFunc('OHELLO', '-BHALLOBHALLOHELLO', False)
    testFunc('BHELLO', 'BHELLABHALLOBHELLO', False)
    testFunc('FGFAEFG', 'ABCDEFGHIJKL', False)
    testFunc('AEFAEF', 'ABCDEFGHIJKL', False)
    testFunc('AEFAEF', 'ABCDEFGHIJKLAEFAEFTYB', False)
    testFunc('AEFAEF', 'AEFAEFABCDEFGHIJKLAEFAEFAEFAEFTAEFAEFYBAEFAEF', False)
    testFunc('AEFAEF', 'AEFAEF', False)
    testFunc('AEFAEF', 'AEFAE', False)
    testFunc('AA', 'AAAAAAAAA', False)
    testFunc('AA', 'AAAAAAAAA', True)