#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys, os

class BAKMPUtil(object):
    def __init__(self):
        super(BAKMPUtil, self).__init__()
        self.__PMTable = []
        self.__tableItemValueKey = 'value'
        self.__tableItemCountKey = 'count'
    
    def printPMTable(self):
        valueString = ''
        countString = ''
        for tableItem in self.__PMTable:
            valueString = valueString + str(tableItem[self.__tableItemValueKey]) + '\t'
            countString = countString + str(tableItem[self.__tableItemCountKey]) + '\t'
        print(valueString)
        print(countString)

    def setMatcher(self, matcher):
        if matcher == None or len(matcher) == 0:
            return
        self.__PMTable = []
        for i in range(len(matcher)):
            matcherTmp = matcher[0 : i + 1]
            matchCount = 0
            if len(matcherTmp) == 1:
                matchCount = 0
            else:
                matcherTmpLen = len(matcherTmp)
                allPrefix = []
                for j in range(0, matcherTmpLen - 1, 1):
                    allPrefix.append(matcherTmp[0 : j + 1])
                for k in range(matcherTmpLen - 1, 0, -1):
                    suffixTmp = matcherTmp[k : matcherTmpLen]
                    if suffixTmp in allPrefix:
                        if len(suffixTmp) >= matchCount:
                            matchCount = len(suffixTmp)
            tableItem = {self.__tableItemValueKey: matcher[i], self.__tableItemCountKey: matchCount}
            self.__PMTable.append(tableItem)
    
    def __searchLoop(self, content, start, machedCount, result):
        if start + machedCount >= (len(content) - 1):
            return

        tableOffset = 0
        lastMatchedTableItem = None
        for i in range(start + machedCount, len(content), 1):
            currentChar = content[i]
            tableItem = self.__PMTable[machedCount + tableOffset]
            tableItemValue = tableItem[self.__tableItemValueKey]
            if tableItemValue == currentChar:
                #matched
                tableOffset = tableOffset + 1
                lastMatchedTableItem = tableItem
                if (tableOffset + machedCount) == len(self.__PMTable):
                    #finded!
                    result.append(start)
                    self.__searchLoop(content, start + len(self.__PMTable), 0, result)
                    break
            else:
                #jump(matched count - PMTable count of this char)
                jumpCount = 0
                if lastMatchedTableItem != None:
                    jumpCount = lastMatchedTableItem[self.__tableItemCountKey]
                offsetForNextLoop = tableOffset - jumpCount
                if offsetForNextLoop == 0:
                    offsetForNextLoop = 1
                self.__searchLoop(content, start + offsetForNextLoop, jumpCount, result)
                break

    def search(self, content):
        result = []
        self.__searchLoop(content, 0, 0, result)
        return result