#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys, os

class BABMUtil(object):
    def __init__(self):
        super(BABMUtil, self).__init__()
        self.__matcher = None
        self.badCharTable = {}
        self.goodSuffixTable = {}

    def __buildBadCharDic(self, matcher):
        self.badCharTable = {}
        matcherLen = len(matcher)
        for i in range(matcherLen):
            currentChar = matcher[i]
            locations = []
            if currentChar in self.badCharTable:
                locations = self.badCharTable[currentChar]
            locations.append(i)
            self.badCharTable[currentChar] = locations

    def __getOffsetByBadCharRule(self, char, stopLocation):
        badCharLocations = []
        if char in self.badCharTable:
            badCharLocations = self.badCharTable[char]
        for i in range(len(badCharLocations) - 1, 0, -1):
            locationTmp = badCharLocations[i]
            if locationTmp < stopLocation:
                return stopLocation - locationTmp
        return stopLocation + 1

    def __buildGoodSuffixDic(self, matcher):
        self.goodSuffixTable = {}
        matcherLen = len(matcher)
        for i in range(matcherLen - 1, 0, -1):
            tmpSuffix = matcher[i : matcherLen]
            tmpSuffixLen = len(tmpSuffix)
            finded = False
            locationTmp = matcherLen - tmpSuffixLen - 1
            while True:
                if locationTmp < 0 - tmpSuffixLen:
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
                self.goodSuffixTable[tmpSuffix] = i - locationTmp
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
        for i in range(len(matcher) - 1, 0, -1):
            currentContentChar = content[start + i]
            currentMatcherChar = matcher[i]
            if currentContentChar != currentMatcherChar:
                offsetOfBadChar = self.__getOffsetByBadCharRule(currentContentChar, i)
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