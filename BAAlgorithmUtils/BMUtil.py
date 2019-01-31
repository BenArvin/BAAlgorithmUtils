#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys, os

class BMUtil(object):
    def __init__(self):
        super(BMUtil, self).__init__()
        self.__matcher = None
        self.badCharTable = {}
        self.goodSuffixTable = {}

    def __buildBadCharDic(self, matcher):
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
        
        #build badCharTable
        self.badCharTable = {}
        for i in range(matcherLen, 0, -1):
            for charTmp in charLocations.keys():
                innerResult = {}
                if charTmp in self.badCharTable:
                    innerResult = self.badCharTable[charTmp]
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
                self.badCharTable[charTmp] = innerResult

    def __getOffsetByBadCharRule(self, char, stopLocation):
        if char in self.badCharTable:
            innerLocationTable = self.badCharTable[char]
            return stopLocation - innerLocationTable[str(stopLocation)]
        else:
            return stopLocation + 1

    def __buildGoodSuffixDic(self, matcher):
        self.goodSuffixTable = {}
        matcherLen = len(matcher)
        for i in range(matcherLen, 1, -1):
            tmpSuffix = matcher[i - 1 : matcherLen]
            tmpSuffixLen = len(tmpSuffix)
            finded = False
            locationTmp = matcherLen - tmpSuffixLen - 1
            while True:
                if locationTmp <= 0 - tmpSuffixLen:
                    break
                matchedThisTime = True
                for j in range(0, tmpSuffixLen, 1):
                    if locationTmp + j < 0:
                        continue
                    if tmpSuffix[j] != matcher[locationTmp + j]:
                        matchedThisTime = False
                if matchedThisTime == True:
                    finded = True
                    break
                locationTmp = locationTmp - 1
            
            if finded == True:
                self.goodSuffixTable[tmpSuffix] = i - 1 - locationTmp
            else:
                self.goodSuffixTable[tmpSuffix] = matcherLen
    
    def __getOffsetByGoodSuffixRule(self, matchedPart):
        if matchedPart == None or len(matchedPart) == 0:
            return 0
        return self.goodSuffixTable[matchedPart]

    def setMatcher(self, matcher):
        if matcher == None or len(matcher) == 0:
            return
        self.__matcher = matcher
        self.__buildBadCharDic(self.__matcher)
        self.__buildGoodSuffixDic(self.__matcher)
        
    def __searchLoop(self, content, duplMode, matcher, start, result):
        if start + len(matcher) > len(content):
            return
        finded = True
        offsetNextLoop = len(matcher)
        matchedPart = ""
        for i in range(len(matcher), 0, -1):
            currentContentChar = content[start + i - 1]
            currentMatcherChar = matcher[i - 1]
            if currentContentChar != currentMatcherChar:
                offsetOfBadChar = self.__getOffsetByBadCharRule(currentContentChar, i - 1)
                offsetOfGoodSuffix = self.__getOffsetByGoodSuffixRule(matchedPart)
                offsetNextLoop = max(offsetOfBadChar, offsetOfGoodSuffix)
                finded = False
                break
            else:
                matchedPart = currentContentChar + matchedPart
        if finded == True:
            if duplMode == True:
                offsetNextLoop = 1
            result.append(start)
        self.__searchLoop(content, duplMode, matcher, start + offsetNextLoop, result)

    def search(self, content, duplMode):
        result = []
        self.__searchLoop(content, duplMode, self.__matcher, 0, result)
        return result