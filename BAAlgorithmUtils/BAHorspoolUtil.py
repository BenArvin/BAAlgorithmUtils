#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys, os

class BAHorspoolUtil(object):
    def __init__(self):
        super(BAHorspoolUtil, self).__init__()
        self.__matcher = None
        self.charLocationTable = {}

    def __buildCharLocationTable(self, matcher):
        #find positions every char
        charLocations = {}
        matcherLen = len(matcher)
        for i in range(matcherLen):
            currentChar = matcher[i]
            locations = []
            if currentChar in charLocations:
                locations = charLocations[currentChar]
            locations.append(i)
            charLocations[currentChar] = locations
        
        #build charLocationTable
        self.charLocationTable = {}
        for i in range(matcherLen, 0, -1):
            for charTmp in charLocations.keys():
                innerResult = {}
                if charTmp in self.charLocationTable:
                    innerResult = self.charLocationTable[charTmp]
                locationsTmp = charLocations[charTmp]
                finded = False
                for j in range(len(locationsTmp), 0, -1):
                    locationTmp = locationsTmp[j - 1]
                    if locationTmp <= i - 1:
                        innerResult[str(i - 1)] = locationTmp
                        finded = True
                        break
                if finded == False:
                    innerResult[str(i - 1)] = -1
                self.charLocationTable[charTmp] = innerResult

    def __getOffset(self, flagChar, stopLocation, matcherLen):
        if flagChar in self.charLocationTable:
            innerLocationTable = self.charLocationTable[flagChar]
            return matcherLen - 1 - innerLocationTable[str(stopLocation)]
        else:
            return matcherLen

    def setMatcher(self, matcher):
        if matcher == None or len(matcher) == 0:
            return
        self.__matcher = matcher
        self.__buildCharLocationTable(self.__matcher)
        
    def __searchLoop(self, content, duplMode, matcher, start, result):
        if start + len(matcher) > len(content):
            return
        matcherLen = len(matcher)
        flagChar = content[start + matcherLen - 1]
        finded = True
        offsetNextLoop = matcherLen
        for i in range(matcherLen - 1, 0, -1):
            currentContentChar = content[start + i]
            currentMatcherChar = matcher[i]
            if currentContentChar != currentMatcherChar:
                offsetNextLoop = self.__getOffset(flagChar, i, len(matcher))
                finded = False
                break
        if finded == True:
            if duplMode == True:
                offsetNextLoop = 1
            result.append(start)
        self.__searchLoop(content, duplMode, matcher, start + offsetNextLoop, result)

    def search(self, content, duplMode):
        result = []
        self.__searchLoop(content, duplMode, self.__matcher, 0, result)
        return result